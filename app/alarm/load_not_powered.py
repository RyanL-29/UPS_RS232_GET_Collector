from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

LOAD_NOT_POWERED = UPSNMC_AlarmInfo(
    alarm_uuid="cb6dffba-b4de-4c47-9f54-1285c6223899",
    name="Load not powered",
    active_message="Load not powered",
    resolved_message="Load protected",
    severity=UPSNMC_SeverityLevel.WARNING,
)
