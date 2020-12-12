from tkinter import *
from tkinter import messagebox
import time


root = Tk()
root.title("My timer")
hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")

hours_entry = Entry(root, textvariable=hours, font=("Arial", 18, ""), width=7)
minutes_entry = Entry(root, textvariable=minutes,
                      font=("Arial", 18, ""), width=7)
seconds_entry = Entry(root, textvariable=seconds,
                      font=("Arial", 18, ""), width=7)

hours_entry.grid(row=0, column=0)
minutes_entry.grid(row=0, column=1)
seconds_entry.grid(row=0, column=2)


def timer():
    try:
        sekunder = int(hours.get()) * 3600 + \
            int(minutes.get()) * 60 + int(seconds.get())
    except:
        print("plaease enter a valid value")

    while sekunder > -1:
        hour, sec = divmod(sekunder, 3600)
        minute, sec = divmod(sekunder, 60)

        hours.set("{0:2d}".format(hour))
        minutes.set("{0:2d}".format(minute))
        seconds.set("{0:2d}".format(sec))

        root.update()
        time.sleep(1)

        if sekunder == 0:
            messagebox.showinfo("Wake up! It's time")

        sekunder -= 1


my_button = Button(root, text="Set Timer!", command=timer, width=10)
my_button.grid(row=2, column=1)

root.mainloop()
