from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

FAN_FAULT = UPSNMC_AlarmInfo(
    alarm_uuid="f4f0b537-2445-49c3-a3d0-306db7519b7c",
    name="Fan fault",
    active_message="Fan fault",
    resolved_message="Fan OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
