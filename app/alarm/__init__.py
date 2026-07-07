from app.alarm.ambient_temp_too_high import AMBIENT_TEMP_TOO_HIGH
from app.alarm.ambient_temp_too_low import AMBIENT_TEMP_TOO_LOW
from app.alarm.battery_charger_fault import BATTERY_CHARGER_FAULT
from app.alarm.battery_discharging import BATTERY_DISCHARGING
from app.alarm.battery_low_state_of_charge import (
    BATTERY_LOW_STATE_OF_CHARGE,
)
from app.alarm.battery_needs_service import BATTERY_NEEDS_SERVICE
from app.alarm.battery_polarity_reversed import (
    BATTERY_POLARITY_REVERSED,
)
from app.alarm.battery_temperature_too_high import (
    BATTERY_TEMPERATURE_TOO_HIGH,
)
from app.alarm.battery_test_failed import BATTERY_TEST_FAILED
from app.alarm.battery_test_in_progress import BATTERY_TEST_IN_PROGRESS
from app.alarm.boost_mode import BOOST_MODE
from app.alarm.buck_mode import BUCK_MODE
from app.alarm.bypass_bad_wiring import BYPASS_BAD_WIRING
from app.alarm.bypass_mode import BYPASS_MODE
from app.alarm.bypass_not_available import BYPASS_NOT_AVAILABLE
from app.alarm.bypass_phases_out_of_sequence import (
    BYPASS_PHASES_OUT_OF_SEQUENCE,
)
from app.alarm.communication_lost import COMMUNICATION_LOST
from app.alarm.emergency_power_off import EMERGENCY_POWER_OFF
from app.alarm.end_of_warranty import END_OF_WARRANTY
from app.alarm.ess_high_efficiency_mode import ESS_HIGH_EFFICIENCY_MODE
from app.alarm.fan_fault import FAN_FAULT
from app.alarm.fan_maintenance_required import FAN_MAINTENANCE_REQUIRED
from app.alarm.group_is_off import GROUP_IS_OFF
from app.alarm.input_ac_not_present import INPUT_AC_NOT_PRESENT
from app.alarm.input_bad_wiring import INPUT_BAD_WIRING
from app.alarm.input_phases_out_of_sequence import (
    INPUT_PHASES_OUT_OF_SEQUENCE,
)
from app.alarm.internal_failure import INTERNAL_FAILURE
from app.alarm.internal_warning import INTERNAL_WARNING
from app.alarm.load_not_powered import LOAD_NOT_POWERED
from app.alarm.load_unprotected import LOAD_UNPROTECTED
from app.alarm.maintenance_bypass import MAINTENANCE_BYPASS
from app.alarm.max_charger_voltage import MAX_CHARGER_VOLTAGE
from app.alarm.no_battery import NO_BATTERY
from app.alarm.on_battery import ON_BATTERY
from app.alarm.overload_pre_alarm import OVERLOAD_PRE_ALARM
from app.alarm.parrallel_ups_redundancy_lost import (
    PARRALLEL_UPS_REDUNDANCY_LOST,
)
from app.alarm.power_overload import POWER_OVERLOAD
from app.alarm.rectifier_failure import RECTIFIER_FAILURE
from app.alarm.sequential_shutdown_scheduled import (
    SEQUENTIAL_SHUTDOWN_SCHEDULED,
)
from app.alarm.service_scheduled import SERVICE_SCHEDULED
from app.alarm.utility_ac_not_present import UTILITY_AC_NOT_PRESENT
from app.alarm.utility_input_neutral_lost import (
    UTILITY_INPUT_NEUTRAL_LOST,
)
from app.schemas.ups_alarm import UPSNMC_AlarmInfo

# MSB
ALARM_MAPPING: list[list[UPSNMC_AlarmInfo]] = [
    [],
    [],
    [RECTIFIER_FAILURE],
    [FAN_MAINTENANCE_REQUIRED],
    [BATTERY_TEMPERATURE_TOO_HIGH],
    [AMBIENT_TEMP_TOO_HIGH],
    [AMBIENT_TEMP_TOO_LOW],
    [END_OF_WARRANTY],
    [SERVICE_SCHEDULED],
    [BATTERY_NEEDS_SERVICE],
    [],
    [PARRALLEL_UPS_REDUNDANCY_LOST],
    [],
    [],
    [BATTERY_CHARGER_FAULT],
    [MAINTENANCE_BYPASS],
    [FAN_FAULT],
    [POWER_OVERLOAD],
    [OVERLOAD_PRE_ALARM],
    [BATTERY_POLARITY_REVERSED],
    [MAX_CHARGER_VOLTAGE],
    [BATTERY_LOW_STATE_OF_CHARGE],
    [NO_BATTERY],
    [],
    [BYPASS_NOT_AVAILABLE],
    [INPUT_BAD_WIRING],
    [INPUT_PHASES_OUT_OF_SEQUENCE],
    [UTILITY_INPUT_NEUTRAL_LOST],
    [
        BYPASS_NOT_AVAILABLE,
        UTILITY_AC_NOT_PRESENT,
        INPUT_AC_NOT_PRESENT,
        BATTERY_DISCHARGING,
    ],
    [],
    [EMERGENCY_POWER_OFF],
    [INTERNAL_WARNING],
]
