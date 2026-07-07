from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

INPUT_AC_NOT_PRESENT = UPSNMC_AlarmInfo(
    alarm_uuid="2f410d86-44a2-4ce1-b08c-ebef722814d2",
    name="Input AC not present",
    active_message="Input AC not present",
    resolved_message="Input AC present",
    severity=UPSNMC_SeverityLevel.WARNING,
)
