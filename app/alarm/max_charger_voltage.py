from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

MAX_CHARGER_VOLTAGE = UPSNMC_AlarmInfo(
    alarm_uuid="67b4933f-ab19-4d63-a26b-839d2e57b60d",
    name="Max charger voltage",
    active_message="Max charger voltage",
    resolved_message="Charger voltage OK",
    description="Charging voltage too high. Some Battery cell(s) may failed",
    severity=UPSNMC_SeverityLevel.WARNING,
)
