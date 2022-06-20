import pandas as pd

def read_excel_file_content_into_pd_dataframe(path):
    file_content_df = pd.read_excel(
        io=path, 
        header=0,
    )
    return file_content_df

def filter_participants_for_complete_data(
    df,
    faces_available = True,
    words_available = True
):
    if faces_available:
        df = df[~df['start_exp1:1'].isnull()]
    if words_available:
        df = df[~df['start_exp2:1'].isnull()]
    return df

def get_participant_information_list(df, filetype = 'encoding'):
    participant_information_list = []
    for index, row in df.iterrows():
        info_obj = {
                'identifier': row['participant'],
                str('file_'+filetype+'_faces'): row['start_exp1:1'],
                str('file_'+filetype+'_words'): row['start_exp2:1']
        }
        participant_information_list.append(info_obj)
    return participant_information_list