from tkinter import *

window = Tk()
window.title('my window')
window.geometry('200x100')  # 400*400大小
var = StringVar();
label1 = Label(window, textvariable=var, bg='white', font=('Arial', 12), width=15, height=2)
label1.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


button1 = Button(window, text='hit me', width=15, height=2, command=hit_me)
button1.pack()
window.mainloop()