from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

OVERLOAD_PRE_ALARM = UPSNMC_AlarmInfo(
    alarm_uuid="00564f79-2ce8-4e54-86b1-4215c7265612",
    name="Overload pre-alarm",
    active_message="Overload pre-alarm",
    resolved_message="No overload pre-alarm",
    severity=UPSNMC_SeverityLevel.WARNING,
)
