from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

FUNC = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="FUNC",
        cmd="FUNC?",
        reply_max_length=10, reply_min_length=10,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="function_params", start_index=0, length=8, data_type="string")
        ]   
    )

#  [int(bit) for byte in bytes.fromhex("00000039") for bit in f"{byte:08b}"]
#  [
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      0, 
#      1, 
#      1, 
#      1, 
#      0, 
#      0, 
#      1  # High Efficiency Mode
#         ]
