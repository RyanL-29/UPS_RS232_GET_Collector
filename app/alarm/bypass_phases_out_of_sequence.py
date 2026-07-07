from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BYPASS_PHASES_OUT_OF_SEQUENCE = UPSNMC_AlarmInfo(
    alarm_uuid="5836e8f8-58d0-4370-ad8b-394264fec9ae",
    name="Bypass phases out of sequence",
    active_message="Bypass phases out of sequence",
    resolved_message="Bypass phases wired OK",
    severity=UPSNMC_SeverityLevel.WARNING,
)
