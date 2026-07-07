from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_NEEDS_SERVICE = UPSNMC_AlarmInfo(
    alarm_uuid="25ff6f32-f61e-40ff-bb68-95f27c0add49",
    name="Battery needs service",
    active_message="Battery needs service",
    resolved_message="Battery OK",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
