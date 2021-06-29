from tkinter import *
from PIL import ImageTk,Image

# This code will create windows

root = Tk()
root.title('Windows')

def open():
    global my_img
    global exit_button

    top = Toplevel()
    top.title('Additional Window')

    #labl = Label(top,text="Hi there").pack()

    # Using images in the second window
    my_img = ImageTk.PhotoImage(Image.open("/home/gxgarciat/Documents/Tkinter/image4.jpg"))
    my_label = Label(top,image=my_img).pack()
    #btn2 = Button(top,text="Close window",command=top.destroy).pack()
    exit_button = Button(top, text="Exit", command=top.destroy)
    exit_button.pack(pady=20)


btn = Button(root,text="Open Additional Window",command=open)
btn.pack()



root.mainloop()
