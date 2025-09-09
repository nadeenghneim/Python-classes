from tkinter import *
from tkinter import messagebox


window=Tk()
window.title("Button")
window.geometry('200x200')

def msg():
    messagebox.showwarning("ALERT","Virus detected!!")

button=Button(window,text="Scan for viruses",command=msg)
button.place(x=50,y=80)
window.mainloop()