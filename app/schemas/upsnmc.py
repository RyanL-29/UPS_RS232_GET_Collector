from app.schemas.base import *
from app.schemas.serial import *
from typing import Optional, List
from pydantic import BaseModel

class UPSNMC_Connection_Info(Serial_Device_Connection_Info):
    pass

class UPSNMC_Reply_Data_Parse_Rules(BaseModel):
    start_index: int = 0
    length: int = 0
    key: str = ""
    data_type: str = "" # string, float, integer
    
class UPSNMC_Data_Fetching_Info(Serial_Data_Fetching_Info):
    require_socket_group_count: Optional[bool] = False
    reply_min_length: int = -1
    reply_max_length: int = -1
    start_with_regex: Optional[str] = ""
    parse_rules: List[UPSNMC_Reply_Data_Parse_Rules] = []
    
class UPSNMC_Action_Info(Serial_Action_Info):
    pass