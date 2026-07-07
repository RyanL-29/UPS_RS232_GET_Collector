import json
import os
import serial
import threading
import time

class SerialListener:
    def __init__(self):
        self.serial_client = None
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
        self.running = True
        self.load_commands()
        
        reload_thread = threading.Thread(target=self._reload_loop, daemon=True)
        reload_thread.start()
        
        try:
            self.serial_client = serial.Serial(
                port='COM19',
                baudrate=2400,
                bytesize=8,
                stopbits=1,
                parity="N",
                rtscts=False,
                dsrdtr=False,
                timeout=1.0
            )
            print(f"Started listening on {self.serial_client.port}...")
        except Exception as e:
            print(f"Failed to initialize serial port: {e}")
            return

        try:
            while True:
                # Read until '\r'
                raw_data = self.serial_client.read_until(b'\r')
                if raw_data:
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
                        self.serial_client.write(result.encode('utf-8'))
                        
                        escaped_result = result.replace('\r', '\\r').replace('\n', '\\n')
                        print(f"Sent: {escaped_result}")
                    else:
                        self.serial_client.write(b"NAK\r")
                        print("Sent: NAK\\r")

        except KeyboardInterrupt:
            print("\nProcess terminated by user.")
        finally:
            self.running = False
            if self.serial_client and self.serial_client.is_open:
                self.serial_client.close()
                print("Serial port closed.")

if __name__ == '__main__':
    listener = SerialListener()
    listener.run()
