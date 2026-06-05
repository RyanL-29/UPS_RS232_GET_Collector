from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

QOF = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="QOF",
        cmd="QOF",
        reply_max_length=6, reply_min_length=6,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="output_frequency", start_index=0, length=4, data_type="float")
        ]
    )