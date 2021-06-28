from tkinter import *
from PIL import ImageTk,Image


# This code will insert a frame and it will include buttons

root = Tk()
root.title("Frame testing")

frame = LabelFrame(root,text="This is a frame",padx=5,pady=5)
frame.pack(padx=100,pady=100)

b =  Button(frame,text="Click here!")
b2 = Button(frame,text="...Not here!")
#b.pack() #1st option
b.grid(row=0,column=0)
b2.grid(row=1,column=1)

root.mainloop()
