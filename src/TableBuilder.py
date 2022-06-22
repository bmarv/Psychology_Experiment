import pandas as pd
import numpy as np

# TODO: build recognition table for participant
# TODO: build whole table in right order

def build_encoding_table_for_participant(
    stimulus_object, 
    vp_nr_a = None,
    vp_nr_b = None,
    encoding_faces_a = None, 
    encoding_faces_b = None, 
    encoding_words_a = None, 
    encoding_words_b = None
):
    participant_encoding_table_obj = {}
    if encoding_faces_a is not None:
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr) + '_encoding_faces_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, encoding_faces_a, stimulus_object['df_encoding_faces_a'])
        print('faces a finished')
    if encoding_faces_b is not None:
        vp_nr = vp_nr_b
        encoding_task =  str(vp_nr) + '_encoding_faces_b'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, encoding_faces_b, stimulus_object['df_encoding_faces_b'])
        print('faces b finished')
    if encoding_words_a is not None:
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr)  + '_encoding_words_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_words_table_from_df(vp_nr, encoding_words_a, stimulus_object['df_encoding_words_a'])
        print('words a finished')
    if encoding_words_b is not None:
        vp_nr = vp_nr_b
        encoding_task =  str(vp_nr)  + '_encoding_words_b'
        participant_encoding_table_obj[encoding_task] = build_encoding_words_table_from_df(vp_nr, encoding_words_b, stimulus_object['df_encoding_words_b'])
        print('words b finished')
    return participant_encoding_table_obj

def build_encoding_faces_table_from_df(vp_nr, encoding_faces_df, df_stimulus_encoding_faces):
    encoding_faces_df['VP'] = int(vp_nr)
    encoding_faces_df['Stimulation'] = encoding_faces_df.apply(lambda row: row.order + 1, axis = 1)
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

def build_encoding_words_table_from_df(vp_nr, encoding_words_df, df_stimulus_encoding_words):
    encoding_words_df['VP'] = int(vp_nr)
    encoding_words_df['Stimulation'] = encoding_words_df.apply(lambda row: row.order + 1, axis = 1)
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