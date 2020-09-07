# =========== MENU AND SUBMENU IN TKINTER ===========
from tkinter import *
root = Tk()
root.geometry('800x400')
root.title('Pycharm')

def myfunc():
    print('omkar sutar')

# create space for main menu in horizontal bar
mainmenu = Menu(root)

# Use this to create main menu without submenu in gui
mainmenu.add_command(label='Print omakr', command=myfunc)
mainmenu.add_command(label='Exit', command=quit)
root.config(menu=mainmenu)

# creating first sub menu
submenu1 = Menu(mainmenu, tearoff=0)                       # create space for sub menu in main menu
mainmenu.add_cascade(label='File', menu=submenu1)          # giving label to main menu and assign it sub menu
submenu1.add_command(label='save', command=myfunc)         # add command in spaces of sub menu with label
submenu1.add_separator()                                   # separate two sub menu adding line between them
submenu1.add_command(label='new project', command=myfunc)  # add command in spaces of sub menu with label
root.config(menu=mainmenu)                                 # showing main menu on screen

# creating second sub menu
submenu2 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='Edit', menu=submenu2)
# creating cascade(can add multiple command) in mainmenu as submenu then various command are added to submenu
submenu2.add_command(label='Cut', command=myfunc)
# add command show option in cascade so when we click on it command execute
submenu2.add_separator()
submenu2.add_command(label='Copy', command=myfunc)
root.config(menu=mainmenu)


root.mainloop()
