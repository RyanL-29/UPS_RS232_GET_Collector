from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

INTERNAL_WARNING = UPSNMC_AlarmInfo(
    alarm_uuid="903b2991-63f5-4c1e-a4f0-3b4987ed6c92",
    name="Internal warning",
    active_message="Internal warning",
    resolved_message="No longer internal warning",
    severity=UPSNMC_SeverityLevel.WARNING,
)
