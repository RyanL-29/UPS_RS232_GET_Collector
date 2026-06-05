from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

SD = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="SD",
        cmd="SD?",
        reply_max_length=4, reply_min_length=4,
        start_with_regex="SD",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="enable_long_time_discharged", start_index=0, length=1, data_type="integer")
        ]
    )