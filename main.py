# Author: ATN 5/17/22

from tkinter import *
import customtkinter

main = Tk()

main.geometry("1024x768")
main.configure(bg='white')

def close_window():
    exit()



examen = Button(main, text='Examen')
examen.pack()

close = Button(main, text='Exit', command=close_window)
close.pack()

mainloop()
