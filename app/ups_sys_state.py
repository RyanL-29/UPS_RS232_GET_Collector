from enum import StrEnum
from app.schemas.ups_alarm import UPSNMC_AlarmInfo
from app.alarm import *


class UPS_SYS_STATE(StrEnum):
    POWER_ON = "Offline Mode"
    STANDBY = "Offline Mode"
    BYPASS = "Bypass Mode"
    LINE = "Online Mode"
    BATTERY = "Battery Mode"
    BATTERY_TEST = "Online Mode"
    FAULT = "Bypass Mode"
    CONVERTER = "Online Mode"
    HE = "High Efficiency Mode"
    SHUTDOWN = "Offline Mode"
    UKNOWN = "Unknown"


SYS_STATE_ORDER_MAP: list[tuple[UPS_SYS_STATE, list[UPSNMC_AlarmInfo]]] = [
    (UPS_SYS_STATE.POWER_ON, [LOAD_NOT_POWERED]),
    (UPS_SYS_STATE.STANDBY, [LOAD_NOT_POWERED]),
    (UPS_SYS_STATE.BYPASS, [LOAD_UNPROTECTED, BYPASS_MODE]),
    (UPS_SYS_STATE.LINE, []),
    (UPS_SYS_STATE.BATTERY, [ON_BATTERY]),
    (UPS_SYS_STATE.BATTERY_TEST, []),
    (UPS_SYS_STATE.FAULT, [INTERNAL_FAILURE, LOAD_UNPROTECTED]),
    (UPS_SYS_STATE.CONVERTER, []),
    (UPS_SYS_STATE.HE, [ESS_HIGH_EFFICIENCY_MODE]),
    (UPS_SYS_STATE.SHUTDOWN, [LOAD_NOT_POWERED]),
]
