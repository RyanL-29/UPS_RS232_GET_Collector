from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

GROUP_IS_OFF = UPSNMC_AlarmInfo(
    alarm_uuid="dbdaefb2-843e-421a-bcac-14797ee1ec21",
    name="Group is OFF",
    active_message="Group is OFF",
    resolved_message="Group is ON",
    severity=UPSNMC_SeverityLevel.INFO,
)
