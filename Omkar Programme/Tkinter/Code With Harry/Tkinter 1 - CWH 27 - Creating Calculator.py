from tkinter import *
root = Tk()
root.geometry('500x600')
root.title('Calculator by Omkar')
def click(event):
    global scvalue
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == 'C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvar=scvalue, font='lucida 35 bold')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


def aa(j, g, h, p):
    global f
    f = Frame(root, bg="grey")
    bb(j)
    bb(g)
    bb(h)
    bb(p)
    f.pack()
def bb(a):
    global f
    b = Button(f, text=a, padx=20, pady=5, font='lucida 25 bold')
    b.bind('<Button-1>', click)
    b.pack(side=LEFT, padx=20, pady=5)

aa('C', '/', '*', '-')
aa('7', '8', '9', '+')
aa('4', '5', '6', '+')
aa('1', '2', '3', '=')
aa('0', '0', '.', '=')

root.mainloop()
