import pandas as pd
import numpy as np

# TODO: build recognition table for participant

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
    if (encoding_faces_a is not None) and (isinstance(encoding_faces_a, pd.DataFrame)):
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr) + '_encoding_faces_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, stimulus_a, encoding_faces_a, stimulus_object['df_encoding_faces_a'])
    if (encoding_faces_b is not None) and (isinstance(encoding_faces_b, pd.DataFrame)):
        vp_nr = vp_nr_b
        encoding_task =  str(vp_nr) + '_encoding_faces_b'
        participant_encoding_table_obj[encoding_task] = build_encoding_faces_table_from_df(vp_nr, stimulus_b, encoding_faces_b, stimulus_object['df_encoding_faces_b'])
    if (encoding_words_a is not None) and (isinstance(encoding_words_a, pd.DataFrame)):
        vp_nr = vp_nr_a
        encoding_task =  str(vp_nr)  + '_encoding_words_a'
        participant_encoding_table_obj[encoding_task] = build_encoding_words_table_from_df(vp_nr, stimulus_a, encoding_words_a, stimulus_object['df_encoding_words_a'])
    if (encoding_words_b is not None) and (isinstance(encoding_words_b, pd.DataFrame)):
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

def build_recognition_table_for_participant(
    stimulus_object, 
    vp_nr_a = None,
    stimulus_a = None,
    vp_nr_b = None,
    stimulus_b = None,
    recognition_faces_a = None, 
    recognition_faces_b = None, 
    recognition_words_a = None, 
    recognition_words_b = None
):
    participant_recognition_table_obj = {}
    if (recognition_faces_a is not None) and (isinstance(recognition_faces_a, pd.DataFrame)):
        vp_nr = vp_nr_a
        recognition_task =  str(vp_nr) + '_recognition_faces_a'
        participant_recognition_table_obj[recognition_task] = build_recognition_faces_table_from_df(
            vp_nr = vp_nr, 
            a_or_b ='A', 
            stimulus = stimulus_a, 
            recognition_faces_df = recognition_faces_a, 
            df_stimulus_recognition_faces = stimulus_object['df_recognition_faces_a']
        )
    if (recognition_faces_b is not None) and (isinstance(recognition_faces_b, pd.DataFrame)):
        vp_nr = vp_nr_b
        recognition_task =  str(vp_nr) + '_recognition_faces_b'
        participant_recognition_table_obj[recognition_task] = build_recognition_faces_table_from_df(
            vp_nr = vp_nr, 
            a_or_b ='B', 
            stimulus = stimulus_b, 
            recognition_faces_df = recognition_faces_b, 
            df_stimulus_recognition_faces = stimulus_object['df_recognition_faces_b']
        )
    if (recognition_words_a is not None) and (isinstance(recognition_words_a, pd.DataFrame)):
        vp_nr = vp_nr_a
        recognition_task =  str(vp_nr)  + '_recognition_words_a'
        participant_recognition_table_obj[recognition_task] = build_recognition_words_table_from_df(
            vp_nr = vp_nr, 
            a_or_b ='A', 
            stimulus = stimulus_a, 
            recognition_words_df = recognition_words_a, 
            df_stimulus_recognition_words = stimulus_object['df_recognition_words_a']
        )
    if (recognition_words_b is not None) and (isinstance(recognition_words_b, pd.DataFrame)):
        vp_nr = vp_nr_b
        recognition_task =  str(vp_nr)  + '_recognition_words_b'
        participant_recognition_table_obj[recognition_task] = build_recognition_words_table_from_df(
            vp_nr = vp_nr, 
            a_or_b ='B', 
            stimulus = stimulus_b, 
            recognition_words_df = recognition_words_b, 
            df_stimulus_recognition_words = stimulus_object['df_recognition_words_b']
        )
    return participant_recognition_table_obj

def build_recognition_faces_table_from_df(vp_nr, a_or_b, stimulus, recognition_faces_df, df_stimulus_recognition_faces):
    recognition_faces_df['VP'] = int(vp_nr)
    recognition_faces_df['Stimulation'] = int(stimulus)
    recognition_faces_df = recognition_faces_df.rename(columns={
        'task': 'Aufgabe',
        'orderrec': 'Antwort_Order',
        'yes_or_no': 'Antwort',
        'confidence': 'Sicherheit'
    })
    recognition_faces_df['A_B'] = a_or_b
    recognition_faces_df['Stimulus'] = recognition_faces_df.apply(lambda row: df_stimulus_recognition_faces.iloc[row.tablerow - 1]['name'], axis = 1)
    recognition_faces_df = recognition_faces_df[[
        'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT', 'Sicherheit'
    ]]
    return recognition_faces_df

def build_recognition_words_table_from_df(vp_nr, a_or_b, stimulus, recognition_words_df, df_stimulus_recognition_words):
    recognition_words_df['VP'] = int(vp_nr)
    recognition_words_df['Stimulation'] = int(stimulus)
    recognition_words_df = recognition_words_df.rename(columns={
        'task': 'Aufgabe',
        'orderrec': 'Antwort_Order',
        'yes_or_no': 'Antwort',
        'confidence': 'Sicherheit'
    })
    recognition_words_df['A_B'] = a_or_b
    recognition_words_df['Stimulus'] = recognition_words_df.apply(lambda row: df_stimulus_recognition_words.iloc[row.tablerow - 1]['name'], axis = 1)
    recognition_words_df = recognition_words_df[[
        'VP', 'Stimulation', 'Aufgabe', 'A_B', 'Stimulus', 'Antwort_Order', 'Antwort', 'RT', 'Sicherheit'
    ]]
    return recognition_words_df

def concat_df_tables_from_df_list(df_list):
    if len(df_list) == 0:
        return pd.DataFrame()
    concat_df_table = pd.concat(df_list, axis=0)
    return concat_df_table