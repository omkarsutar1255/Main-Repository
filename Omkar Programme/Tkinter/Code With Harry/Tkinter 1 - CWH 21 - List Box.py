# ========== ListBox ===========
from tkinter import *
root = Tk()
root.geometry('500x300')
root.title('ListBox')
def add():
    global i
    lbx.insert(ACTIVE, f'{i}')        # insert i value above active item in listbox
    i += 1
i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, 'First item of our listbox')        # item set at end in listbox
Button(root, text='Add Item', command=add).pack()

root.mainloop()

