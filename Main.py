from src import InputHandler
from src import TableBuilder

def run_build_encoding_table_dfs(stimulus_object):
    
    encoding_data_a_list = InputHandler.encoding_workflow()
    encoding_data_b_list = InputHandler.encoding_workflow()
    # TODO: make table for every participant
    df_table_participant = TableBuilder.build_encoding_table_for_participant(
        stimulus_object = stimulus_object,
        vp_nr_a = encoding_data_a_list[0]['vp_nr'],
        vp_nr_b = encoding_data_b_list[0]['vp_nr'],
        encoding_faces_a = encoding_data_a_list[0]['df_faces'],
        encoding_faces_b = encoding_data_b_list[0]['df_faces'],
        encoding_words_a = encoding_data_a_list[0]['df_words'],
        encoding_words_b = encoding_data_b_list[0]['df_words'],
        )
    return df_table_participant


def run_build_table_dfs():
    stimulus_object = InputHandler.stimulus_lists_workflow()
    df_table = run_build_encoding_table_dfs(stimulus_object)
    return df_table
