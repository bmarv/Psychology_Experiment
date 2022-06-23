import pandas as pd

def read_excel_file_content_into_pd_dataframe(path):
    file_content_df = pd.read_excel(
        io=path, 
        header=0,
    )
    return file_content_df

def filter_participants_for_complete_data(
    df,
    faces_neccessary = False,
    words_neccessary = False
):
    df = df[~df['VP_NR:1'].isnull()]
    if faces_neccessary:
        df = df[~df['start_exp1:1'].isnull()]
    if words_neccessary:
        df = df[~df['start_exp2:1'].isnull()]
    return df

def get_participant_information_list(df, filetype = 'encoding'):
    participant_information_list = []
    for index, row in df.iterrows():
        info_obj = {
                'identifier': row['participant'],
                'vp_nr': row['VP_NR:1'],
                str('file_'+filetype+'_faces'): row['start_exp1:1'],
                str('file_'+filetype+'_words'): row['start_exp2:1']
        }
        if filetype == 'encoding':
            info_obj['stimulation'] = row['Stimulation:1']
        else:
            info_obj['stimulation'] = 0
        participant_information_list.append(info_obj)
    return participant_information_list

def read_encoding_data_txt_into_df(path):
    if path == 'nan':
        return 'nan'
    df = pd.read_csv(
        filepath_or_buffer = path, 
        sep = ' ', 
        header = None, 
        names=['order', 'task', 'tablerow', 'img_column', 'RT', 'valence']
    )
    return df

def read_memory_data_txt_into_df(path):
    if path == 'nan':
        return 'nan'
    df = pd.read_csv(
        filepath_or_buffer = path, 
        sep = ' ', 
        header = None, 
        names=['order', 'orderrec', 'task', 'tablerow', 'RT', 'yes_or_no', 'confidence']
    )
    return df

def read_stimulus_encoding_txt_into_dfs(path):
    df = pd.read_csv(
        filepath_or_buffer = path, 
        engine = 'python',
        sep = r'\t\s*', 
        header = None, 
    )
    df_a = df.iloc[:, 0:2]
    df_b = df.iloc[:, 2:4]
    df_a = df_a.rename(
        columns={
            0: 'name',
            1: 'file'
        }
    )
    df_b = df_b.rename(
        columns={
            2: 'name',
            3: 'file'
        }
    )
    return df_a, df_b

def read_stimulus_recognition_txt_into_df(path):
    df = pd.read_csv(
        filepath_or_buffer = path, 
        engine = 'python',
        sep = r'\t\s*', 
        header = None, 
    )
    df = df.rename(
        columns={
            0: 'name',
            1: 'value1',
            2: 'value2'
        }
    )
    return df