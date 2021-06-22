from tkinter import *

# This will display a calculator on the screen
# This calculator only carries out SUM

root = Tk()
root.title("Simplified calculator")


# For this, an entry widget will be required
e = Entry(root,width=40,borderwidth=5)
# e.pack()
e.grid(row=0,column=0,columnspan=3)

# This will get the event from clicking the Button. It needs to be inside of the function
# e.get()

# This will insert a message in the entry box
#e.insert(0,"Enter your name: ")

# Defining events that will occur when pressing the  Button
def buttonclick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def buttonclear():
    e.delete(0,END)


def buttonadd():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def buttonsubs():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0,END)

def buttonmult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def buttondiv():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

def buttonequal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0,f_num + int(second_number))
    if math == "substraction":
        e.insert(0,f_num - int(second_number))
    if math == "multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "division":
        e.insert(0,f_num / int(second_number))



# This will create & position buttons
myButton1 = Button(root,text=" 1 ",padx=40,pady=40,command=lambda:buttonclick(1))
myButton1.grid(row=3,column=0)
myButton2 = Button(root,text=" 2 ",padx=40,pady=40,command=lambda: buttonclick(2))
myButton2.grid(row=3,column=1)
myButton3 = Button(root,text=" 3 ",padx=40,pady=40,command=lambda: buttonclick(3))
myButton3.grid(row=3,column=2)
myButton4 = Button(root,text=" 4 ",padx=40,pady=40,command=lambda: buttonclick(4))
myButton4.grid(row=2,column=0)
myButton5 = Button(root,text=" 5 ",padx=40,pady=40,command=lambda: buttonclick(5))
myButton5.grid(row=2,column=1)
myButton6 = Button(root,text=" 6 ",padx=40,pady=40,command= lambda: buttonclick(6))
myButton6.grid(row=2,column=2)
myButton7 = Button(root,text=" 7 ",padx=40,pady=40,command= lambda: buttonclick(7))
myButton7.grid(row=1,column=0)
myButton8 = Button(root,text=" 8 ",padx=40,pady=40,command= lambda: buttonclick(8))
myButton8.grid(row=1,column=1)
myButton9 = Button(root,text=" 9 ",padx=40,pady=40,command= lambda: buttonclick(9))
myButton9.grid(row=1,column=2)
myButton0 = Button(root,text=" 0 ",padx=40,pady=40,command= lambda: buttonclick(0))
myButton0.grid(row=4,column=0)
myButtonplus = Button(root,text=" + ",padx=38,pady=40,command= buttonadd)
myButtonplus.grid(row=5,column=0)
myButtonsubs = Button(root,text=" - ",padx=40,pady=40,command= buttonsubs)
myButtonsubs.grid(row=6,column=0)
myButtonmult = Button(root,text=" * ",padx=40,pady=40,command= buttonmult)
myButtonmult.grid(row=6,column=1)
myButtondiv = Button(root,text=" / ",padx=40,pady=40,command= buttondiv)
myButtondiv.grid(row=6,column=2)
myButtonequal = Button(root,text=" = ",padx=89,pady=40,command=buttonequal)
myButtonequal.grid(row=4,column=1,columnspan=2)
myButtonclear = Button(root,text="Clear",padx=87,pady=40,command= buttonclear)
myButtonclear.grid(row=5,column=1,columnspan=2)

# This will keep it as a loop
root.mainloop()
