from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

AMBIENT_TEMP_TOO_HIGH = UPSNMC_AlarmInfo(
    alarm_uuid="e2958653-504f-487c-87f5-7e248255ad48",
    name="Ambient temperature is too high",
    active_message="Ambient temperature is too high",
    resolved_message="Ambient temperature is OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
