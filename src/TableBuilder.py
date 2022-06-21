import pandas as pd
import numpy as np

# TODO: build recognition table for participant
# TODO: build whole table in right order

def build_encoding_table_for_participant(stimulus_object, encoding_data_obj_a, encoding_data_obj_b):
    # stimulus-lists a and b for encoding
    df_stimulus_encoding_faces_a = stimulus_object['df_encoding_faces_a']
    df_stimulus_encoding_faces_b = stimulus_object['df_encoding_faces_b']
    df_stimulus_encoding_words_a = stimulus_object['df_encoding_words_a']
    df_stimulus_encoding_words_b = stimulus_object['df_encoding_words_b']
    
    # TODO: implement for words also
    # index 0: A, 1:B
    # TODO: implement index 1:B
    # TODO: make as generic as possible
    for index in range(0,2):
        if index == 0:
            vp_nr = encoding_data_obj_a['vp_nr']
            df_encoding_faces_a = encoding_data_obj_a['df_faces']
            df_encoding_faces_a['VP'] = vp_nr
            df_encoding_faces_a['Stimulation'] = df_encoding_faces_a.apply(lambda row: row.order + 1, axis = 1)
            df_encoding_faces_a = df_encoding_faces_a.rename(columns={
                'task': 'Aufgabe',
                'valence': 'Antwort'
            })
            df_encoding_faces_a['A_B'] = df_encoding_faces_a.apply(lambda row: 'A' if (row.order == 0) else 'B', axis = 1)
            df_encoding_faces_a['Stimulus'] = df_encoding_faces_a.apply(lambda row: df_stimulus_encoding_faces_a.iloc[row.tablerow - 1]['name'], axis = 1)
            df_encoding_faces_a['Antwort_Order'] = np.nan
            df_encoding_faces_a = df_encoding_faces_a[[
                'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT'
            ]]
            return vp_nr, df_encoding_faces_a
    # TODO: return all 4 df