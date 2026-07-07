from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

NO_BATTERY = UPSNMC_AlarmInfo(
    alarm_uuid="fa8210b1-1efe-4882-ba49-31e85c451ef1",
    name="No battery",
    active_message="No battery",
    resolved_message="Battery present",
    advice="Check Battery",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
