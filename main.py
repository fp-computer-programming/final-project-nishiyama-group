# Author: ATN 5/17/22

import tkinter as tk
from tkinter import ttk, Toplevel, Text
from ttkthemes import themed_tk as tttk
import random

root = tttk.ThemedTk()
root.get_themes()
root.set_theme("plastik")


big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

def close_window():
    exit()


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


def create_generosity_page_1():
    win_generosity = Toplevel(root)
    win_generosity.geometry("720x480")
    t = Text(win_generosity, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    generosity_1 = """Lord Jesus, teach me to be generous. Teach me to serve as you deserve, \nto give and not to count the cost, to fight and not to heed the wounds, to \nlabor and not to seek to rest, to give of my self and not ask for a reward, \nexcept the reward of knowing that I am doing your will. St. Ignatius of \nLoyola, pray for us. Amen"""
    t.pack()
    t.insert(tk.END, generosity_1)
    close = ttk.Button(win_generosity, text="Close", command=win_generosity.destroy)
    close.pack()


def create_ourfather_page_1():
    win_ourfather = Toplevel(root)
    win_ourfather.geometry("720x480")
    t = Text(win_ourfather, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    ourfather_1 = """Our Father, who art in heaven, hallowed be thy name; thy kingdom come; \nthy will be done on earth as it is in heaven. Give us this day our daily \nbread; and forgive us our trespasses as we forgive those who trespass \nagainst us; and lead us not into temptation, but deliver us from evil. Amen."""
    t.pack()
    t.insert(tk.END, ourfather_1)
    close = ttk.Button(win_ourfather, text="Close", command=win_ourfather.destroy)
    close.pack()


def create_serenity_page_1():
    win_serenity = Toplevel(root)
    win_serenity.geometry("720x480")
    t = Text(win_serenity, height = 5, width = 100)
    t.configure(font=("Arial", 20, "bold"))
    serenity_1 = """God, grant me the serenity to accept the things I cannot change, courage \nto change the things I can, and wisdom to know the difference."""
    t.pack()
    t.insert(tk.END, serenity_1)
    close = ttk.Button(win_serenity, text="Next", command=win_serenity.destroy)
    close.pack()


examen = ttk.Button(root, text="Examen", command=create_examen_page_1)
examen.pack()

generosity = ttk.Button(root, text="Generosity", command=create_generosity_page_1)
generosity.pack()

ourfather = ttk.Button(root, text="Our Father", command=create_ourfather_page_1)
ourfather.pack()

serenity = ttk.Button(root, text="Serenity", command=create_serenity_page_1)
serenity.pack()

tasks = ttk.Button(root, text="Tasks", command=list_tasks_page_1)
tasks.pack()

close = ttk.Button(root, text="Exit", command=close_window)
close.pack()

root.mainloop()
