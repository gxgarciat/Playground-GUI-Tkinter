from tkinter import *
from PIL import ImageTk,Image


# This code will implement sliders

root = Tk()
root.title('Windows')
root.geometry("400x400") # This will define the starting size of the GUI

vertical = Scale(root,from_= 0, to=200)
vertical.pack()

horizontal = Scale(root,from_= 0, to=600,orient=HORIZONTAL)
horizontal.pack()

#my_label = Label(root, text= horizontal.get()).pack()

def slide():
    #my_label = Label(root, text= horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


my_button = Button(root,text="Resize here",command=slide).pack()

root.mainloop()
