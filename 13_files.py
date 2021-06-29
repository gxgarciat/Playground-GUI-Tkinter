from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

# This code will open files using a dialog

root = Tk()
root.title('Windows')



def open():
    global my_image

    root.filename = filedialog.askopenfilename(initialdir = "/home/gxgarciat/Documents/Tkinter",title = "Select a file",filetypes= (("jpeg files","*.jpg"),("all files","*.*")))
    # Showing the result after clicking the image
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()



my_button = Button(root,text="Open file",command=open).pack()

root.mainloop()
