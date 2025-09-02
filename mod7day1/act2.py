from tkinter import *
from PIL import image, imageTk
window=Tk()
window.title("images")
window.geometry("500x300")

image1=image.Open("background.jpg")

image_1=imageTk.PhotoImage(image1)

label=Label(window,image=image_1)
textbox=Text(window,height=3,width=8)
textbox.insert(END,text="you did it!")

label.pack()
textbox.pack()
window.mainloop()