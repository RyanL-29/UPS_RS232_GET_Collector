from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BUCK_MODE = UPSNMC_AlarmInfo(
    alarm_uuid="0f8f1f41-fd23-4547-887e-14595f571e8a",
    name="On AVR (Buck)",
    active_message="On AVR (Buck)",
    resolved_message="End of AVR (Buck)",
    severity=UPSNMC_SeverityLevel.INFO,
)
