from tkinter import *

window = Tk()
window.title('my window')
window.geometry('200x200')  # 400*400大小
var1 = StringVar()  # lable中变量动态表示
l = Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()



def print_selection():
    value = lb.get(lb.curselection())  # 获得光标位置的值
    var1.set(value)


b1 = Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

var2 = StringVar()
var2.set((11,22,33,44))  # 用变量设置列表的初始值--元组
lb = Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)  # 动态插入列表值
lb.insert(1, 'first')   #索引插入删除值
lb.insert(2, 'second')
lb.delete(2)
lb.pack()
window.mainloop()
