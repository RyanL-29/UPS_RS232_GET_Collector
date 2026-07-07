from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

SERVICE_SCHEDULED = UPSNMC_AlarmInfo(
    alarm_uuid="686dfc22-0e43-4bc4-97eb-45fe0650f174",
    name="Service scheduled",
    active_message="Service scheduled",
    resolved_message="Service no longer scheduled",
    severity=UPSNMC_SeverityLevel.INFO,
)
