from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

TC = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="TC",
        cmd="TC?",
        reply_max_length=7, reply_min_length=7,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="battery_temperature", start_index=0, length=5, data_type="float")
        ]
    )