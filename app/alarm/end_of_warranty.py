from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

END_OF_WARRANTY = UPSNMC_AlarmInfo(
    alarm_uuid="07c20664-fcfe-44e3-aad9-82fa43eafa74",
    name="End of warranty",
    active_message="End of warranty",
    resolved_message="End of warranty cleared",
    severity=UPSNMC_SeverityLevel.WARNING,
)
