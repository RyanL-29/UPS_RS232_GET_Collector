from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

WC = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="WC",
        cmd="WC",
        reply_max_length=11, reply_min_length=11,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="load_total_watt", start_index=0, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_total_va", start_index=5, length=4, data_type="float")
        ]
    )