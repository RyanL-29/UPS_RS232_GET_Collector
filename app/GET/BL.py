from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

BL = UPSNMC_Data_Fetching_Info(
        calculated_field="{{ input }} * 0.01",
        calculated_fetcher=False,
        key="BL",
        cmd="BL?",
        reply_max_length=4, reply_min_length=4,
        start_with_regex="",
        parse_rules=[UPSNMC_Reply_Data_Parse_Rules(
            key="battery_capacity",
            start_index=0, length=3, data_type="integer"
        )]
    )