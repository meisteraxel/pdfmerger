#PDF Merger

#Import Libraries
from PyPDF2 import PdfMerger
import os
import tkinter
from tkinter import filedialog
import customtkinter

#Set TK Window
customtkinter.set_appearance_mode("System")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("PDF Merger")
app.grid_columnconfigure(0, weight=1)

#Define Functions
merger = PdfMerger()

def filepath():
    global files
    files = filedialog.askdirectory()

def merge():
    for root, dirs, file_names in os.walk(files):
        for file_name in file_names:
            merger.append(files + "/" + file_name)
    merger.write("merged_pdfs.pdf")
    merger.close()

#Define Buttons/Labels
label = customtkinter.CTkLabel(app, text="PDF Merger - created by Axel", fg_color="transparent")
label.grid(row=0, column=0, padx=20, pady=20)

path_button = customtkinter.CTkButton(app, text="File Path", command=filepath)
path_button.grid(row=1, column=0, padx=20, pady=10)

merge_button = customtkinter.CTkButton(app, text="Merge Files", command=merge)
merge_button.grid(row=2, column=0, padx=20, pady=20)


app.mainloop()

