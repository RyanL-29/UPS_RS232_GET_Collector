from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

UTILITY_AC_NOT_PRESENT = UPSNMC_AlarmInfo(
    alarm_uuid="f7da8fcd-0083-4c63-8539-a2acade42950",
    name="Utility AC not present",
    active_message="Utility AC not present",
    resolved_message="Utility AC present",
    severity=UPSNMC_SeverityLevel.INFO,
)
