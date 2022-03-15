# Import the following modules
import shutil
from datetime import date
import os
import sys

# What it actually does:
# Creates a main backup folder
# Makes an array of directories
# Loops over array to copy directories into separate backup folders
# Moves backup folders into main backup folder

# What I need this script to do:
# 1) Create new backup folder, rename with today's date
# 2) Copy folders/files from source folder given paths of folders/files
# 3) Paste files to backup folder given path of backup folder

# What is the path address of your source directory?
# What are the names of the sub-directories you'd like to back up?
# What is the path address of the directory you'd like to store your backup folder?
# What would you like to name your backup folder?

# backup_name, main_dir, sub_dir, backup_dir:
# backup_name: "UI Backup"
# main_dir: "C:/Program Files (x86)/World of Warcraft/_retail_/"
# sub_dir(s): "Interface", "WTF"
# backup_dir: "C:/Users/kbh78/Desktop"

today = date.today()
date_format = today.strftime("%d_%b_%Y_")

# Makes backup folder in destination path
main_backup_path = "C:/Users/kbh78/Desktop"
backup_name = "UI_Backup"
local_backup_path = main_backup_path + f"/{backup_name} " + f"{date_format}"
os.mkdir(local_backup_path)

# Makes copies of sub-directories in main backup path, moves them into backup folder
source_path = "C:/Program Files (x86)/World of Warcraft/_retail_"
arr = ["Interface", "WTF"]
for i in range(0, len(arr)):
    src = f"{source_path}/{arr[i]}"
    dst = f"{main_backup_path}/{arr[i]} Backup " + f"{date_format}"
    shutil.copytree(src, dst)
    shutil.move(dst, local_backup_path)
