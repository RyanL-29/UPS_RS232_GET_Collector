from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

Q4 = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="Q4",
        cmd="Q4",
        reply_max_length=74, reply_min_length=62,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="input_voltage_1", start_index=0, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_voltage_1", start_index=24, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_percent", start_index=34, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="input_frequency", start_index=38, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_voltage_positive", start_index=51, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="ups_temperature", start_index=57, length=4, data_type="float")
        ]
    )