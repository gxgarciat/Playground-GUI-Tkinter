from tkinter import *

# Everything on tkinter is based using widgets


root = Tk()

# This will create a label widget
myLabel = Label(root, text="Hello World")

# This will pack the widget onto the screen
myLabel.pack()

# This will keep it as a loop
root.mainloop()
