from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

IP = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="IP",
        cmd="IP?",
        reply_max_length=4, reply_min_length=4,
        start_with_regex="IP",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="input_range_type", start_index=0, length=1, data_type="string")
        ]   
    )