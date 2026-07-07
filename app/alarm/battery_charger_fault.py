from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_CHARGER_FAULT = UPSNMC_AlarmInfo(
    alarm_uuid="956c011a-534c-4f23-8579-38e4028e6901",
    name="Battery charger fault",
    active_message="Battery charger fault",
    resolved_message="Battery charger OK",
    advice="Check Battery",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
