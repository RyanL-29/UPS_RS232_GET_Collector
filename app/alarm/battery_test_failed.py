from app.schemas.ups_alarm import UPSNMC_AlarmInfo, UPSNMC_SeverityLevel

BATTERY_TEST_FAILED = UPSNMC_AlarmInfo(
    alarm_uuid="2c60406d-77e4-408f-acb9-9bcd42e01567",
    name="Battery test failed",
    active_message="Battery test failed",
    resolved_message="",
    severity=UPSNMC_SeverityLevel.CRITICAL,
)
