from tkinter import *

# Everything on tkinter is based using widgets
# The program will expand depending on the content

root = Tk()

# Defining events that will occur when pressing the  Button
def myClick():
    myLabel = Label(root,text="You have clicked the button!")
    myLabel.pack()


# This will create a label widget
#myButton = Button(root,text="Click here")
# padx will size the button
#myButton = Button(root,text="Click here", padx=50, pady=50)
#myButton = Button(root,text="Click here", command=myClick) #  command does not use ()
myButton = Button(root,text="Click here", command=myClick,fg="blue",bg="green") #  giving color to buttons

# This will create a disbled Button
# myButton = Button(root,text="Click here",state=DISABLED)

myButton.pack()

# This will keep it as a loop
root.mainloop()
