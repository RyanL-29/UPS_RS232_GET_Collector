from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

SF = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="SF",
        cmd="SF?",
        reply_max_length=9, reply_min_length=9,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="input_frequency_high_limit_in_percent", start_index=0, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="input_frequency_low_limit_in_percent", start_index=4, length=3, data_type="integer")
        ]
    )