from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

SL = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="SL",
        cmd="SL?",
        reply_max_length=9, reply_min_length=9,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="phase_lock_high_limit_in_percent", start_index=0, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="phase_lock_low_limit_in_percent", start_index=4, length=3, data_type="integer")
        ]
    )