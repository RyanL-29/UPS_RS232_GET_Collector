from typing import Optional
from typing import Optional
from pydantic import BaseModel
from app.schemas.base import *

class Serial_Device_Connection_Info(BaseModel):
    port: str = "/dev/null"
    baud_rate: Optional[int] = 2400
    data_bits: Optional[int] = 8
    stop_bits: Optional[int] = 1
    parity: Optional[str] = "N"
    rtscts: Optional[bool] = False
    dsrdtr: Optional[bool] = False
    send_line_ending: Optional[str] = ""
    read_line_ending: Optional[str] = ""
    
class Serial_Data_Fetching_Info(Base_Data_Fetching_Info):
    cmd: Optional[str] = ""
    
class Serial_Action_Info(Base_Action_Info):
    pass