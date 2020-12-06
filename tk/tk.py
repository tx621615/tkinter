from tkinter import *

window = Tk()
window.title('my window')
window.geometry('400x400')  # 400*400大小
label1 = Label(window, text="welcom to Python", bg='white', font=('Arial', 12), width=15, height=2)
label1.place(x=200, y=200)  # 400以内即可


def moveleft(l):
    l.place(x=1, y=1)


button1 = Button(window, text='<=', width=15, height=2, command=moveleft(label1))
button1.place(x=100, y=100)
window.mainloop()