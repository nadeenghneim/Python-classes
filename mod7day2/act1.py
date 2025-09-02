from tkinter import *

window=Tk()
window.title("tkinter widget practice")
window.geometry("200x300")

set=[[1,2,3],[4,5,6],[7,8,9],['#',0,'*']]

for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)

for i in range(4):
    for j in range(3):
        frame=Frame(master=window,relief=RAISED,borderwidth=4,bg='pink')
        frame.grid(row=i,column=j,sticky='nsew')
        label=Label(master=frame,text=set[i][j],bg='white',font=('arial',20))
        label.pack(expand=True,fill='both',padx=5,pady=5)


window.mainloop()