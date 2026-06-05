from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

TD = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="TD",
        cmd="TD?",
        reply_max_length=4, reply_min_length=4,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="auto_test_period_day", start_index=0, length=2, data_type="integer")
        ]
    )