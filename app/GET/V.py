from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

V = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="V",
        cmd="V?",
        reply_max_length=6, reply_min_length=5,
        start_with_regex="\\(V|\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="rating_volt", start_index=0, length=3, data_type="integer")
        ]
    )