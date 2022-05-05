# Author: ATN 5/17/22

import tkinter as tk
from tkinter import ttk, Toplevel, Text

root = tk.Tk()

big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def close_window():
    exit()


def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        root.tk.call("set_theme", "light")
    else:
        root.tk.call("set_theme", "dark")


def create_examen():
    win_examen = Toplevel(root)
    win_examen.geometry("1024x768")
    t = Text(win_examen, height = 5, width = 52)

    text_examen = """this is some placeholder text this is some placeholder text this is some placeholder text"""

    t.pack()
    t.insert(tk.END, text_examen)


examen = ttk.Button(root, text="Examen", command=create_examen)
examen.pack()

theme = ttk.Button(root, text="Change", command=change_theme)
theme.pack()

close = ttk.Button(root, text="Exit", command=close_window)
close.pack()

root.mainloop()
