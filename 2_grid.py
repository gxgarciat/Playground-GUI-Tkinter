from tkinter import *

# Everything on tkinter is based using widgets
# The program will expand depending on the content

root = Tk()

# This will create a label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Guillermo")

# When using grid, instead of packing, we use the grid method
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

# Tests
# Position will be relative. If the window does not find anything
# among the column 1-4, it will look like myLabel2 is positioned at
# the same level.

#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=5)

# As python is OOP, the 4 lines of code can be replaced by:
#myLabel1 = Label(root, text="Hello World").myLabel1.grid(row=0,column=0)
#myLabel2 = Label(root, text="My name is Guillermo").myLabel2.grid(row=1,column=0)

# This will keep it as a loop
root.mainloop()
