from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

RECTIFIER_FAILURE = UPSNMC_AlarmInfo(
    alarm_uuid="c4fb1319-a3c1-4aec-bbe5-5c63fb8d0f93",
    name="Rectifier failure",
    active_message="Rectifier failure",
    resolved_message="Rectifier OK",
    advice="Service required",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
