from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BYPASS_MODE = UPSNMC_AlarmInfo(
    alarm_uuid="8f30cb44-11c3-4bea-bc8f-0f279a99c0c7",
    name="Bypass mode",
    active_message="Bypass mode",
    resolved_message="No longer on bypass",
    severity=UPSNMC_SeverityLevel.WARNING,
)
