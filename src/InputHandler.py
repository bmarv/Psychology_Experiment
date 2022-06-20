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
    if filetype == 'encoding': 
        encoding_folder = os.path.join(
            basepath,
            'experiment_data'
        )
        encoding_info_file = os.path.join(
            basepath,
            'data.xlsx'
        )
        encoding_info_df = FileInput.read_excel_file_content_into_pd_dataframe(encoding_info_file)
        encoding_info_df = FileInput.filter_participants_for_complete_data(
            df = encoding_info_df, 
            faces_encoding_available = True, 
            words_encoding_available = True
        )
        encoding_file_names_list = FileInput.get_participant_information_list(
            df = encoding_info_df,
            filetype = filetype
        )
        encoding_path_list = []
        for participant in encoding_file_names_list:
            info_obj = {
                'identifier': participant['identifier'],
                'path_encoding_faces': os.path.join(
                    encoding_folder,
                    participant['file_encoding_faces']
                ),
                'path_encoding_words': os.path.join(
                    encoding_folder,
                    participant['file_encoding_words']
                )
            }
            encoding_path_list.append(info_obj)
        return encoding_path_list
    else:
        return -1
