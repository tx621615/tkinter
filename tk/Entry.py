from tkinter import *

window = Tk()
window.title('my window')
window.geometry('200x200')  # 400*400大小
e = Entry(window, show=None)  # None表示显示,具体字符表示密码---'*'
e.pack()


def insert_point():
    var = e.get()  # 获得entry的值
    t.insert('insert', var)   # insert表示在光标处插入

def insert_end():
    var = e.get()
    t.insert('end', var)  # 尾部插入



b1 = Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()

t = Text(window, height=2)
t.pack()

window.mainloop()
