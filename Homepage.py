from tkinter import *
from math import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Syntax Error"

        scvalue.set(value)
        screen.update()

    elif text == "!":
        text = event.widget.cget("text")
        print(text)
        if scvalue.get().isdigit():
            value = int(scvalue.get())
            value = eval('factorial(value)')
            scvalue.set(value)
            screen.update()


    elif text == "\u221A":
        text = event.widget.cget("text")
        print(text)
        if scvalue.get().isdigit():
            value = int(scvalue.get())
            a = eval('sqrt(value)')
            scvalue.set(a)
            screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("480x455")
root.title("Calculator")
# root.wm_iconbitmap()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, fg='gray10', bg='Cadet blue', textvar=scvalue, font="Times 40 bold",)
screen.pack(fill=X, ipadx=8, ipady=10, pady=5)

f1 = Frame(root, bg="dark grey")
b1 = Button(f1, text="9", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure',  bg='dark slate grey')
b1.pack(side=LEFT, padx=4, pady=1)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="8", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b2.pack(side=LEFT, padx=4, pady=1)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="7", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b3.pack(side=LEFT, padx=4, pady=1)
b3.bind("<Button-1>", click)

b4 = Button(f1, text="+", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='cyan4')
b4.pack(side=LEFT, padx=4, pady=1)
b4.bind("<Button-1>", click)

b5 = Button(f1, text="AC", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='indian red')
b5.pack(side=LEFT, padx=4, pady=1)
b5.bind("<Button-1>", click)

f1.pack()

f2 = Frame(root, bg="dark grey")
b1 = Button(f2, text="6", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b1.pack(side=LEFT, padx=4, pady=1)
b1.bind("<Button-1>", click)

b2 = Button(f2, text="5", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b2.pack(side=LEFT, padx=4, pady=1)
b2.bind("<Button-1>", click)

b3 = Button(f2, text="4", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b3.pack(side=LEFT, padx=4, pady=1)
b3.bind("<Button-1>", click)

b4 = Button(f2, text="-", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='cyan4')
b4.pack(side=LEFT, padx=4, pady=1)
b4.bind("<Button-1>", click)

b5 = Button(f2, text="\u221A", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='turquoise3')
b5.pack(side=LEFT, padx=4, pady=1)
b5.bind("<Button-1>", click)

f2.pack()

f3 = Frame(root, bg="dark grey")
b1 = Button(f3, text="3", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b1.pack(side=LEFT, padx=4, pady=1)
b1.bind("<Button-1>", click)

b2 = Button(f3, text="2", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b2.pack(side=LEFT, padx=4, pady=1)
b2.bind("<Button-1>", click)

b3 = Button(f3, text="1", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b3.pack(side=LEFT, padx=4, pady=1)
b3.bind("<Button-1>", click)

b4 = Button(f3, text="*", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure',bg='cyan4')
b4.pack(side=LEFT, padx=4, pady=1)
b4.bind("<Button-1>", click)

b5 = Button(f3, text="**", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='turquoise3')
b5.pack(side=LEFT, padx=4, pady=1)
b5.bind("<Button-1>", click)

f3.pack()

f4 = Frame(root, bg="dark grey")
b1 = Button(f4, text=".", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='aquamarine4')
b1.pack(side=LEFT, padx=4, pady=1)
b1.bind("<Button-1>", click)

b2 = Button(f4, text="0", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='dark slate grey')
b2.pack(side=LEFT, padx=4, pady=1)
b2.bind("<Button-1>", click)

b3 = Button(f4, text="=", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='aquamarine4')
b3.pack(side=LEFT, padx=4, pady=1)
b3.bind("<Button-1>", click)

b4 = Button(f4, text="/", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure',bg='cyan4')
b4.pack(side=LEFT, padx=4, pady=1)
b4.bind("<Button-1>", click)

b5 = Button(f4, text="!", padx=15, pady=5, font="Times 30 bold", height=1, width=2, fg='azure', bg='turquoise3')
b5.pack(side=LEFT, padx=4, pady=1)
b5.bind("<Button-1>", click)

f4.pack()

root.mainloop()
