from tkinter import *
from operator import add, mul, sub, truediv
import string
import math

root = Tk()
root.title("My Calculate")

equation = StringVar()
expression = " "

e = Entry(root, textvariable=equation, width=60, borderwidth=7)
e.grid(row=0, column=0, columnspan=4, pady=15, padx=5)


def button_click(number):
    global expression

    expression = expression + str(number)
    equation.set(expression)


def equal_press():
    try:
        global expression

        result = str(eval(expression))
        total = math.floor(float(result))
        result = str(total)
        equation.set(result)
        expression = ""

    except:
        equation.set("erorr")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def window():

    myButton_7 = Button(root, text="7", pady=20, padx=40,
                        command=lambda: button_click(7))

    myButton_4 = Button(root, text="4", pady=20, padx=40,
                        command=lambda: button_click(4))

    myButton_1 = Button(root, text="1", pady=20, padx=40,
                        command=lambda: button_click(1))

    myButton_8 = Button(root, text="8", pady=20, padx=40,
                        command=lambda: button_click(8))

    myButton_5 = Button(root, text="5", pady=20, padx=40,
                        command=lambda: button_click(5))

    myButton_2 = Button(root, text="2", pady=20, padx=40,
                        command=lambda: button_click(2))

    myButton_9 = Button(root, text="9", pady=20, padx=40,
                        command=lambda: button_click(9))

    myButton_6 = Button(root, text="6", pady=20, padx=40,
                        command=lambda: button_click(6))

    myButton_3 = Button(root, text="3", pady=20, padx=40,
                        command=lambda: button_click(3))

    myButton_0 = Button(
        root, text="0", command=lambda: button_click(0), pady=20, padx=40)

    myButton_add = Button(
        root, text="+", command=lambda: button_click("+"), pady=20, padx=40, bg="orange")
    myButton_sub = Button(
        root, text="-", command=lambda: button_click("-"), pady=20, padx=40, bg="orange")
    myButton_mul = Button(
        root, text="X", command=lambda: button_click("*"), pady=20, padx=40, bg="orange")
    myButton_truediv = Button(
        root, text="/", command=lambda: button_click("/"), pady=20, padx=40, bg="orange")

    myButton_equal = Button(
        root, text="=", command=equal_press, pady=20, padx=40)
    myButton_clear = Button(
        root, text="Clear", command=clear, pady=20, padx=30)

    myButton_0.grid(row=4, column=0)
    myButton_clear.grid(row=4, column=1)
    myButton_equal.grid(row=4, column=2)
    myButton_truediv.grid(row=4, column=3)

    myButton_1.grid(row=3, column=0)
    myButton_2.grid(row=3, column=1)
    myButton_3.grid(row=3, column=2)
    myButton_add.grid(row=3, column=3)

    myButton_4.grid(row=2, column=0)
    myButton_5.grid(row=2, column=1)
    myButton_6.grid(row=2, column=2)
    myButton_sub.grid(row=2, column=3)

    myButton_7.grid(row=1, column=0)
    myButton_8.grid(row=1, column=1)
    myButton_9.grid(row=1, column=2)
    myButton_mul.grid(row=1, column=3)

    mainloop()


window()
