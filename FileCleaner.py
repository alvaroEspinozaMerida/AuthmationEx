import shutil
from datetime import datetime
# from os import scandir, rename
from os.path import exists, join, splitext
from os import scandir, rename
import os
from shutil import move
import json


import logging
"""
FILE CLEANER SCRIPT - Will Run Twice a Day on my Mac to clean up any files that I may leave on my desktop 
the objective is to take files from my classes that I may have created or that I downloaded and go and automatically clean them up 

the program will determine where each of these files will be sent through the use of a special json file that keeps track of the special headers 
for example CS_448_Lecture_1.pt will have the header CS_448 once the file is read the header is removed and the only "lecture_1.pt" will be moved to 
a folder with the name CS_448 

"""
# Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


headers_path =  os.path.join(os.path.expanduser("~"), "Desktop", "headers.json")


current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

print(f"File Cleaner Activated at {current_time}")

def load_headers():
    if os.path.exists(headers_path):
        with open(headers_path, 'r') as file:
            return json.load(file)
    return []
def save_headers(names):
    with open(headers_path, 'w') as file:
        json.dump(names, file, indent=4)


def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1

    # Construct the full path using os.path.join to ensure OS-agnostic behavior
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry):
    if exists(f"{dest}/{entry}"):
        unique_name = make_unique(dest, entry)
        oldName = join(dest, entry)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

def on_cleaner():
    headers = load_headers()


    with os.scandir(desktop_path) as entries:
        for entry in entries:
            name = entry.name
            # print(f"Processing {name}")
            start = name.split("_")

            if name.startswith(tuple(headers)):

                directory_path = os.path.join(desktop_path,f"{start[0]}_{start[1]}")

                # Makes directory if doesnt not exist
                if not os.path.exists(directory_path):
                    # If it doesn't exist, create it
                    os.makedirs(directory_path)
                #checks files name to check if  it already exist inside of the directory

                if os.path.exists(os.path.join(directory_path, name)):

                    unique_name = make_unique(directory_path, name)
                    directory_path = os.path.join(directory_path, unique_name)
                else:
                    directory_path = os.path.join(directory_path, unique_name)

                shutil.move(entry, directory_path)




on_cleaner()