from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

AMBIENT_TEMP_TOO_LOW = UPSNMC_AlarmInfo(
    alarm_uuid="b2a4f0f0-38d5-4920-831f-39ea8c43cb6d",
    name="Ambient temperature is too low",
    active_message="Ambient temperature is too low",
    resolved_message="Ambient temperature is OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
