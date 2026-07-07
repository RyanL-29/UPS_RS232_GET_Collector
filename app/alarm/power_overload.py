from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

POWER_OVERLOAD = UPSNMC_AlarmInfo(
    alarm_uuid="5f7cb9d8-c659-4f1f-934b-badd463373d2",
    name="Power overload",
    active_message="Power overload",
    resolved_message="No power overload",
    severity=UPSNMC_SeverityLevel.WARNING,
)
