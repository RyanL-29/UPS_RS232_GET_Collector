from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BYPASS_NOT_AVAILABLE = UPSNMC_AlarmInfo(
    alarm_uuid="bc2d5455-d1ad-44af-a709-3ff0f89feb58",
    name="Bypass not available",
    active_message="Bypass not available",
    resolved_message="Bypass available",
    severity=UPSNMC_SeverityLevel.WARNING,
)
