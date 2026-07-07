from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

ON_BATTERY = UPSNMC_AlarmInfo(
    alarm_uuid="1981088c-7be9-42c8-ad04-067985d7c4d4",
    name="On battery",
    active_message="On battery",
    resolved_message="No more on battery",
    severity=UPSNMC_SeverityLevel.WARNING,
)
