from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

ESS_HIGH_EFFICIENCY_MODE = UPSNMC_AlarmInfo(
    alarm_uuid="a9ac150b-e8ba-4fbb-a4d6-7863e0c5f9fd",
    name="On high efficiency / On ESS mode",
    active_message="On high efficiency / On ESS mode",
    resolved_message="High efficiency disabled / ESS disabled",
    severity=UPSNMC_SeverityLevel.INFO,
)
