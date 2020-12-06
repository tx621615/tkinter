from tkinter import *

window = Tk()
window.title('my window')
window.geometry('650x200')  # 400*400大小
l = Label(window, width=15,text='Welcome')
l.place(x=250, y=100)
var = StringVar()
i = 250
j = 0
def set_color():
    l.config(bg=var.get())

def move_left():
    global i
    i -= 50
    l.place(x=i)

def move_right():
    global i
    i = i + 50
    l.place(x=i)

r1 = Radiobutton(window, text='Red', variable=var, value='red', command=set_color)  # 将variable对应变量设置为value
r2 = Radiobutton(window, text='Yellow', variable=var, value='yellow', command=set_color)  # 将variable对应变量设置为value
r3 = Radiobutton(window, text='White', variable=var, value='white', command=set_color)  # 将variable对应变量设置为value
r4 = Radiobutton(window, text='Gray', variable=var, value='gray', command=set_color)  # 将variable对应变量设置为value
r5 = Radiobutton(window, text='Green', variable=var, value='green', command=set_color)  # 将variable对应变量设置为value
r1.place(x=100, y=10)
r2.place(x=200, y=10)
r3.place(x=300, y=10)
r4.place(x=400, y=10)
r5.place(x=500, y=10)

b1 = Button(window, text='<=', width=4, height=2, command=move_left)
b1.place(x=275, y=150)

b1 = Button(window, text='>=', width=4, height=2, command=move_right)
b1.place(x=325, y=150)

window.mainloop()
