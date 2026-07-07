from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

EMERGENCY_POWER_OFF = UPSNMC_AlarmInfo(
    alarm_uuid="4275e77e-c8d7-44b2-add1-905d7d54d941",
    name="Emergency power OFF",
    active_message="Emergency power OFF",
    resolved_message="No emergency OFF",
    severity=UPSNMC_SeverityLevel.WARNING,
)
