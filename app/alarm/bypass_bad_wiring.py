from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BYPASS_BAD_WIRING = UPSNMC_AlarmInfo(
    alarm_uuid="2fccdb0c-cc15-4f2c-b690-3533f7bae6c5",
    name="Bypass bad wiring",
    active_message="Bypass bad wiring",
    resolved_message="Bypass wiring OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
