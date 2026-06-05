from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

Q1 = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="Q1",
        cmd="Q1",
        reply_max_length=47, reply_min_length=47,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="input_voltage_1", start_index=0, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_voltage_1", start_index=12, length=5, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="load_percent", start_index=18, length=3, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="output_frequency", start_index=22, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="battery_voltage_positive", start_index=27, length=4, data_type="float"),
            UPSNMC_Reply_Data_Parse_Rules(key="status_q1", start_index=37, length=8, data_type="string"),
        ]   
    )