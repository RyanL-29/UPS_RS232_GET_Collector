from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_POLARITY_REVERSED = UPSNMC_AlarmInfo(
    alarm_uuid="af325d47-f996-4dfb-a140-36ca292d729d",
    name="Battery polarity reversed",
    active_message="Battery polarity reversed",
    resolved_message="No battery polarity reversed",
    severity=UPSNMC_SeverityLevel.WARNING,
)
