import os
import random
from tkinter import *

W = Tk()
W.title('Guess The Number - GUI Version 0')
W.geometry('800x800')

for x in range(4): W.columnconfigure(x, weight=1)

T = Label(W, text="Welcome to Guess The Number\nFrom 0 to 99\nYou get 5 attempts.\nGO!!!")
T.grid(column=1, row=0, columnspan=2)

number_label = Label(W, text="Enter guess:")
number_label.grid(column=0, row=3)
number_label_field = Entry()
number_label_field.grid(column=1, row=3, columnspan=2)

W=mainloop()
