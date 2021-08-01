from tkinter import *


def motion(x,y):

    if c.coords(ball)[2]<x:
        x_dir=1
    elif c.coords(ball)[2]>x:
        x_dir=-1
    else:
        x_dir=0


    if c.coords(ball)[3]<y:
        y_dir=1
    elif c.coords(ball)[3]>y:
        y_dir=-1
    else:
        y_dir=0


    if c.coords(ball)[2]!=x or c.coords(ball)[3]!=y:
        c.move(ball,x_dir,y_dir)
    if c.coords(ball)[2] != x or c.coords(ball)[3] != y:
        root.after(10,lambda :motion(x,y))



    # if c.coords(ball)[2] < x  :
    #     c.move(ball, 1,1)
    #     root.after(10, lambda: motion(x, y))
    # else:
    #     if c.coords(ball)[2,3] > x:
    #      c.move(ball,-1,-1)
    #     root.after(10, lambda :motion(x,y))

   # if c.coords(ball)[2]<y:
    #    c.move(ball,0,1)
    #    root.after(10,lambda:motion(x,y))


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
#motion()

def func(event):
    print(event.x,event.y)

def click(event):
    x=event.x
    y=event.y
    motion(x+20,y+20)

root.bind('<Motion>',func)
root.bind('<Button-1>',click)

root.mainloop()