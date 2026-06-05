from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

RT = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="RT",
        cmd="RT",
        reply_max_length=80, reply_min_length=74,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="firmware_version", start_index=0, length=5, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="model", start_index=12, length=30, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="source_number", start_index=43, length=3, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="phase_number", start_index=47, length=3, data_type="string"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_volt", start_index=51, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_frequency", start_index=55, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_battery_unit_number", start_index=61, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_battery_voltage_per_unit", start_index=65, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="ups_module_number", start_index=70, length=2, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_va", start_index=73, length=5, data_type="integer"),
        ]
    )