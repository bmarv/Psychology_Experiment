import pandas as pd
import numpy as np

# TODO: build recognition table for participant
# TODO: build whole table in right order

def build_encoding_table_for_participant(stimulus_object, encoding_data_obj_a, encoding_data_obj_b):    
    # index 0,1: faces a,b; index 2,3: words a,b;
    # a for even indices, b for odd indices
    df_stimulus_encoding_list = [
        stimulus_object['df_encoding_faces_a'],
        stimulus_object['df_encoding_faces_b'],
        stimulus_object['df_encoding_words_a'],
        stimulus_object['df_encoding_words_b']
    ]

    participant_encoding_table_obj = {}
    for index in range(0,4):
        # encoding_data_obj for a, if index is even; b if index is odd
        if index%2:
            encoding_data_obj = encoding_data_obj_b
            vp_nr = encoding_data_obj['vp_nr']
            encoding_task = str(vp_nr) + '_b'
        else:
            encoding_data_obj = encoding_data_obj_a
            vp_nr = encoding_data_obj['vp_nr']
            encoding_task = str(vp_nr) + '_a'
        # encoding element for faces for index 0,1; for words for index 2,3
        if index < 2:
            encoding_task += '_encoding_faces'
            df_encoding_element = encoding_data_obj['df_faces']
        else:
            encoding_task += '_encoding_words'
            df_encoding_element = encoding_data_obj['df_words']
        df_encoding_element['VP'] = vp_nr
        df_encoding_element['Stimulation'] = df_encoding_element.apply(lambda row: row.order + 1, axis = 1)
        df_encoding_element = df_encoding_element.rename(columns={
            'task': 'Aufgabe',
            'valence': 'Antwort'
        })
        df_encoding_element['A_B'] = df_encoding_element.apply(lambda row: 'A' if (row.order == 0) else 'B', axis = 1)
        df_encoding_element['Stimulus'] = df_encoding_element.apply(lambda row: df_stimulus_encoding_list[index].iloc[row.tablerow - 1]['name'], axis = 1)
        df_encoding_element['Antwort_Order'] = np.nan
        df_encoding_element = df_encoding_element[[
            'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT'
        ]]
        participant_encoding_table_obj[encoding_task] = df_encoding_element
    return participant_encoding_table_obj