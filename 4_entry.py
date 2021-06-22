from tkinter import *

# Everything on tkinter is based using widgets
# The program will expand depending on the content

root = Tk()


# For this, an entry widget will be required
e = Entry(root,width=50,borderwidth=5)
e.pack()
# This will get the event from clicking the Button. It needs to be inside of the function
# e.get()

# This will insert a message in the entry box
e.insert(0,"Enter your name: ")

# Defining events that will occur when pressing the  Button
def myClick():
    fetching = e.get()
    myLabel = Label(root,text="Hello " + fetching)
    myLabel.pack()


# This will create a label widget
myButton = Button(root,text="Your name is: ",command=myClick)
myButton.pack()

# This will keep it as a loop
root.mainloop()
