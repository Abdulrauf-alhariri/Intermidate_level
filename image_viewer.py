from tkinter import *
from PIL import ImageTk
import PIL.Image
import os

root = Tk()
root.title("View app")

my_image1 = ImageTk.PhotoImage(PIL.Image.open(
    os.path.join(r"C:\Users\abdullrauf.alhariri\Desktop\HelloWorld\Intermidiate_level\image_app\bild1.jpg")))

my_image3 = ImageTk.PhotoImage(PIL.Image.open(
    os.path.join(r"C:\Users\abdullrauf.alhariri\Desktop\HelloWorld\Intermidiate_level\image_app\bild3.jpg")))

my_image2 = ImageTk.PhotoImage(PIL.Image.open(
    os.path.join(r"C:\Users\abdullrauf.alhariri\Desktop\HelloWorld\Intermidiate_level\image_app\bild2.jpg")))

image_list = [my_image1, my_image2, my_image3]

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global button_exit

    my_label.grid_forget()
    button_forward.grid_forget()
    button_back.grid_forget()
    button_exit.grid_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(
        root, text=">>>", command=lambda: forward(image_number + 1))
    button_back = Button(
        root, text="<<<", command=lambda: backward(image_number - 1))
    button_exit = Button(root, text="Exit Program", command=root.quit, width=8)

    if image_number == 3:
        button_forward = Button(root, text=">>>", state=DISABLED)

    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)


def backward(image_number):
    global my_label
    global button_forward
    global button_back
    global button_exit

    my_label.grid_forget()
    button_forward.grid_forget()
    button_back.grid_forget()
    button_exit.grid_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(
        root, text=">>>", command=lambda: forward(image_number + 1))
    button_back = Button(
        root, text="<<<", command=lambda: backward(image_number - 1))

    button_exit = Button(root, text="Exit Program", command=root.quit, width=8)

    if image_number == 3:
        button_forward = Button(root, text=">>>", state=DISABLED)

    elif image_number == 1:
        button_back = Button(root, text="<<<", state=DISABLED)

    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)


button_back = Button(root, text="<<<", command=lambda: backward(1), width=8)
button_back.grid(row=1, column=0)

button_exit = Button(root, text="Exit Program", command=root.quit, width=8)
button_exit.grid(row=1, column=1)

button_forward = Button(root, text=">>>", width=8, command=lambda: forward(2))
button_forward.grid(row=1, column=2)
root.mainloop()
