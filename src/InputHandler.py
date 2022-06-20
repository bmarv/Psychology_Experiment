import os
from pathlib import Path

from tkinter import *
from tkinter import filedialog

from src import FileInput

def ask_directory():
    Tk().withdraw()
    folder_path = Path(filedialog.askdirectory())
    return folder_path

def get_directory_content():
    folder_path = ask_directory()
    return os.listdir(folder_path)
 
def get_participants_experiment_path_list(basepath, filetype = 'encoding'):
    experiment_folder = os.path.join(
        basepath,
        'experiment_data'
    )
    experiment_info_file = os.path.join(
        basepath,
        'data.xlsx'
    )
    info_df = FileInput.read_excel_file_content_into_pd_dataframe(experiment_info_file)
    info_df = FileInput.filter_participants_for_complete_data(
        df = info_df, 
        faces_available = True, 
        words_available = True
    )
    encoding_file_names_list = FileInput.get_participant_information_list(
        df = info_df,
        filetype = filetype
    )
    path_list = []
    for participant in encoding_file_names_list:
        info_obj = {
            'identifier': participant['identifier'],
            'vp_nr': participant['vp_nr'],
            str('path_'+filetype+'_faces'): os.path.join(
                experiment_folder,
                participant[str('file_'+filetype+'_faces')]
            ),
            str('path_'+filetype+'_words'): os.path.join(
                experiment_folder,
                participant[str('file_'+filetype+'_words')]
            )
        }
        path_list.append(info_obj)
    return path_list

def read_data_for_participant(path_list, filetype ='encoding'):
    data_list = []
    for participant in path_list:
        if filetype == 'encoding':
            data_obj = {
                'identifier': participant['identifier'],
                'vp_nr': participant['vp_nr'],
                'df_faces': FileInput.read_encoding_data_txt_into_df(participant['path_encoding_faces']),
                'df_words': FileInput.read_encoding_data_txt_into_df(participant['path_encoding_words'])
            }
        elif filetype == 'memory':
            data_obj = {
                'identifier': participant['identifier'],
                'vp_nr': participant['vp_nr'],
                'df_faces': FileInput.read_memory_data_txt_into_df(participant['path_memory_faces']),
                'df_words': FileInput.read_memory_data_txt_into_df(participant['path_memory_words'])
            }
        else:
            data_obj = {}
            print('filetype not supported')
        data_list.append(data_obj)
    return data_list

def encoding_workflow():
    basepath = ask_directory()
    encoding_path_list = get_participants_experiment_path_list(basepath, 'encoding')
    encoding_data_list = read_data_for_participant(encoding_path_list, 'encoding')
    return encoding_data_list

def memory_workflow():
    basepath = ask_directory()
    memory_path_list = get_participants_experiment_path_list(basepath, 'memory')
    memory_data_list = read_data_for_participant(memory_path_list, 'memory')
    return memory_data_list