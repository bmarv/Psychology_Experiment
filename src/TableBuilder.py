import pandas as pd
import numpy as np

# TODO: build recognition table for participant
# TODO: build whole table in right order

# TODO: test for incomplete Data
def build_encoding_table_for_participant(
    stimulus_object, 
    vp_nr_a = None,
    stimulus_a = None,
    vp_nr_b = None,
    stimulus_b = None,
    encoding_faces_a = None, 
    encoding_faces_b = None, 
    encoding_words_a = None, 
    encoding_words_b = None
):
    participant_encoding_table_obj = {}
    if encoding_faces_a is not None:
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr) + '_encoding_faces_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, stimulus_a, encoding_faces_a, stimulus_object['df_encoding_faces_a'])
    if encoding_faces_b is not None:
        vp_nr = vp_nr_b
        encoding_task =  str(vp_nr) + '_encoding_faces_b'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, stimulus_b, encoding_faces_b, stimulus_object['df_encoding_faces_b'])
    if encoding_words_a is not None:
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr)  + '_encoding_words_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_words_table_from_df(vp_nr, stimulus_a, encoding_words_a, stimulus_object['df_encoding_words_a'])
    if encoding_words_b is not None:
        vp_nr = vp_nr_b
        encoding_task =  str(vp_nr)  + '_encoding_words_b'
        participant_encoding_table_obj[encoding_task] = build_encoding_words_table_from_df(vp_nr, stimulus_b, encoding_words_b, stimulus_object['df_encoding_words_b'])
    return participant_encoding_table_obj

def build_encoding_faces_table_from_df(vp_nr, stimulus, encoding_faces_df, df_stimulus_encoding_faces):
    encoding_faces_df['VP'] = int(vp_nr)
    encoding_faces_df['Stimulation'] = int(stimulus)
    encoding_faces_df = encoding_faces_df.rename(columns={
        'task': 'Aufgabe',
        'valence': 'Antwort'
    })
    encoding_faces_df['A_B'] = encoding_faces_df.apply(lambda row: 'A' if (row.order == 0) else 'B', axis = 1)
    encoding_faces_df['Stimulus'] = encoding_faces_df.apply(lambda row: df_stimulus_encoding_faces.iloc[row.tablerow - 1]['name'], axis = 1)
    encoding_faces_df['Antwort_Order'] = np.nan
    encoding_faces_df = encoding_faces_df[[
        'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT'
    ]]
    return encoding_faces_df

def build_encoding_words_table_from_df(vp_nr, stimulus, encoding_words_df, df_stimulus_encoding_words):
    encoding_words_df['VP'] = int(vp_nr)
    encoding_words_df['Stimulation'] = int(stimulus)
    encoding_words_df = encoding_words_df.rename(columns={
        'task': 'Aufgabe',
        'valence': 'Antwort'
    })
    encoding_words_df['A_B'] = encoding_words_df.apply(lambda row: 'A' if (row.order == 0) else 'B', axis = 1)
    encoding_words_df['Stimulus'] = encoding_words_df.apply(lambda row: df_stimulus_encoding_words.iloc[row.tablerow - 1]['name'], axis = 1)
    encoding_words_df['Antwort_Order'] = np.nan
    encoding_words_df = encoding_words_df[[
        'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT'
    ]]
    return encoding_words_df

def concat_df_tables_from_df_list(df_list):
    concat_df_table = pd.concat(df_list, axis=0)
    return concat_df_table