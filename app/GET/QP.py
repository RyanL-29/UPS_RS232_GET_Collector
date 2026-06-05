from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

QP = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="QP",
        cmd="QP",
        reply_max_length=31, reply_min_length=27,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="qp_parameters", start_index=18, length=52, data_type="string")
        ]
    )