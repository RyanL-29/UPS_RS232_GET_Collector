from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

SEQUENTIAL_SHUTDOWN_SCHEDULED = UPSNMC_AlarmInfo(
    alarm_uuid="e3790cc8-c3f8-4d6f-b032-503f4e3ee379",
    name="Sequential shutdown scheduled",
    active_message="{{component}} Sequential shutdown scheduled",
    resolved_message="Sequential shutdown canceled",
    severity=UPSNMC_SeverityLevel.INFO,
)
