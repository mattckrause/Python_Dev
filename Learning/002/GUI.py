#https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/

from tkinter import *

root = Tk()

root.title("HangMan")
root.geometry("800x800")

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="black")
myButton.pack()

root.mainloop()