# ======== Creating Notepad by self ==========
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('500x300')
root.title('Notepad')
mainmenu = Menu(root)


def aa():
    q = tmsg.askyesno('Save', 'Do you save this file')
    if q == YES:
        with open("Tkinter.txt", "a") as f:
            f.write(text.get('1.0', 'end'))
        text.delete('1.0', 'end')
    else:
        text.delete('1.0', 'end')


def bb():
    with open("Tkinter.txt", "r") as f:
        text.insert('insert', f.read())


def cc():
    with open("Tkinter.txt", "a") as f:
        f.write(text.get('1.0', 'end'))


def dd():
    global omk
    omk = text.selection_get()


def ee():
    global omk
    omk = text.selection_get()
    start = text.index('sel.first')
    end = text.index('sel.last')
    text.delete(start, end)


def ff():
    text.insert('insert', omk)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

submenu1 = Menu(mainmenu, tearoff=0)
submenu1.add_command(label='New', command=aa)
submenu1.add_command(label='Open', command=bb)
submenu1.add_command(label='Save', command=cc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=submenu1)

submenu1 = Menu(mainmenu, tearoff=0)
submenu1.add_command(label='Copy', command=dd)
submenu1.add_command(label='Cut', command=ee)
submenu1.add_command(label='Paste', command=ff)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit', menu=submenu1)

root.mainloop()
