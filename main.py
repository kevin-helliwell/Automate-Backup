# Import the following modules
import shutil
from datetime import date
import os
import sys

# What I need this script to do:
# 1) Create new backup folder, rename with today's date
# 2) Copy folders/files from source folder given paths of folders/files
# 3) Paste files to backup folder given path of backup folder

# What it actually does:
# Creates a main backup folder in destination path
# Takes an array of sub-directory strings to specify what sub-directories to copy from source path
# Loops over array to copy sub-directories into separate backup folders
# Moves backup folders in destination path into main backup folder

# Questions:
# What is the path address of the directory you'd like to store your backup folder in?
# What would you like to name your backup folder?
# What is the path address of your source directory?
# What are the names of the sub-directories you'd like to back up?


def create_backup(source_path, source_sub_arr, backup_path, backup_name):

    # Initializes date for backup folder to name itself correctly
    today = date.today()
    date_format = today.strftime("%d_%b_%Y_")

    # Creates backup folder in destination path
    local_backup_path = backup_path + f"/{backup_name} " + f"{date_format}"
    os.mkdir(local_backup_path)

    # Creates copies of chosen sub-directories (source_sub_arr) in source path, then moves them into backup folder
    for i in range(0, len(source_sub_arr)):
        src = f"{source_path}/{source_sub_arr[i]}"
        dst = f"{backup_path}/{source_sub_arr[i]} Backup " + f"{date_format}"
        shutil.copytree(src, dst)
        shutil.move(dst, local_backup_path)


# Example
# create_backup(
#     "C:/Program Files (x86)/World of Warcraft/_retail_",
#     ["Interface", "WTF"],
#     "C:/Users/kbh78/Desktop",
#     "UI_Backup",
# )
<<<<<<< Updated upstream

# Example
# create_backup(
#     "C:/Program Files (x86)/World of Warcraft/_retail_",
#     ["Interface", "WTF", "Logs"],
#     "C:/Users/kbh78/Desktop",
#     "UI_Backup",
# )
=======
>>>>>>> Stashed changes


# OLD WAY
# today = date.today()
# date_format = today.strftime("%d_%b_%Y_")

# # Makes backup folder in destination path
# main_backup_path = "C:/Users/kbh78/Desktop"
# backup_name = "UI_Backup"
# local_backup_path = main_backup_path + f"/{backup_name} " + f"{date_format}"
# os.mkdir(local_backup_path)

# # Makes copies of sub-directories in main backup path, moves them into backup folder
# source_path = "C:/Program Files (x86)/World of Warcraft/_retail_"
# arr = ["Interface", "WTF"]
# for i in range(0, len(arr)):
#     src = f"{source_path}/{arr[i]}"
#     dst = f"{main_backup_path}/{arr[i]} Backup " + f"{date_format}"
#     shutil.copytree(src, dst)
#     shutil.move(dst, local_backup_path)
# OLD WAY
