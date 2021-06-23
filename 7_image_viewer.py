from tkinter import *
from PIL import ImageTk,Image


# This will display images and icon

root = Tk()
root.title("Image viewer")

# Importing images is a 3 step process here.
# Images taken from google - chairs
# Images are scaled here with resize method

my_img1 = Image.open("image1.jpg")
my_img1 = my_img1.resize((800,600),Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(my_img1)

my_img2 = Image.open("image2.jpg")
my_img2 = my_img2.resize((800,600),Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open("image3.jpg")
my_img3 = my_img3.resize((800,600),Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(my_img3)

my_img4 = Image.open("image4.jpg")
my_img4 = my_img4.resize((800,600),Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(my_img4)

my_img5 = Image.open("image5.jpg")
my_img5 = my_img5.resize((800,600),Image.ANTIALIAS)
my_img5 = ImageTk.PhotoImage(my_img5)

# List of Images
image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

# Implementing status bar
status = Label(root,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

# Showing images
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

# Adding functions
def left(image_number):
    global my_label
    global buttonleft
    global buttonright

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    buttonright = Button(root,text=">>",command=lambda:right(image_number+1))
    buttonleft = Button(root,text="<<",command=lambda:left(image_number-1))

    my_label.grid(row=0,column=0,columnspan=3)
    buttonleft.grid(row=1,column=0)
    buttonright.grid(row=1,column=2)

    if image_number == 1:
        buttonleft = Button(root,text="<<",state=DISABLED)

    status = Label(root,text="Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def right(image_number):
    global my_label
    global buttonleft
    global buttonright

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    buttonright = Button(root,text=">>",command=lambda:right(image_number+1))
    buttonleft = Button(root,text="<<",command=lambda:left(image_number-1))

    if image_number ==5:
        buttonright = Button(root,text=">>",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    buttonleft.grid(row=1,column=0)
    buttonright.grid(row=1,column=2)

    status = Label(root,text="Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)




# Adding functionality with 3 buttons
buttonleft = Button(root,text="<<",command=left,state=DISABLED)
buttonquit = Button(root,text="EXIT",command=root.quit)
buttonright = Button(root,text=">>",command=lambda:right(2))

# Positioning buttons
buttonleft.grid(row=1,column=0)
buttonquit.grid(row=1,column=1)
buttonright.grid(row=1,column=2,pady=10)

# Positioning status bar
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
