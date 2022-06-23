from src import InputHandler
from src import TableBuilder
from src import FileExporter

def run_build_encoding_table(output_format = 'csv'):
    stimulus_object = InputHandler.stimulus_lists_workflow()
    df_table = run_build_encoding_table_dfs(stimulus_object)
    if output_format == 'excel':
        FileExporter.write_dataframe_to_excel(df_table, 'encoding', 'encoding_data.xlsx')
    else:
        FileExporter.write_dataframe_to_csv(df_table, 'encoding', 'encoding_data.csv')
    return df_table

def run_build_recognition_table(output_format = 'csv'):
    stimulus_object = InputHandler.stimulus_lists_workflow()
    df_table = run_build_recognition_table_dfs(stimulus_object)
    if output_format == 'excel':
        FileExporter.write_dataframe_to_excel(df_table, 'recognition', 'recognition_data.xlsx')
    else:
        FileExporter.write_dataframe_to_csv(df_table, 'recognition', 'recognition_data.csv')
    return df_table

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
    
    # build one encoding table for each participant
    participants_df_list = []
    for participant in list(participants_table_dict.keys()):
        table_df_list = list(participants_table_dict[participant].values())
        participants_df_list.append(TableBuilder.concat_df_tables_from_df_list(table_df_list))
    # build one encoding table for all participants
    encoding_df = TableBuilder.concat_df_tables_from_df_list(participants_df_list)
    return encoding_df

def run_build_recognition_table_dfs(stimulus_object):
    recognition_data_a_list = InputHandler.memory_workflow()
    recognition_data_b_list = InputHandler.memory_workflow()
    recognition_stimulus_a_obj = {}
    recognition_faces_a_obj = {}
    recognition_words_a_obj = {}
    # distinct data dicts for each encoding category
    for el in recognition_data_a_list:
        recognition_stimulus_a_obj[el['vp_nr']] = el['stimulation']
        recognition_faces_a_obj[el['vp_nr']] = el['df_faces']
        recognition_words_a_obj[el['vp_nr']] = el['df_words']
    recognition_stimulus_b_obj = {}
    recognition_faces_b_obj = {}
    recognition_words_b_obj = {}
    for el in recognition_data_b_list:
        recognition_stimulus_b_obj[el['vp_nr']] = el['stimulation']
        recognition_faces_b_obj[el['vp_nr']] = el['df_faces']
        recognition_words_b_obj[el['vp_nr']] = el['df_words']
    
    participants_table_dict = {}
    # creating tables for every participant, clustering each participant into one table
    for faces_a in list(recognition_faces_a_obj.keys()):
        stimulus_a, stimulus_b, recognition_faces_a, recognition_faces_b, recognition_words_a, recognition_words_b = None, None, None, None, None, None
        vp_nr = faces_a
        stimulus_a = recognition_stimulus_a_obj[vp_nr]
        recognition_faces_a = recognition_faces_a_obj[vp_nr]
        if vp_nr in list(recognition_faces_b_obj.keys()):
            stimulus_b = recognition_stimulus_b_obj[vp_nr]
            recognition_faces_b = recognition_faces_b_obj[vp_nr]
            recognition_faces_b_obj.pop(vp_nr)
        if vp_nr in list(recognition_words_a_obj.keys()):
            stimulus_a = recognition_stimulus_a_obj[vp_nr]
            recognition_words_a = recognition_words_a_obj[vp_nr]
            recognition_words_a_obj.pop(vp_nr)
        if vp_nr in list(recognition_words_b_obj.keys()):
            stimulus_b = recognition_stimulus_b_obj[vp_nr]
            recognition_words_b = recognition_words_b_obj[vp_nr]
            recognition_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_recognition_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            recognition_faces_a = recognition_faces_a,
            recognition_faces_b = recognition_faces_b,
            recognition_words_a = recognition_words_a,
            recognition_words_b = recognition_words_b,
        )

    # tables for participants, that weren't in faces_a
    for faces_b in list(recognition_faces_b_obj.keys()):
        stimulus_a, stimulus_b, recognition_faces_b, recognition_words_a, recognition_words_b = None, None, None, None, None
        vp_nr = faces_b
        stimulus_b = recognition_stimulus_b_obj[vp_nr]
        recognition_faces_b = recognition_faces_b_obj[vp_nr]
        recognition_faces_b_obj.pop(vp_nr)
        if vp_nr in list(recognition_words_a_obj.keys()):
            stimulus_a = recognition_stimulus_a_obj[vp_nr]
            recognition_words_a = recognition_words_a_obj[vp_nr]
            recognition_words_a_obj.pop(vp_nr)
        if vp_nr in list(recognition_words_b_obj.keys()):
            stimulus_b = recognition_stimulus_b_obj[vp_nr]
            recognition_words_b = recognition_words_b_obj[vp_nr]
            recognition_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_recognition_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            recognition_faces_a = None,
            recognition_faces_b = recognition_faces_b,
            recognition_words_a = recognition_words_a,
            recognition_words_b = recognition_words_b,
        )
    # tables for participants, that weren't in faces_a or faces_b
    for words_a in list(recognition_words_a_obj.keys()):
        stimulus_a, stimulus_b, recognition_words_a, recognition_words_b = None, None, None, None
        recognition_words_a = recognition_words_a_obj[vp_nr]
        vp_nr = words_a
        stimulus_a = recognition_stimulus_a_obj[vp_nr]
        if vp_nr in list(recognition_words_b_obj.keys()):
            stimulus_b = recognition_stimulus_b_obj[vp_nr]
            recognition_words_b = recognition_words_b_obj[vp_nr]
            recognition_words_b_obj.pop(vp_nr)
        participants_table_dict[vp_nr] = TableBuilder.build_recognition_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = vp_nr,
            stimulus_a = stimulus_a,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            recognition_faces_a = None,
            recognition_faces_b = None,
            recognition_words_a = recognition_words_a,
            recognition_words_b = recognition_words_b,
        )
    # tables for participants, that weren't in faces_a, faces_b or words_a
    for words_b in list(recognition_words_b_obj.keys()):
        stimulus_b, recognition_words_b = None, None
        recognition_words_b = recognition_words_b_obj[vp_nr]
        vp_nr = words_b
        stimulus_b = recognition_stimulus_b_obj[vp_nr]
        participants_table_dict[vp_nr] = TableBuilder.build_recognition_table_for_participant(
            stimulus_object = stimulus_object,
            vp_nr_a = None,
            stimulus_a = None,
            vp_nr_b = vp_nr,
            stimulus_b = stimulus_b,
            recognition_faces_a = None,
            recognition_faces_b = None,
            recognition_words_a = None,
            recognition_words_b = recognition_words_b,
        )
    
    # build one encoding table for each participant
    participants_df_list = []
    for participant in list(participants_table_dict.keys()):
        table_df_list = list(participants_table_dict[participant].values())
        participants_df_list.append(TableBuilder.concat_df_tables_from_df_list(table_df_list))
    # build one encoding table for all participants
    recognition_df = TableBuilder.concat_df_tables_from_df_list(participants_df_list)
    return recognition_df
