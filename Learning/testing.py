import tkinter as tk

window = tk.Tk()
window.title("Hangman")
window.geometry("500x500")

greeting = tk.Label(text="Welcome to Hangman!")
greeting.pack()

guess = tk.Entry()
guess.pack()

window.mainloop()