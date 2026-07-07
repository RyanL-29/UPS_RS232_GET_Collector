from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

Q6 = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="Q6",
        cmd="Q6",
        reply_max_length=110, reply_min_length=110,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="input_voltage_1", start_index=0, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="input_voltage_2", start_index=6, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="input_voltage_3", start_index=12, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="input_frequency", start_index=18, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_voltage_1", start_index=23, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_voltage_2", start_index=29, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_voltage_3", start_index=35, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_frequency", start_index=41, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_voltage_positive", start_index=58, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_voltage_negative", start_index=64, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="ups_temperature", start_index=70, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_remain_time_second", start_index=75, length=5, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_remain_percentage", start_index=81, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="system_state", start_index=85, length=1, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_state", start_index=86, length=1, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_capacity", start_index=81, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="q6_fault_code", start_index=88, length=8, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="q6_warnings", start_index=97, length=8, data_type="string")
        ]
    )


# q6_warnings mapping app/alarm/_init_.py (ALARM_MAPPING) # HEX
# system_state mapping app/ups_sys_state.py (SYS_STATE_ORDER_MAP) # Not HEX !! Left Digit sys_state 
# system_state ups_battery_state.py  # Not HEX !! Right Digit battery_state