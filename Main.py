from src import InputHandler
from src import TableBuilder

def run_build_encoding_table_dfs(stimulus_object):
    
    encoding_data_a_list = InputHandler.encoding_workflow()
    encoding_data_b_list = InputHandler.encoding_workflow()
    encoding_stimulus_a_obj = {}
    encoding_faces_a_obj = {}
    encoding_words_a_obj = {}
    # distinct data dicts for each encoding category
    for el in encoding_data_a_list:
        encoding_stimulus_a_obj[el['vp_nr']] = el['stimulation']
        encoding_faces_a_obj[el['vp_nr']] = el['df_faces']
        encoding_words_a_obj[el['vp_nr']] = el['df_words']
    encoding_stimulus_b_obj = {}
    encoding_faces_b_obj = {}
    encoding_words_b_obj = {}
    for el in encoding_data_b_list:
        encoding_stimulus_b_obj[el['vp_nr']] = el['stimulation']
        encoding_faces_b_obj[el['vp_nr']] = el['df_faces']
        encoding_words_b_obj[el['vp_nr']] = el['df_words']
    

    participants_table_dict = {}
    # creating tables for every participant, clustering each participant into one table
    for faces_a in list(encoding_faces_a_obj.keys()):
        stimulus_a, stimulus_b, encoding_faces_a, encoding_faces_b, encoding_words_a, encoding_words_b = None, None, None, None, None, None
        vp_nr = faces_a
        stimulus_a = encoding_stimulus_a_obj[vp_nr]
        encoding_faces_a = encoding_faces_a_obj[vp_nr]
        if vp_nr in list(encoding_faces_b_obj.keys()):
            stimulus_b = encoding_stimulus_b_obj[vp_nr]
            encoding_faces_b = encoding_faces_b_obj[vp_nr]
            encoding_faces_b_obj.pop(vp_nr)
        if vp_nr in list(encoding_words_a_obj.keys()):
            stimulus_a = encoding_stimulus_a_obj[vp_nr]
            encoding_words_a = encoding_words_a_obj[vp_nr]
            encoding_words_a_obj.pop(vp_nr)
        if vp_nr in list(encoding_words_b_obj.keys()):
            stimulus_b = encoding_stimulus_b_obj[vp_nr]
            encoding_words_b = encoding_words_b_obj[vp_nr]
            encoding_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_encoding_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            encoding_faces_a = encoding_faces_a,
            encoding_faces_b = encoding_faces_b,
            encoding_words_a = encoding_words_a,
            encoding_words_b = encoding_words_b,
        )

    # tables for participants, that weren't in faces_a
    for faces_b in list(encoding_faces_b_obj.keys()):
        stimulus_a, stimulus_b, encoding_faces_b, encoding_words_a, encoding_words_b = None, None, None, None, None
        vp_nr = faces_b
        stimulus_b = encoding_stimulus_b_obj[vp_nr]
        encoding_faces_b = encoding_faces_b_obj[vp_nr]
        encoding_faces_b_obj.pop(vp_nr)
        if vp_nr in list(encoding_words_a_obj.keys()):
            stimulus_a = encoding_stimulus_a_obj[vp_nr]
            encoding_words_a = encoding_words_a_obj[vp_nr]
            encoding_words_a_obj.pop(vp_nr)
        if vp_nr in list(encoding_words_b_obj.keys()):
            stimulus_b = encoding_stimulus_b_obj[vp_nr]
            encoding_words_b = encoding_words_b_obj[vp_nr]
            encoding_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_encoding_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            encoding_faces_a = None,
            encoding_faces_b = encoding_faces_b,
            encoding_words_a = encoding_words_a,
            encoding_words_b = encoding_words_b,
        )
    # tables for participants, that weren't in faces_a or faces_b
    for words_a in list(encoding_words_a_obj.keys()):
        stimulus_a, stimulus_b, encoding_words_a, encoding_words_b = None, None, None, None
        encoding_words_a = encoding_words_a_obj[vp_nr]
        vp_nr = words_a
        stimulus_a = encoding_stimulus_a_obj[vp_nr]
        if vp_nr in list(encoding_words_b_obj.keys()):
            stimulus_b = encoding_stimulus_b_obj[vp_nr]
            encoding_words_b = encoding_words_b_obj[vp_nr]
            encoding_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_encoding_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            encoding_faces_a = None,
            encoding_faces_b = None,
            encoding_words_a = encoding_words_a,
            encoding_words_b = encoding_words_b,
        )
    # tables for participants, that weren't in faces_a, faces_b or words_a
    for words_b in list(encoding_words_b_obj.keys()):
        stimulus_b, encoding_words_b = None, None
        encoding_words_b = encoding_words_b_obj[vp_nr]
        vp_nr = words_b
        stimulus_b = encoding_stimulus_b_obj[vp_nr]
        participants_table_dict[vp_nr] = TableBuilder.build_encoding_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = None,
            stimulus_a = None,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            encoding_faces_a = None,
            encoding_faces_b = None,
            encoding_words_a = None,
            encoding_words_b = encoding_words_b,
        )
    return participants_table_dict

# TODO: build recognition table
def run_build_recognition_table_dfs(stimulus_object):
    pass

def run_build_table_dfs():
    stimulus_object = InputHandler.stimulus_lists_workflow()
    df_table = run_build_encoding_table_dfs(stimulus_object)
    return df_table
