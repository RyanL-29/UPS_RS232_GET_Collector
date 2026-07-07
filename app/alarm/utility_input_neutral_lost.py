from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

UTILITY_INPUT_NEUTRAL_LOST = UPSNMC_AlarmInfo(
    alarm_uuid="af455ca7-e52d-4f22-ae76-4d9aacfd2b9e",
    name="Utility input neutral lost",
    active_message="Utility input neutral lost",
    resolved_message="No utility input neutral lost",
    severity=UPSNMC_SeverityLevel.WARNING,
)
