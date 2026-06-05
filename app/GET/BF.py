from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

BF = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="BF",
        cmd="BF?",
        reply_max_length=3, reply_min_length=3,
        start_with_regex="\\(",
        parse_rules=[UPSNMC_Reply_Data_Parse_Rules(
            key="enable_auto_test",
            start_index=0, length=1, data_type="integer"
        )]
    )