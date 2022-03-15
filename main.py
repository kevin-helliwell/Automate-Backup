# Import the following modules
from multiprocessing.sharedctypes import Array
import shutil
from datetime import date
import os
import sys

# What it actually does
# Makes an array of directories to copy into backup folders
# Loops over array to copy directories into separate backup folders
# Creates main backup folder to bundle them into
# Moves backup folders into main backup folder

# What I need this script to do:
# 1) Create new backup folder, rename with today's date
# 2) Copy folders/files from source folder given paths of folders/files
# 3) Paste files to backup folder given path of backup folder


today = date.today()
date_format = today.strftime("%d_%b_%Y_")

# Makes backup folder we eventually move to
path = "C:/Users/kbh78/Desktop"
ui_backup_path = path + "/UI_Backup " + f"{date_format}"
os.mkdir(ui_backup_path)

arr = ["Interface", "WTF"]
for i in range(0, len(arr)):
    src = f"C:/Program Files (x86)/World of Warcraft/_retail_/{arr[i]}"
    dst = f"C:/Users/kbh78/Desktop/{arr[i]} Backup " + f"{date_format}"
    shutil.copytree(src, dst)
    shutil.move(dst, ui_backup_path)

# src1 = f"C:/Program Files (x86)/World of Warcraft/_retail_/{arr[0]}"
# dst1 = f"C:/Users/kbh78/Desktop/{arr[0]} Backup " + f"{date_format}"
# shutil.copytree(src1, dst1)

# src2 = f"C:/Program Files (x86)/World of Warcraft/_retail_/{arr[1]}"
# dst2 = f"C:/Users/kbh78/Desktop/{arr[1]} Backup " + f"{date_format}"
# shutil.copytree(src2, dst2)

# # Moves folders to final folder
# shutil.move(dst1, ui_backup_path)
# shutil.move(dst2, ui_backup_path)
