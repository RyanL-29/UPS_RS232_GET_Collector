from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_TEST_IN_PROGRESS = UPSNMC_AlarmInfo(
    alarm_uuid="0c509f1d-59f2-413b-83ab-2bee9cac2c2f",
    name="Battery test in progress",
    active_message="Battery test in progress",
    resolved_message="Battery test finished",
    severity=UPSNMC_SeverityLevel.INFO,
)
