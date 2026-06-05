from app.schemas.upsnmc import UPSNMC_Data_Fetching_Info, UPSNMC_Reply_Data_Parse_Rules

LSARD = UPSNMC_Data_Fetching_Info(
        calculated_fetcher=False,
        key="LSARD{{ ups_load_socket_group_count }}?",
        cmd="LSARD{{ ups_load_socket_group_count }}?",
        require_socket_group_count=True,
        reply_max_length=10, reply_min_length=10,
        start_with_regex="\\(",
        parse_rules=[
            UPSNMC_Reply_Data_Parse_Rules(key="auto_restart_delay_second_ls_{{ ups_load_socket_group_count }}", start_index=3, length=5, data_type="integer")
        ]   
    )