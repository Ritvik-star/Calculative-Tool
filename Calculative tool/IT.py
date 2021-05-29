from ast import Num
import tkinter
from tkinter import Button, Entry, Label, font
from tkinter.constants import COMMAND, END, GROOVE, LEFT
from typing import Text
import random

root = tkinter.Tk()
root.title("Master Calculator")
root.geometry("250x400+300+300")
root.configure(background="#e1e5ea")
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

w = 500
h = 400

x = int(ws/2-w/2)
y = int(wh/2-h/2)

data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)


def ITamount():
    amount = int(user_entry.get())
#With deductions and exemptions
    if (amount) <=250000 :
        tax = 0
        total_IT = (amount)
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

        

    if amount > 250000 and amount <=500000:
        tax = (amount*5) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

    if amount > 500001 and amount <= 750000:
        tax = (amount*20) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

    if amount > 750001 and amount <= 1000000:
        tax = (amount*20) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

    if amount > 1000001 and amount <=1250001:
        tax = (amount*20) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()
    
    if amount > 1250001 and amount <=1500000:
        tax = (amount*20) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

    if amount >= 1500001: 
        tax = (amount*20) / 100
        total_IT = amount + tax
        lbl0 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("tax is", tax),
        )
        lbl0.pack()
        lbl1 = Label(
            root,
            font=("Times New Roman",16),
            fg="#000000",
            bg="#f0ebcc",
            text=("ITR is",total_IT),
        )
        lbl1.pack()

    

lbl8 = Label(
    root,
    text="amount for IT",
    relief=GROOVE,
    border=0,
    font=("Times New Roman",16),
    width=10,
    height=2,
)
lbl8.pack(pady=20)

user_entry = Entry(
    root,
    font=("Times New Roman",16),
    )
user_entry.pack()
btn1 = Button(
    root,
    text="check",
    font=("Times New Roman",16),
    width=10,
    height=2,
    relief=GROOVE,
    border=0,
    command=ITamount,
)
btn1.pack(pady=20)



root.mainloop()    

