from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

BT = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="BT",
        cmd="BT?",
        reply_max_length=7, reply_min_length=7,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="battery_remain_time_second", start_index=0, length=5, data_type="integer")
        ]   
    )