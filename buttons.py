from tkinter import *

win = Tk()
win.geometry('500x500')

def color_change():
    if var.get() == 0:
        Label['bg'] ='red'
    elif var.get() == 1:
        Label['bg'] ='blue'
    elif var.get() == 2:
        Label['bg'] ='green'


def func():
    if var.get()== 0:

     print('red')
     if chk_var.get() == 0:
      win['bg'] ='red'
    elif var.get()== 1:
     print('blue')
     if chk_var.get() == 0:
      win['bg'] = 'blue'
    elif var.get() == 2:
     print('green')
     if chk_var.get() == 0:
      win['bg'] ='green'




var=IntVar()
var.set(0)
radio_btn_0 = Radiobutton(text='red',variable=var,value=0)
radio_btn_0.pack(anchor=W)
radio_btn_1 = Radiobutton(text='blue',variable=var,value=1)
radio_btn_1.pack(anchor=W)
radio_btn_2 = Radiobutton(text='green',variable=var,value=2)
radio_btn_2.pack(anchor=W)
bnt_1=Button(text="push",command=func).place(x=100,y=100,)

chk_var =BooleanVar()
chk_var.set(0)
chk_btn = Checkbutton(text='сменить цвет фона',variable=chk_var)
chk_btn.place(x=200,y=200)



win.mainloop()
