from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

WA = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="WA",
        cmd="WA",
        reply_max_length=82, reply_min_length=80,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="load_watt_1", start_index=0, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_watt_2", start_index=6, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_watt_3", start_index=12, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_va_1", start_index=18, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_va_2", start_index=24, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_va_3", start_index=30, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_total_va", start_index=36, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_current_1", start_index=42, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_current_2", start_index=48, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_current_3", start_index=54, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_percent", start_index=66, length=5, data_type="float"),
        ]
    )