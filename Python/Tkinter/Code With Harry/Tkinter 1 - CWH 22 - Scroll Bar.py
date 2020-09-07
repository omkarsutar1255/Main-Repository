# ========== Scroll Bar For Widget ===========
from tkinter import *
root = Tk()
root.geometry('500x300')
root.title('Scroll Bar')
# for connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)          # Scroll bar on root assign to scrollbar variable
scrollbar.pack(side=RIGHT, fill=Y)   # position of scrollbar in widget

listbox = Listbox(root, yscrollcommand=scrollbar.set)    # giving scrollbar to text widget scrollcommand
for i in range(344):
    listbox.insert(END, f'Item {i}')
listbox.pack(fill='both', padx=22)
scrollbar.config(command=listbox.yview)  # giving scrollbar listbox.yview(y direction scroll in listbox)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()
