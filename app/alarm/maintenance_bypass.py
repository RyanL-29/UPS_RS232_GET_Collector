from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

MAINTENANCE_BYPASS = UPSNMC_AlarmInfo(
    alarm_uuid="0f1b1ec2-2b2a-4bc2-b057-2f6cba4ed6bf",
    name="Maintenance bypass",
    active_message="Maintenance bypass",
    resolved_message="Not on maintenance bypass",
    severity=UPSNMC_SeverityLevel.WARNING,
)
