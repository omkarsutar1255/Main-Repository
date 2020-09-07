from tkinter import *
root = Tk()

def new2():
    root.geometry('1000x500')
    root.update()                  # updates all changes in root
def new():
    global root2
    # root.iconify()       # this create icon of window in taskbar so user can access each window
    root.withdraw()        # whereas withdraw remove window without destroy it
    root2 = Toplevel()
    root2.geometry('500x400+120+120')
    label = Button(root2, text='desr', command=reopen)
    label.pack()
def reopen():
    root2.destroy()
    root.update()
    root.deiconify()
root.geometry('500x400+120+120')
label = Button(root, text='omkar', command=new)
label.pack()

label2 = Button(root, text='new button', command=new2)
label2.pack()


root.mainloop()
