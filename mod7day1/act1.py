from tkinter import *
from datetime import date
window=Tk()
window.title("learning tkinter")
window.geometry("500x300")

label=Label(text="Helloo!!",fg="red",bg="white",height=2,width=10)
name_label=Label(text="Name",bg='purple')
name_entry=Entry()

def display():
    name=name_entry.get()
    global message 
    message="you are using tkinter,\ntoday's date is:"
    greeting="Welcome "+name+"\n"

    text_box.insert(END,greeting)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
button=Button(text="enter",command=display,bg="pink",fg="orange",height=2)
label.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()
window.mainloop()
