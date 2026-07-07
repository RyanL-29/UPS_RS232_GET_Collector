from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_LOW_STATE_OF_CHARGE = UPSNMC_AlarmInfo(
    alarm_uuid="d21de4e8-4c8a-4c2d-b606-243e9d69eed1",
    name="Battery low state of charge",
    active_message="Battery low state of charge",
    resolved_message="Battery state of charge OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
