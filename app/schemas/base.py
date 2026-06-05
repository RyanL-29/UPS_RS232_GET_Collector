import json
from typing import Any, Optional, Union, Dict
from typing import Optional, List, Any
from pydantic import BaseModel, model_validator, Field

from app.schemas.camel_base import CamelBase
# The Device_Data_Fetching_Rule class takes the latest returned value of a sensor, and performs the designated operator against the list of conditions (i.e. IN, OR, AND).
# If the conditions returns true, it will set the return_val into the return_key on the Parent's Upload_Type class (i.e. Attribute or Telemetry)
# The upload_all function decides whether all of the keys that belongs to the Parent aka both Attributes and Telemetry
# Optionally the condition can also trigger actions inside Action Set that belongs to the parent
class Device_Data_Fetching_Rule(BaseModel):
    operator: str = ""
    conditions: List[Any] = []
    return_val: str = ""
    return_key: str = ""
    upload_all: Optional[bool] = False
    upload_all_onchange: Optional[bool] = False
    action: List[str] = []
    
class Base_Data_Fetching_Info(BaseModel):
    key: str = ""
    polling_interval: Optional[int] = -1
    saving_interval: Optional[int] = -1
    upload_interval: Optional[int] = -1
    calculated_field: str = ""
    rule_set: List[Device_Data_Fetching_Rule] = []
    data_converter: Optional[str] = "DefaultConverter"
    calculated_fetcher: bool = False
    upload_on_change: Optional[bool] = False
    save_on_change: Optional[bool] = False
            
class Base_Action_Info(BaseModel):
    action_name: str = ""
    value: Optional[Union[str, bool, Dict, int, float]] = ""
    
    

