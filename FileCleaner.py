from datetime import datetime
# from os import scandir, rename
# from os.path import exists, join, splitext
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




def on_cleaner():
    headers = load_headers()


    with os.scandir(desktop_path) as entries:
        for entry in entries:
            name = entry.name
            start = name.split("_")
            if name.startswith(tuple(headers)):

                directory_path = os.path.join(desktop_path,f"{start[0]}_{start[1]}")

                if not os.path.exists(directory_path):
                    # If it doesn't exist, create it
                    os.makedirs(directory_path)
                    print(f"Directory created at: {directory_path}")
                else:
                    print(f"Directory already exists at: {directory_path}")


                print(f"Will move: {name} to the directory {directory_path}")

on_cleaner()