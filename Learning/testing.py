from tkinter import *

root = Tk()

root.title("Testing")
root.geometry("400x400")

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="black")
myButton.pack()

root.mainloop()
