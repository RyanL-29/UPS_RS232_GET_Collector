from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

QF = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="QF",
        cmd="QF",
        reply_max_length=58, reply_min_length=3,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="fault_code", start_index=0, length=2, data_type="string"),
        ]
    )