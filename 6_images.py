from tkinter import *
from PIL import ImageTk,Image

import sys, os

# This will display images and icon

root = Tk()
root.title("Expanding GUI")

# With ubuntu, it did not work the icon part
#root.iconbitmap('@/home/gxgarciat/Documents/Tkinter/gdrive.ico')
#root.iconphoto(True, PhotoImage(file="@/home/gxgarciat/Documents/Tkinter/gdrive.ico"))
#root.iconbitmap(os.path.join(sys.path[0], "/home/gxgarciat/Documents/Tkinter/gdrive.ico"))
#root.iconbitmap('~home/gxgarciat/Documents/Tkinter/gdrive.ico')
#root.iconphoto(False, Tk.PhotoImage(file='/home/gxgarciat/Documents/Tkinter/gdrive.ico'))


# Importing images is a 3 step process here.
my_img = ImageTk.PhotoImage(Image.open("googledrive.png"))
my_label = Label(image=my_img)
my_label.pack()

# Adding a quit button
buttonquit = Button(root,text="Exit program",command=root.quit)
buttonquit.pack()

root.mainloop()
