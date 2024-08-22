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

headers = file_path = os.path.join(os.path.expanduser("~"), "Desktop", "headers.json")


current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

print(f"File Cleaner Activated at {current_time}")