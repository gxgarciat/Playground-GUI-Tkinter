from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

# This code will use API and connect to them by Tkinter

root = Tk()

root.title('House Distribution')
root.geometry("500x100") # This will define the starting size of the GUI

def graph():
    house_prices = np.random.normal(20000,25000,5000)
    plt.hist(house_prices,100)
    plt.show()

my_button = Button(root,text="Graph it",command = graph)
my_button.pack()

root.mainloop()
