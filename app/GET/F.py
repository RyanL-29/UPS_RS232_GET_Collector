from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

F = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="F",
        cmd="F",
        reply_max_length=23, reply_min_length=22,
        start_with_regex="\\(#|#",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="rating_voltage", start_index=0, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_current", start_index=6, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_battery_voltage", start_index=10, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="rating_frequency", start_index=16, length=4, data_type="float")
        ]   
    )