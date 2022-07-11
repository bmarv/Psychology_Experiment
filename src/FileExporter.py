import os

import pandas as pd

from src import InputHandler

def write_dataframe_to_csv(dataframe: pd.DataFrame, filetype = 'encoding', file_name = None):
    folder_path = InputHandler.ask_directory()
    if file_name is not None:
        if filetype == 'encoding':
            file_name = 'encoding_data.csv'
        elif filetype == 'recognition':
            file_name = 'recognition_data.csv'
        else:
            file_name = 'unified_data.csv'
    file_path = os.path.join(
        folder_path,
        file_name
    )
    try:
        dataframe.to_csv(
            file_path,
            sep = '\t'
        )
    except Exception as err:
        print('error saving file: {0}'.format(err))
    return file_path

def write_dataframe_to_excel(dataframe: pd.DataFrame, filetype = 'encoding', file_name = None):
    folder_path = InputHandler.ask_directory()
    if file_name is not None:
        if filetype == 'encoding':
            file_name = 'encoding_data.xlsx'
        elif filetype == 'recognition':
            file_name = 'recognition_data.xlsx'
        else:
            file_name = 'unified_data.xlsx'
    file_path = os.path.join(
        folder_path,
        file_name
    )
    try:
        dataframe.to_excel(
            file_path,
        )
    except Exception as err:
        print('error saving file: {0}'.format(err))
    return file_path
