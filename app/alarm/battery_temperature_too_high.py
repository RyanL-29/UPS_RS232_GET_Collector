from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_TEMPERATURE_TOO_HIGH = UPSNMC_AlarmInfo(
    alarm_uuid="7fa482ac-d72c-4c65-9177-7fcbb2ca744c",
    name="Battery temperature too high",
    active_message="Battery temperature too high",
    resolved_message="Battery temperature OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
