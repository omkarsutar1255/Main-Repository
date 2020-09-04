from tkinter import *
root = Tk()
from tkinter import ttk
def print1():
    value = combo.get()
    print(value)
v = ['C++', 'C#', 'Python']
# v = list(range(1, 19))               # we can give list of number to combobox
combo = ttk.Combobox(root, values=v, width=15, height=5)
# Combobox show list of item in scrolling way
# height is how many item can show at a time and width is how many character can add in one line
combo.set('select')
combo.pack()
button = Button(root, text="print", command=print1).pack()
root.mainloop()
