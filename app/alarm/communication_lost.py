from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

COMMUNICATION_LOST = UPSNMC_AlarmInfo(
    alarm_uuid="260589ca-91e1-4d3d-a9ab-2cff7509ae84",
    name="Communication lost with device",
    active_message="Communication lost with device",
    resolved_message="Communication recovered with device",
    severity=UPSNMC_SeverityLevel.WARNING,
)
