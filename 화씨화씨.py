from tkinter import *

def f2c():
    f = float(e1.get())
    c = (f-32)*5/9
    e2.delete(0, END)
    e2.insert(0, str(c))

def c2f():
    c = float(e2.get())
    f = (c*(9/5))+32
    e1.delete(0, END)
    e1.insert(0, str(f))

win = Tk()
win.title('화씨/섭씨 변환')

label1 = Label(win, text = "   화씨")
label2 = Label(win, text = "   섭씨")
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)

e1 = Entry(win, width=15)
e2 = Entry(win, width=15)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(win, text = " 화씨 → 섭씨 ", command=f2c)
b2 = Button(win, text = " 섭씨 → 화씨 ", command=c2f)
b1.grid(row = 2, column = 1)
b2.grid(row = 3, column = 1)

win.mainloop()
