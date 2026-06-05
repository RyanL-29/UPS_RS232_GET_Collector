from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

SASV07 = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="SASV07",
        cmd="SASV07?",
        reply_max_length=30, reply_min_length=7,
        start_with_regex="GASV07D",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="serial_number", start_index=0, length=20, data_type="string")
        ]
    )