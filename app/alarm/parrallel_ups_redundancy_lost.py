from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

PARRALLEL_UPS_REDUNDANCY_LOST = UPSNMC_AlarmInfo(
    alarm_uuid="ad2e043a-0bd0-4ef9-a28e-30166abe1daa",
    name="Parallel UPS redundancy lost",
    active_message="Parallel UPS redundancy lost",
    resolved_message="Parallel UPS redundancy OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
