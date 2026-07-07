from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

INPUT_BAD_WIRING = UPSNMC_AlarmInfo(
    alarm_uuid="4d20d115-08a8-4f21-9c5c-152ec406c252",
    name="Input bad wiring",
    active_message="Input bad wiring",
    resolved_message="Input wiring OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
