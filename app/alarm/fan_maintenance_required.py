from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

FAN_MAINTENANCE_REQUIRED = UPSNMC_AlarmInfo(
    alarm_uuid="3c3439a6-20c0-4873-b573-eb2241145622",
    name="Fan maintenance required",
    active_message="Fan maintenance required",
    resolved_message="No fan maintenance required",
    severity=UPSNMC_SeverityLevel.WARNING,
)
