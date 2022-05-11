# Author: ATN 5/17/22

import tkinter as tk
from tkinter import ttk, Toplevel, Text
import random

root = tk.Tk()

big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

personality_type = 'extroverted'

def close_window():
    exit()


def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        root.tk.call("set_theme", "light")
    else:
        root.tk.call("set_theme", "dark")


def create_examen_page_1():
    win_examen = Toplevel(root)
    win_examen.geometry("720x480")
    t = Text(win_examen, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    examen_1 = """1. Place yourself in God’s presence. \nGive thanks for God’s great love for you."""
    t.pack()
    t.insert(tk.END, examen_1)
    next = ttk.Button(win_examen, text="Next", command=lambda:[create_examen_page_2(), win_examen.destroy()])
    next.pack()


def create_examen_page_2():
    win_examen = Toplevel(root)
    win_examen.geometry("720x480")
    t = Text(win_examen, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    examen_2 = """2. Pray for the grace to understand how God is acting in your life."""
    t.pack()
    t.insert(tk.END, examen_2)
    next = ttk.Button(win_examen, text="Next", command=lambda:[create_examen_page_3(), win_examen.destroy()])
    next.pack()


def create_examen_page_3():
    win_examen = Toplevel(root)
    win_examen.geometry("720x480")
    t = Text(win_examen, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    examen_3 = """3. Review your day — recall specific moments and your feelings at the \ntime."""
    t.pack()
    t.insert(tk.END, examen_3)
    next = ttk.Button(win_examen, text="Next", command=lambda:[create_examen_page_4(), win_examen.destroy()])
    next.pack()


def create_examen_page_4():
    win_examen = Toplevel(root)
    win_examen.geometry("720x480")
    t = Text(win_examen, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    examen_4 = """4. Reflect on what you did, said, or thought in those instances. Were you \ndrawing closer to God, or further away?"""
    t.pack()
    t.insert(tk.END, examen_4)
    next = ttk.Button(win_examen, text="Next", command=lambda:[create_examen_page_5(), win_examen.destroy()])
    next.pack()


def create_examen_page_5():
    win_examen = Toplevel(root)
    win_examen.geometry("720x480")
    t = Text(win_examen, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    examen_5 = """5. Look toward tomorrow — think of how you might collaborate more \neffectively with God’s plan. Be specific, and conclude with the \n“Our Father.”"""
    t.pack()
    t.insert(tk.END, examen_5)
    finish = ttk.Button(win_examen, text="Finish", command=win_examen.destroy)
    finish.pack()


tasks = {
    "Compliment a stranger" : "1",
    "Volunteer at an organization" : "3",
    "Donate to a charity" : "3"
}

keys = list(tasks.keys())
random.shuffle(keys)

values = list(tasks.values())
random.shuffle(values)

# hoping to sort out tasks as given by the user's personality type
def personality():
    win_personality = Toplevel(root)
    win_personality.geometry("720x480")
    t = Text(win_personality, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    personalities = """Personality type: {0}""".format(personality_type)
    t.pack()
    t.insert(tk.END, personalities)
    # introverted = ttk.Button(win_personality, text="Introverted", command=)
    # introverted.pack()
    # extroverted = ttk.Button(win_personality, text="Extroverted", command=)
    # extroverted.pack()
    leave = ttk.Button(win_personality, text="leave", command=win_personality.destroy)
    leave.pack()

    
def list_tasks_page_1():
    win_tasks = Toplevel(root)
    win_tasks.geometry("720x480")
    t = Text(win_tasks, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    tasks_1 = """{0} Difficulty: {1}""".format(keys[0], values[0])
    t.pack()
    t.insert(tk.END, tasks_1)
    next = ttk.Button(win_tasks, text="Next", command=lambda:[list_tasks_page_2(), win_tasks.destroy()])
    next.pack()


def list_tasks_page_2():
    win_tasks = Toplevel(root)
    win_tasks.geometry("720x480")
    t = Text(win_tasks, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    tasks_2 = """{0} Difficulty: {1}""".format(keys[1], values[1])
    t.pack()
    t.insert(tk.END, tasks_2)
    next = ttk.Button(win_tasks, text="Next", command=lambda:[list_tasks_page_3(), win_tasks.destroy()])
    next.pack()


def list_tasks_page_3():
    win_tasks = Toplevel(root)
    win_tasks.geometry("720x480")
    t = Text(win_tasks, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    tasks_3 = """{0} Difficulty: {1}""".format(keys[2], values[2])
    t.pack()
    t.insert(tk.END, tasks_3)
    leave = ttk.Button(win_tasks, text="Leave", command=win_tasks.destroy)
    leave.pack()




examen = ttk.Button(root, text="Examen", command=create_examen_page_1)
examen.pack()

tasks = ttk.Button(root, text="Tasks", command=list_tasks_page_1)
tasks.pack()

personality = ttk.Button(root, text="Personality", command=personality)
personality.pack()

theme = ttk.Button(root, text="Theme", command=change_theme)
theme.pack()

close = ttk.Button(root, text="Exit", command=close_window)
close.pack()

root.mainloop()
