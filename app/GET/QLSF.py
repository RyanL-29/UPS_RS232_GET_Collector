from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

QLSF = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="QLSF",
        cmd="QLSF?",
        reply_max_length=5, reply_min_length=5,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="ls_supported", start_index=0, length=1, data_type="integer"),
            UPSNMC_Reply_Data_Parse_Rules(key="ls_number", start_index=2, length=1, data_type="integer")
        ]
    )