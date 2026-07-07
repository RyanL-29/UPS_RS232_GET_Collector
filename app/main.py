from copy import deepcopy
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
from app.GET import *
import codecs
import serial
from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info
import time
from openpyxl import Workbook
from datetime import datetime
from app.utils.jinja2_extension import XTemplate
import json
import re
from tqdm import tqdm

class UPS_RS232_COLLECTOR:
    def __init__(self) -> None:
        self.serial_client: 'serial.Serial'
        self.serial_job_lock = threading.Lock()
        self.write_line_ending = '\r'
        self.read_line_ending = '\r'
        self.read_line_end_str = codecs.getdecoder("unicode_escape")(self.read_line_ending.encode('utf-8'))[0]
        self.socket_group_count = self.get_ups_load_socket_group_count()
        self.collector_job = []
        self.readings: list[tuple[UPSNMC_Data_Fetching_Info, str]] = []
        
    def connect(self):
        self.serial_client = serial.Serial(
            port = 'COM21',
            baudrate = 2400,
            bytesize = 8,
            stopbits = 1,
            parity = "N",
            rtscts = False,
            dsrdtr = False,
            timeout = 1.0
        )
        
    def init(self):
        try:
            self.connect()
            self.process_job_info()
            self.collect()
        except Exception as e:
            print(e)
            
    def get_ups_load_socket_group_count(self):
        socket_group_error = False
        socket_group_count = 1
        cmd_template: XTemplate = XTemplate("QLSS{{ '%02d' % ups_load_socket_group_count }}?")
        while not socket_group_error:
            try:
                self.connect()
                decode_unicode_escape = codecs.getdecoder("unicode_escape")
                cmd = cmd_template.hybrid_render({"ups_load_socket_group_count": socket_group_count})
                cmd_tuple = decode_unicode_escape(f"{cmd}{self.write_line_ending}".encode('utf-8'))
                cmd_str = cmd_tuple[0]
                self.serial_client.write(cmd_str.encode('utf-8'))
                result = self.serial_client.read_until(str.encode(self.read_line_end_str))
                self.serial_client.close()
                result_str = result.decode("utf-8") # type: ignore
                if "(" in result_str:
                    socket_group_count += 1
                else:
                    socket_group_count -= 1
                    raise Exception("Invalid Result")
            except Exception as e:
                socket_group_error = True
        
        if socket_group_count < 0:
            socket_group_count = 0
        self.ups_load_socket_group_count = socket_group_count
        
        return socket_group_count
        
    
    def process_job_info(self):
        for cmd in GET_CMD:
            if cmd.calculated_fetcher:
                continue
            if cmd.require_socket_group_count:
                for i in range(1, self.ups_load_socket_group_count + 1):
                    _cmd = deepcopy(cmd)
                    cmd_template: XTemplate = XTemplate(_cmd.cmd) # type: ignore
                    _cmd.key = cmd_template.render({"ups_load_socket_group_count": str(i).zfill(2)})
                    _cmd.cmd = cmd_template.render({"ups_load_socket_group_count": str(i).zfill(2)})
                    for k, v in enumerate(_cmd.parse_rules):
                        rule_key_template: XTemplate = XTemplate(v.key)
                        _cmd.parse_rules[k].key = rule_key_template.render({"ups_load_socket_group_count": i})
                    self.collector_job.append(_cmd)
            else:
                self.collector_job.append(cmd)
                
    def parse_msg(self):
        result = {}
        print("Parsing messages...")
        pbar = tqdm(self.readings, desc="Parsing", unit="msg")
        for reading_info in pbar:
            job_info, decoded_msg = reading_info
            pbar.set_postfix({"Command": job_info.cmd})
            if 'NAK' in decoded_msg:
                continue
            
            if len(decoded_msg) < job_info.reply_min_length or len(decoded_msg) > job_info.reply_max_length:
                print(f"Commnad: {job_info.cmd} Unexpected reply length")
                continue
            
            if len(job_info.start_with_regex) > 0:  # type: ignore
                start_with_regex = f"^{job_info.start_with_regex}"
                try:
                    re.compile(start_with_regex)
                except:
                    print(f"Commnad: {job_info.cmd} Invalid start with regex string")
                    continue
                    
                if not re.search(start_with_regex, decoded_msg):
                   print(f"Commnad: {job_info.cmd} Start char not found")
                   continue
                
                decoded_msg = re.sub(start_with_regex, "", decoded_msg)
                
            for parse_rule in job_info.parse_rules:
                value = decoded_msg[parse_rule.start_index:(parse_rule.start_index + parse_rule.length)]
                try:
                    if parse_rule.data_type == "string":
                        value = str(value)
                    elif parse_rule.data_type == "integer":
                        value = int(value)
                    elif parse_rule.data_type == "float":
                        value = float(value)
                except ValueError:
                    pass
                result[parse_rule.key] = value
                
        return result
         
    def collect(self):
        wb = Workbook()
        ws = wb.active
        if ws:
            ws.title = "Raw Results"
            ws.append(["Command", "Result", "Response Time"])
        
        json_data = []
        
        print("Collecting data...")
        pbar = tqdm(self.collector_job, desc="Collecting", unit="cmd")
        for cmd in pbar:
            pbar.set_postfix({"Command": cmd.cmd})
            result, job_info, response_time = self.serial_job(cmd)
            if not result or not job_info:
                continue
            self.readings.append((job_info, result))
            if ws:
                ws.append([job_info.cmd, result, response_time])
            
            json_data.append({
                "cmd": job_info.cmd,
                "result": result
            })
                
        parsed_result = self.parse_msg()
        
        ws_parsed = wb.create_sheet(title="Parsed Results")
        ws_parsed.append(["Key", "Value"])
        if parsed_result:
            for key, value in parsed_result.items():
                ws_parsed.append([key, value])
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ups_results_{timestamp}.xlsx"
        wb.save(filename)
        print(f"Saved results to {filename}")
        
        json_filename = f"ups_results_{timestamp}.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
        print(f"Saved JSON results to {json_filename}")
            
    def serial_job(self, job_info: 'UPSNMC_Data_Fetching_Info') -> 'tuple[str | None, UPSNMC_Data_Fetching_Info | None, float | None]':
        with self.serial_job_lock:
            try:
                decode_unicode_escape = codecs.getdecoder("unicode_escape")
                cmd_tuple = decode_unicode_escape(f"{job_info.cmd}\r".encode('utf-8'))
                cmd_str = cmd_tuple[0]
                start_time = time.perf_counter()
                self.serial_client.write(cmd_str.encode('utf-8'))
                end_time = time.perf_counter()
                result = self.serial_client.read_until(str.encode(self.read_line_end_str))
                return result.decode('utf-8'), job_info, end_time - start_time
            except Exception as e:
                print(e)
                return None, None, None
                

def main():
    rs232_collector = UPS_RS232_COLLECTOR()
    rs232_collector.init()
    

if __name__ == "__main__":
    main()
