from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_DISCHARGING = UPSNMC_AlarmInfo(
    alarm_uuid="5a603b7c-b9af-4af2-b837-6372a8813bf6",
    name="Battery discharging",
    active_message="Battery discharging",
    resolved_message="Battery no longer discharging",
    severity=UPSNMC_SeverityLevel.INFO,
)
