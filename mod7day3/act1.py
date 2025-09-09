from tkinter import *

window=Tk()
window.title("Button")
window.geometry('200x200')

def handle_keypress(event):
    print("the key was pressed")
    print(event.char)

window.bind("<Key>",handle_keypress)

def handle_clicked(event):
    print("the button was clicked")

button=Button(text="click me.")

button.pack()

window.bind("<Button-1>",handle_clicked)
window.mainloop()