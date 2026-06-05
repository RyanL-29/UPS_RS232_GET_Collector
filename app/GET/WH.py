from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

WH = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="WH",
        cmd="WH",
        reply_max_length=115, reply_min_length=113,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="firmware_version", start_index=0, length=5, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="model", start_index=15, length=30, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_volt", start_index=48, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_frequency", start_index=52, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_battery_unit_number", start_index=58, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_battery_voltage_per_unit", start_index=62, length=5, data_type="float")
        ]
    )