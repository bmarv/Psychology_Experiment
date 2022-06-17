import os
from pathlib import Path

from tkinter import *
from tkinter import filedialog

def ask_directory():
    Tk().withdraw()
    folder_path = Path(filedialog.askdirectory())
    return folder_path

def read_directory_content():
    folder_path = ask_directory()
    return os.listdir(folder_path)