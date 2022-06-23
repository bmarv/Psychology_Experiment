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
        faces_neccessary = False, 
        words_neccessary = False
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
        'stimulation': participant['stimulation']
        }
        if str(participant[str('file_'+filetype+'_faces')]) == 'nan':
            info_obj[str('path_'+filetype+'_faces')] = 'nan'
        elif str(participant[str('file_'+filetype+'_faces')]) is not 'nan':
            info_obj[str('path_'+filetype+'_faces')] = os.path.join(
                experiment_folder,
                participant[str('file_'+filetype+'_faces')]
            )
        if str(participant[str('file_'+filetype+'_words')]) == 'nan':
            info_obj[str('path_'+filetype+'_words')] = 'nan'
        elif str(participant[str('file_'+filetype+'_words')]) is not 'nan':
            info_obj[str('path_'+filetype+'_words')] = os.path.join(
                experiment_folder,
                participant[str('file_'+filetype+'_words')]
            )
        path_list.append(info_obj)
    return path_list

def read_data_for_participant(path_list, filetype ='encoding'):
    data_list = []
    for participant in path_list:
        if filetype == 'encoding':
            data_obj = {
                'identifier': participant['identifier'],
                'vp_nr': participant['vp_nr'],
                'stimulation': participant['stimulation'],
                'df_faces': FileInput.read_encoding_data_txt_into_df(participant['path_encoding_faces']),
                'df_words': FileInput.read_encoding_data_txt_into_df(participant['path_encoding_words'])
            }
        elif filetype == 'memory':
            data_obj = {
                'identifier': participant['identifier'],
                'vp_nr': participant['vp_nr'],
                'stimulation': participant['stimulation'],
                'df_faces': FileInput.read_memory_data_txt_into_df(participant['path_memory_faces']),
                'df_words': FileInput.read_memory_data_txt_into_df(participant['path_memory_words'])
            }
        else:
            data_obj = {}
            print('filetype not supported')
        data_list.append(data_obj)
    return data_list

def read_stimulus_lists(basepath):
    faces_directory = os.path.join(
        basepath,
        'Faces'
    )
    words_directory = os.path.join(
        basepath,
        'Words'
    )
    encoding_filename = 'img_encoding.txt'
    recognition_a_filename = 'img_recognition_A.txt'
    recognition_b_filename = 'img_recognition_B.txt'

    df_encoding_faces_a, df_encoding_faces_b = FileInput.read_stimulus_encoding_txt_into_dfs(
        path= os.path.join(
            faces_directory,
            encoding_filename
        )
    )
    df_encoding_words_a, df_encoding_words_b = FileInput.read_stimulus_encoding_txt_into_dfs(
        path= os.path.join(
            words_directory,
            encoding_filename
        )
    )
    df_recognition_faces_a = FileInput.read_stimulus_recognition_txt_into_df(
        path= os.path.join(
            faces_directory,
            recognition_a_filename
        )
    )
    df_recognition_faces_b = FileInput.read_stimulus_recognition_txt_into_df(
        path= os.path.join(
            faces_directory,
            recognition_b_filename
        )
    )
    df_recognition_words_a = FileInput.read_stimulus_recognition_txt_into_df(
        path= os.path.join(
            words_directory,
            recognition_a_filename
        )
    )
    df_recognition_words_b = FileInput.read_stimulus_recognition_txt_into_df(
        path= os.path.join(
            words_directory,
            recognition_b_filename
        )
    )
    return {
        'df_encoding_faces_a': df_encoding_faces_a,
        'df_encoding_faces_b': df_encoding_faces_b,
        'df_encoding_words_a': df_encoding_words_a,
        'df_encoding_words_b': df_encoding_words_b,
        'df_recognition_faces_a': df_recognition_faces_a,
        'df_recognition_faces_b': df_recognition_faces_b,
        'df_recognition_words_a': df_recognition_words_a,
        'df_recognition_words_b': df_recognition_words_b,
    }

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

def stimulus_lists_workflow():
    basepath = ask_directory()
    stimulus_object = read_stimulus_lists(basepath)
    return stimulus_object
