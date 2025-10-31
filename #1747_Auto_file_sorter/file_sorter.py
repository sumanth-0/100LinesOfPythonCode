import tkinter as tk
from tkinter import filedialog,Text,Frame,Button,INSERT,END,WORD,BOTH,LEFT,RIGHT,TRUE,Checkbutton,Listbox,Scrollbar,Y
from pathlib import Path
import shutil

selected_folder = None  
global file_ex 
def select_dir():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        l.config(text=f"Selected folder: {selected_folder}")

def organize_files():
    if selected_folder:
        target_dir = Path(selected_folder)
        is_preview = preview.get()  # Get checkbox value
        sort_files(selected_folder, target_dir, is_preview)

def dynamic_lw(listbox,files):
    longest = max(files,key=len)
    n_width = len(longest)
    listbox.config(width = n_width)

def sort_files(dir,target_dir,preview,):
    file_types = {
    ".pdf" : "PDF's",
    ".exe" : "Applications",
    ".zip" : "Zip_files",
    ".jpeg": "Images",
    ".png" : "Images",
    ".jpg" : "Images",
    ".xlsx": "Excel_Files",
    ".docx": "Word_Documents",
    ".txt" :"Text_Files"
}
    scroll = Scrollbar(canvas)
    preview_listbox = Listbox(canvas, relief=tk.RIDGE, yscrollcommand=scroll.set)
    scroll.config(command=preview_listbox.yview)
    
    
    if preview:
        scroll.pack(side=RIGHT, fill=Y)
        preview_listbox.pack(fill=BOTH, expand=True)
        preview_listbox.delete(0, tk.END)  # Clear previous results
    
    
    for file in target_dir.iterdir():
        if file.is_file():
            file_ex = file.suffix.lower()
            
            if file_ex not in file_types:
                if preview:
                    preview_listbox.insert(tk.END, f"{file_ex} is not supported")
            else:
                if preview:
                   
                    preview_listbox.insert(tk.END, f"Would move: {file.name} -> {file_types[file_ex]}")
                else:
                   
                    folder_path = Path(dir) / file_types[file_ex]
                    folder_path.mkdir(exist_ok=True)
                    shutil.move(file, folder_path)

canvas = tk.Tk()
canvas.geometry("300x250")
canvas.title("File Sorter")

frame = tk.Frame(master=canvas, relief=tk.RIDGE, borderwidth=5)
frame.pack(padx=10,pady=5)
frame.config()

l= tk.Label(master=frame,text = "Slected folder : No folder is sleected")
l.pack(in_=frame)

b1 = Button(master=frame , text="Select",command = select_dir)
b1.pack()

Checkbutton1 = tk.IntVar()
preview = tk.IntVar()
Button1 = Checkbutton(canvas, text = "Log", 
                    variable = Checkbutton1, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10)

Button2 = Checkbutton(canvas, text = "Preview", 
                    variable = preview, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10)

b2= Button(canvas, text="Organize", command = organize_files)

Button1.pack()
Button2.pack()
b2.pack()
canvas.mainloop()