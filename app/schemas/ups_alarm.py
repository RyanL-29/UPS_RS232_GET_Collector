from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from enum import StrEnum


class UPSNMC_SeverityLevel(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class UPSNMC_AlarmInfo(BaseModel):
    start_time: Optional[datetime] = datetime.fromtimestamp(0)
    end_time: Optional[datetime] = datetime.fromtimestamp(0)
    alarm_uuid: str
    name: str
    active_message: str
    resolved_message: str
    advice: Optional[str] = ""
    description: Optional[str] = ""
    severity: UPSNMC_SeverityLevel = Field(default=UPSNMC_SeverityLevel.INFO)
