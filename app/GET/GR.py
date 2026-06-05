from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

GR = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="GR",
        cmd="GR?",
        reply_max_length=4, reply_min_length=4,
        start_with_regex="GR",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="enable_green_function", start_index=0, length=1, data_type="integer")
        ]   
    )