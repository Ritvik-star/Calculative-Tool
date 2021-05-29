import tkinter
from tkinter import *
from tkinter import Button, Entry, Label, Message, StringVar, font
from tkinter.constants import ACTIVE, BOTH, LEFT, SE
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.configure(background="#e1e5ea")
root.title("MASTER CALCULATOR")

ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

w = 500
h = 400

x = int(ws/2-w/2)
y = int(wh/2-h/2)

data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)

root.geometry(data)    #it can take 4 arguments(widthxheight+x+y)




def openNewWindow():
    global newwindow1
    newwindow1 = tkinter.Toplevel(root)
    newwindow1.title("BASIC CALCULATOR")
    newwindow1.configure(background="#c6ffc1")
    newwindow1.geometry("250x400+300+300")

    ws = newwindow1.winfo_screenwidth()
    wh = newwindow1.winfo_screenheight()

    w = 500
    h = 400

    x = int(ws/2-w/2)
    y = int(wh/2-h/2)

    data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)

    newwindow1.geometry(data)    #it can take 4 arguments(widthxheight+x+y)


    
    val = ""
    A = 0
    operator = ""

    def btn_1_isclicked():
        global val
        val = val + "1"
        data.set(val)

    def btn_2_isclicked():
        global val
        val = val + "2"
        data.set(val)

    def btn_3_isclicked():
        global val
        val = val + "3"
        data.set(val)

    def btn_4_isclicked():
        global val
        val = val + "4"
        data.set(val)

    def btn_5_isclicked():
        global val
        val = val + "5"
        data.set(val) 

    def btn_6_isclicked():
        global val
        val = val + "6"
        data.set(val)

    def btn_7_isclicked():
        global val
        val = val + "7"
        data.set(val)

    def btn_8_isclicked():
        global val
        val = val + "8"
        data.set(val)

    def btn_9_isclicked():
        global val
        val = val + "9"
        data.set(val)

    def btn_0_isclicked():
        global val
        val = val + "0"
        data.set(val)                           

        
# functions for the operator button click
    def btn_plus_clicked():
        global A
        global operator,val
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)


    def btn_minus_clicked():
        global A
        global operator,val
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)


    def btn_mult_clicked():
        global A
        global operator,val
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)


    def btn_div_clicked():
        global A
        global operator,val
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)


    def btn_c_clicked():
        global A
        global operator,val
        val = ""
        A = 0
        operator = ""
        data.set(val)                



# function to find the result
    def result():
        global A,operator,val
        val2 = val
        if operator == "+":
            x = int((val2.split("+")[1]))
            C = A + x
            val = str(C)
            data.set(val)
        if operator == "-":
            x = int((val2.split("-")[1]))
            C = A - x
            val = str(C)
            data.set(val)
        if operator == "*":
            x = int((val2.split("*")[1]))
            C = A * x
            val = str(C)
            data.set(val)
        if operator == "/":
            x = int((val2.split("/")[1]))
            if x == 0:
                messagebox.showerror("Error","Division By 0 Not Supported")
                A = ""
                val = ""
                data.set(val)
            else:    
                C =int(A/x)
                data.set(C)


# the label that shows the result
    data = StringVar()
    lbl = Label(
        newwindow1,
        text="Label",
        anchor = SE,
        font = ("Verdana", 20),
        textvariable = data,
        background = "#ffffff",
        fg = "#000000",
    )
    lbl.pack(expand=True, fill="both")


# the frames section
    btnrow1 = Frame(newwindow1)
    btnrow1.pack(expand = True, fill = "both")

    btnrow2 = Frame(newwindow1)
    btnrow2.pack(expand = True, fill = "both")

    btnrow3 = Frame(newwindow1)
    btnrow3.pack(expand = True, fill = "both")

    btnrow4 = Frame(newwindow1)
    btnrow4.pack(expand = True, fill = "both")


# The buttons section
    btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
    )
    btn1.pack(side = LEFT, expand = True, fill = "both",)

    btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
    )
    btn2.pack(side = LEFT, expand = True, fill = "both",) 

    btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
    )
    btn3.pack(side = LEFT, expand = True, fill = "both",)

    btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
    )
    btnplus.pack(side = LEFT, expand = True, fill = "both",)


    btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
    )
    btn4.pack(side = LEFT, expand = True, fill = "both",)

    btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
    )
    btn5.pack(side = LEFT, expand = True, fill = "both",)

    btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
    )
    btn6.pack(side = LEFT, expand = True, fill = "both",)

    btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
    )
    btnminus.pack(side = LEFT, expand = True, fill = "both",)

    btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
    )
    btn7.pack(side = LEFT, expand = True, fill = "both",)

    btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
    )
    btn7.pack(side = LEFT, expand = True, fill = "both",)

    btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
    )
    btn9.pack(side = LEFT, expand = True, fill = "both",)

    btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult_clicked,
    )
    btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4

    btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_clicked,
    )
    btnc.pack(side = LEFT, expand = True, fill = "both",)

    btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,    
    )
    btn0.pack(side = LEFT, expand = True, fill = "both",)

    btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,    
    )
    btnequal.pack(side = LEFT, expand = True, fill = "both",)

    btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,    
    )
    btndiv.pack(side = LEFT, expand = True, fill = "both",)
    newwindow1.mainloop()





lbl0 = tkinter.Label(root, text="CHOOSE YOUR CALCULATION")
lbl0.pack(pady=30)

btn1 = tkinter.Button(root,
border=1,
relief=GROOVE,
text="BASIC CALCULATOR",
command=openNewWindow,)
btn1.pack()

btn2 = Button(root,
border=1,
relief=GROOVE,
text="CONVERSIONS",

)
btn2.pack(pady=20)


btn3 = Button(root,
border=1,
relief=GROOVE,
text="INCOME TAX",
)
btn3.pack()


btn4 = Button(root,
border=1,
relief=GROOVE,
text="GST",

)
btn4.pack(pady=20)



root.mainloop()    