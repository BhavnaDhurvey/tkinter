from tkinter import *

win = Tk()
win.title("master")
# win.iconbitmap('icon.ico')
# win.geometry('600*300')
win.maxsize(width=600,height=200)
win.maxsize(width=600,height=200)



def func():
    x=var.get()
    print(x)
    lbl.config(text=x,bg="green")


lbl=Label(win,text="user Name",bg="red",fg="white")
lbl.place(x=10,y=10)

bl=Label(win,text="nothing",bg="red",fg="white")
lbl.place(x=40,y=120)


var=StringVar()
ent=Entry(win,bg="red",fg='white',bd=5, textvariable=var,width=30)
ent.place(x=80,y=10)



btn=Button(win,text="submit",bg='green',command=func)
btn.place(x=10,y=60)

win. mainloop()