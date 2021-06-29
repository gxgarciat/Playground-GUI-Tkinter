from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


# This code will use message boxes

root = Tk()
root.title('Message Box')

def popup():
    #messagebox.showinfo("This is a popup!", "Hello World!")
    #messagebox.showwarning("This is a popup!", "Hello World!")
    #messagebox.showerror("This is a popup!", "Hello World!")
    #messagebox.askquestion("This is a popup!", "Hello World!")
    #messagebox.askokcancel("This is a popup!", "Hello World!")
    response = messagebox.askyesno("This is a popup!", "Hello World!")
     Label(root,text=response).pack() # This will print the result after pressing the button
    if response == 1:
        Label(root,text="You click Yes!").pack()
    else:
        Label(root,text="You click No!").pack()


Button(root,text="Popup",command=popup).pack()


root.mainloop()
