from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

LOAD_UNPROTECTED = UPSNMC_AlarmInfo(
    alarm_uuid="a80bd880-931b-4c2c-956c-ea7c90743346",
    name="Load unprotected",
    active_message="Load unprotected",
    resolved_message="Load protected",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
