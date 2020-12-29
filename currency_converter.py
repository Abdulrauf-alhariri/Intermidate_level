from tkinter import *
import requests

root = Tk()

value = StringVar()
from_option = StringVar()
to_option = StringVar()


currenses = ["Euro",
             "Swedish krona"]


def convert():

    respons = requests.get(api).json()

    value_to_convert = value.get()

    if from_option.get() == currenses[0] and to_option.get() == currenses[1]:

        result = respons["rates"]["SEK"] * float(value_to_convert)
        value.set(str(result))

    elif from_option.get() == currenses[1] and to_option.get() == currenses[0]:
        result = float(value_to_convert) / respons["rates"]["SEK"]
        value.set(str(result))


def reset():
    value.set("")


def window():

    from_option.set(currenses[0])
    to_option.set(currenses[1])

    amount_label = Label(root, text="Amount", font=("Helvetica", 10))
    amount_label.grid(row=0, column=0, pady=7, padx=0, sticky=W)

    amount_entry = Entry(root, textvariable=value, width=30, borderwidth=7)
    amount_entry.grid(row=1, column=0, columnspan=2, padx=5)

    from_label = Label(root, text="from: ", font=("Helvetica", 10))
    from_label.grid(row=2, column=0, pady=7, sticky=W)

    to_label = Label(root, text="To: ", font=("Helvetica", 10))
    to_label.grid(row=4, column=0, pady=7, sticky=W)

    from_menue = OptionMenu(root, from_option, *currenses)
    from_menue.grid(row=3, column=0, sticky=W)

    to_menue = OptionMenu(root, to_option, *currenses)
    to_menue.grid(row=5, column=0, sticky=W)

    convert_button = Button(root, text="Convert", command=convert)
    convert_button.grid(row=6, column=0, pady=10, sticky=W)

    rest_button = Button(root, text="Reset", command=reset, width=10)
    rest_button.grid(row=6, column=1, pady=10)


window()
mainloop()
