from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BOOST_MODE = UPSNMC_AlarmInfo(
    alarm_uuid="cfd4f893-fcad-42ea-a705-6cb124487a28",
    name="On AVR (Boost)",
    active_message="On AVR (Boost)",
    resolved_message="End of AVR (Boost)",
    severity=UPSNMC_SeverityLevel.INFO,
)
