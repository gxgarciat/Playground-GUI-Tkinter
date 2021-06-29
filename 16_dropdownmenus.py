from tkinter import *
from PIL import ImageTk,Image


# This code will implement sliders

root = Tk()
root.title('Windows')
root.geometry("400x400") # This will define the starting size of the GUI

def show():
    myLabel = Label(root,text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
#clicked.set("Monday")
clicked.set(options[0])


drop = OptionMenu(root,clicked, *options)  # it needs to have a * here
drop.pack()

#user_password = Label(root, text = clicked.get()).place(x = 40,y = 100)
#user_password.pack()

myButton = Button(root,text="Show selection",command=show).pack()

root.mainloop()
