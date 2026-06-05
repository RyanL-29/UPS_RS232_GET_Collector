from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

BPS = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="BPS",
        cmd="BPS",
        reply_max_length=26, reply_min_length=24,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="bypass_volt_1", start_index=0, length=5, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="bypass_volt_2", start_index=7, length=5, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="bypass_volt_3", start_index=13, length=5, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="bypass_freq", start_index=19, length=4, data_type="integer"),
        ]   
    )