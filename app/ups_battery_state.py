from enum import StrEnum
from app.alarm import *


class UPS_BATTERY_STATE(StrEnum):
    IDLE = "Idle"
    PROCESSING = "In Progress"
    RESULT_SUCCESS = "Success"
    RESULT_FAIL = "Failed"
    INHIBITE = "Inhibite"
    TEST_CANCEL = "Cancel"
    UKNOWN = "Unknown"


BAT_STATE_ORDER_MAP_Q6: list[tuple[UPS_BATTERY_STATE, list[UPSNMC_AlarmInfo]]] = [
    (UPS_BATTERY_STATE.IDLE, []),
    (UPS_BATTERY_STATE.PROCESSING, [BATTERY_TEST_IN_PROGRESS]),
    (UPS_BATTERY_STATE.RESULT_SUCCESS, []),
    (UPS_BATTERY_STATE.RESULT_FAIL, [BATTERY_TEST_FAILED]),
    (UPS_BATTERY_STATE.INHIBITE, []),
    (UPS_BATTERY_STATE.TEST_CANCEL, []),
    (UPS_BATTERY_STATE.UKNOWN, []),
    (UPS_BATTERY_STATE.UKNOWN, []),
]
