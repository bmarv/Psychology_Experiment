from src import InputHandler
from src import TableBuilder

def run_build_encoding_table_dfs(stimulus_object):
    
    encoding_data_a_list = InputHandler.encoding_workflow()
    encoding_data_b_list = InputHandler.encoding_workflow()
    # TODO: make table for every participant
    df_table_participant = TableBuilder.build_encoding_table_for_participant(stimulus_object, encoding_data_a_list[0], encoding_data_b_list[0])
    return df_table_participant


def run_build_table_dfs():
    stimulus_object = InputHandler.stimulus_lists_workflow()
    df_table = run_build_encoding_table_dfs(stimulus_object)
    return df_table
