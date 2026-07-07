from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

INTERNAL_FAILURE = UPSNMC_AlarmInfo(
    alarm_uuid="e6859b17-8859-4f87-8de2-c57684ea6d63",
    name="Internal failure",
    active_message="Internal failure",
    resolved_message="End of internal failure",
    advice="Service required",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
