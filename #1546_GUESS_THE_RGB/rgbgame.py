import tkinter as tk
import random
from tkinter import messagebox

def new_color():
    global target
    target=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    hexc='#%02x%02x%02x'%target
    canvas.config(bg=hexc) #set new color
    status.set("New color generated. Make a guess!")

def check_guess():
    try:
        r=int(e_r.get());g=int(e_g.get()); b=int(e_b.get())
    except ValueError:
        messagebox.showerror("Invalid input","Enter integers")
        return
    if not all(0<=v<=255 for v in (r,g,b)):
        messagebox.showerror("Out of range","Values must be between 0 and 255.")
        return
    guessed=(r,g,b)
    if guessed == target:
        status.set("Correct! Exact match.")
    else:
        dist=((r-target[0])**2+(g-target[1])**2+(b-target[2])**2) ** 0.5
        #compute eucilidean dist
        status.set(f"Ahh try again, distance:{dist:.1f}. target was:{target}")
    if guessed == target:
        root.after(1000,new_color)

root=tk.Tk()
root.title("Guess the RGB Color")
root.resizable(False, False)
canvas = tk.Frame(root, width=300, height=150)
canvas.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
color_area = tk.Label(canvas, width=40, height=8, bd=2, relief="sunken")
color_area.pack(expand=True, fill="both")
canvas=color_area
tk.Label(root,text="R").grid(row=1, column=0)
tk.Label(root,text="G").grid(row=1, column=1)
tk.Label(root,text="B").grid(row=1, column=2)
e_r=tk.Entry(root,width=6);e_r.grid(row=2,column=0,padx=4)
e_g=tk.Entry(root,width=6);e_g.grid(row=2,column=1,padx=4)
e_b=tk.Entry(root,width=6);e_b.grid(row=2,column=2,padx=4)
guess_btn=tk.Button(root, text="Guess",command=check_guess)
guess_btn.grid(row=2, column=3, padx=6)
status=tk.StringVar()
status.set("Click 'New Color' to start.")
tk.Label(root,textvariable=status, wraplength=300, justify="left").grid(row=3, column=0, columnspan=4, pady=8)
new_btn = tk.Button(root, text="New Color", command=new_color)
new_btn.grid(row=4, column=0, columnspan=2, pady=6)
quit_btn = tk.Button(root, text="Quit", command=root.destroy)
quit_btn.grid(row=4, column=2, columnspan=2, pady=6)
target = (0,0,0)
new_color()
root.mainloop()
