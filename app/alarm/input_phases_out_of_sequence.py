from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

INPUT_PHASES_OUT_OF_SEQUENCE = UPSNMC_AlarmInfo(
    alarm_uuid="4696ba1b-03c8-475c-ade8-637f811d2390",
    name="Input phases out of sequence",
    active_message="Input phases out of sequence",
    resolved_message="Input phases wired OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
