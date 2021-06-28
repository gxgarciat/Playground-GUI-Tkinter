from tkinter import *
from PIL import ImageTk,Image


# This code will use radio buttons

root = Tk()
root.title("Radio Buttons")

r = IntVar() # It will collect what has been stored in this variable
# In case it is a string, it should be StrVar()
r.set("2")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushrooms","Mushrooms"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root,text=text,variable=pizza,value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
#Radiobutton.pack()

#myLabel = Label(root,text=pizza.get())
#myLabel.pack()

myButton = Button(root,text="Click here",command=lambda:clicked(pizza.get()))
myButton.pack()

root.mainloop()
