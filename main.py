# Import the following modules
import shutil
from datetime import date
import os
import sys

# What I need this script to do:
# 1) Create new backup folder, rename with today's date
# 2) Copy folders/files from source folder given paths of folders/files
# 3) Paste files to backup folder given path of backup folder

arr = ["Interface", "WTF"]

today = date.today()
date_format = today.strftime("%d_%b_%Y_")
path = "C:/Users/kbh78/Desktop"

src1 = "C:/Program Files (x86)/World of Warcraft/_retail_/Interface"
dst1 = f"C:/Users/kbh78/Desktop/{arr[0]} Backup " + f"{date_format}"
shutil.copytree(src1, dst1)

src2 = "C:/Program Files (x86)/World of Warcraft/_retail_/WTF"
dst2 = f"C:/Users/kbh78/Desktop/{arr[1]} Backup " + f"{date_format}"
shutil.copytree(src2, dst2)

# Makes backup folder we eventually move to
ui_backup_path = path + "/UI_Backup " + f"{date_format}"
os.mkdir(ui_backup_path)

# Moves folders to final folder
shutil.move(dst1, ui_backup_path)
shutil.move(dst2, ui_backup_path)
