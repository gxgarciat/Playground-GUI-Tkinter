from tkinter import *
from PIL import ImageTk,Image


# This code will implement sliders

root = Tk()
root.title('Windows')
root.geometry("400x400") # This will define the starting size of the GUI

var = IntVar()
chckbox = Checkbutton(root,text="Check here",variable = var)
chckbox.pack()

def show():
    myLabel = Label(root,text=var.get())
    myLabel.pack()


def show2():
    myLabel = Label(root,text=var2.get())
    myLabel.pack()

myButton = Button(root,text="Selection",command=show)
myButton.pack()

myButton2 = Button(root,text="Additional Selection",command=show2)
myButton2.pack()


# This will will do in case on/off is required instead of IntVar
var2 = StringVar()
c2 = Checkbutton(root,text="This is another option",variable=var2,onvalue="On",offvalue="off")
c2.deselect()
c2.pack()


root.mainloop()
