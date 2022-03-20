import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class Window:
    
    def __init__(self):
        
        self.root=tk.Tk()
        
        self.label=tk.Label(self.root, text="Folder you'd like to back up:", font=("Arial", 18))
        self.label.pack(padx=10,pady=10)
        
        self.button=tk.Button(self.root,text="Browse", font=("Arial", 18), command=target_file)
        self.button.pack(padx=10,pady=10)
        
        self.root.mainloop()
        
def target_file():
        file = filedialog.askopenfile()
        return file
        
def create_file_array():
    file_array=[]
        
Window()