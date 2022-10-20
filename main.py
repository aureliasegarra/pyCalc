import tkinter
from tkinter import *

root = Tk()
root.title("Python Calculator")
root.geometry("420x350")
root.resizable(False, False)
root.configure(bg="#282C34")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text = equation)

def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text = result)


label_result = Label(root, width=35, height=2, text="", font=("roboto", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#3697f5", command=lambda: clear()).place(x=10,y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("%")).place(x=110, y=100)
Button(root, text="AC", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("AC")).place(x=210, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("/")).place(x=310, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#3697f5", command=lambda: show("7")).place(x=10,y=150)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("8")).place(x=110, y=150)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("9")).place(x=210, y=150)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("*")).place(x=310, y=150)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#3697f5", command=lambda: show("4")).place(x=10,y=200)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("5")).place(x=110, y=200)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("6")).place(x=210, y=200)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("+")).place(x=310, y=200)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#3697f5", command=lambda: show("1")).place(x=10,y=250)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("2")).place(x=110, y=250)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("3")).place(x=210, y=250)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("-")).place(x=310, y=250)

Button(root, text="0", width=17, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#73EDAE", command=lambda: show("0")).place(x=10, y=300)
Button(root, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#3697f5", command=lambda: calculate()).place(x=310, y=300)



root.mainloop()
