# =========== MENU AND SUBMENU IN TKINTER ===========
from tkinter import *
import tkinter.messagebox as tmsg  # tkinter have message box for user interaction

root = Tk()
root.geometry('800x400')
root.title('Pycharm')


def myfunc():
    print('omkar sutar')


def help1():
    a = tmsg.askquestion("Exit", 'want to exit')  # asking question to user in yes no way
    if a == 'yes':
        msg = "what went wrong"
    else:
        msg = 'Enjoy the experience'
    tmsg.showinfo("info", msg)  # show information to user


def sss():
    ans = tmsg.askretrycancel("sss", "want to have friendship")  # asking question to user in retry and cancel way
    if ans:
        print("retry krte raho")
    else:
        print("good cancel kr diya")


def skk():
    ans = tmsg.askyesnocancel("sss", "want to have friendship")  # asking question to user in yes, no and cancel way
    if ans == True:
        print("well done bhava")
    elif ans == False:
        print("ky kelas bhava")
    else:
        print("kuch toh kr bhava")


def oadsjf():
    tmsg.showerror('Error', 'Failed the process')


def adslfj():
    tmsg.showwarning('Warning', 'your data will be deleted')


# create space for main menu in horizontal bar
mainmenu = Menu(root)

# Use this to create main menu without submenu in gui
mainmenu.add_command(label='Print omakr', command=myfunc)
mainmenu.add_command(label='Exit', command=quit)
root.config(menu=mainmenu)

# create submenu in mainmenu
submenu3 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="help", menu=submenu3)
submenu3.add_command(label='help', command=help1)
submenu3.add_command(label='befriend', command=sss)
submenu3.add_command(label='new feature', command=skk)
submenu3.add_command(label='error', command=oadsjf)    # error messagebox
submenu3.add_command(label='warning', command=adslfj)  # warning messagebox
root.config(menu=mainmenu)

root.mainloop()
