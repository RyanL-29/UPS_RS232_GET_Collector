import json
import os
import threading
import time
import select

try:
    import pty
    import termios
except ImportError:
    pty = None
    termios = None

class VirtualSerialDevice:
    def __init__(self):
        self.master_fd = None
        self.slave_fd = None
        self.command_map = {}
        self.running = False

    def load_commands(self):
        json_filename = 'ups_results_20260625_154942.json'
        # Try getting the json from the parent directory of this script or the current working directory
        json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), json_filename)
        if not os.path.exists(json_path):
            json_path = json_filename

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                new_map = {item['cmd']: item['result'] for item in data}
                if new_map != self.command_map:
                    self.command_map = new_map
                    print(f"Loaded {len(self.command_map)} commands from {json_path}")
        except Exception as e:
            print(f"Could not load {json_filename}: {e}")

    def _reload_loop(self):
        while self.running:
            self.load_commands()
            time.sleep(2.0)

    def run(self):
        if pty is None:
            print("The pty module is not available on this OS. This script requires Linux/Unix.")
            return

        self.running = True
        self.load_commands()
        
        reload_thread = threading.Thread(target=self._reload_loop, daemon=True)
        reload_thread.start()
        
        try:
            self.master_fd, self.slave_fd = pty.openpty()  # type: ignore
            slave_name = os.ttyname(self.slave_fd)  # type: ignore
            
            # Disable echo on slave to prevent loopback, and disable canonical mode
            if termios:
                try:
                    attrs = termios.tcgetattr(self.slave_fd)  # type: ignore
                    # attrs[3] represents the local modes (lflags)
                    attrs[3] = attrs[3] & ~termios.ECHO & ~termios.ICANON  # type: ignore
                    termios.tcsetattr(self.slave_fd, termios.TCSANOW, attrs)  # type: ignore
                except Exception:
                    pass

            print(f"Started listening on virtual port: {slave_name}")
        except Exception as e:
            print(f"Failed to initialize virtual serial port: {e}")
            return

        buffer = b""

        try:
            while self.running:
                # Wait for data to be available on master_fd
                r, w, e = select.select([self.master_fd], [], [], 1.0)
                if r:
                    try:
                        data = os.read(self.master_fd, 1024)
                    except OSError:
                        # Might happen on some systems if the other end is closed
                        continue
                        
                    if data:
                        buffer += data
                        while b'\r' in buffer:
                            idx = buffer.find(b'\r')
                            raw_data = buffer[:idx+1]
                            buffer = buffer[idx+1:]
                            
                            # Decode string
                            decoded_str = raw_data.decode('utf-8', errors='ignore')
                            
                            # Escape the line ending char and print
                            escaped_str = decoded_str.replace('\r', '\\r').replace('\n', '\\n')
                            print(f"Received: {escaped_str}")

                            # Extract command by stripping '\r' since json keys don't include it
                            cmd = decoded_str.replace('\r', '').replace('\n', '')

                            # Find the cmd inside the json results
                            if cmd in self.command_map:
                                result: str = self.command_map[cmd]
                                os.write(self.master_fd, result.encode('utf-8'))
                                
                                escaped_result = result.replace('\r', '\\r').replace('\n', '\\n')
                                print(f"Sent: {escaped_result}")
                            else:
                                os.write(self.master_fd, b"NAK\r")
                                print("Sent: NAK\\r")

        except KeyboardInterrupt:
            print("\nProcess terminated by user.")
        finally:
            self.running = False
            if self.master_fd is not None:
                os.close(self.master_fd)
            if self.slave_fd is not None:
                os.close(self.slave_fd)
            print("Virtual serial port closed.")

if __name__ == '__main__':
    listener = VirtualSerialDevice()
    listener.run()
