# ========== Status Bar ===========
from tkinter import *
root = Tk()
root.geometry('500x300')
root.title('status bar')

def upload():
    statusvar.set('Busy..')   # after run upload function statusbar changes to busy..
    sbar.update()             # now statusbar is update to busy..
    import time
    time.sleep(2)
    statusvar.set('Ready Now')     # after 2 sec again statusbar set to ready now

statusvar = StringVar()
statusvar.set('Ready')             # first setting statusbar as ready
sbar = Label(root, textvariable=statusvar, relief=RIDGE, anchor='w')
sbar.pack(side=BOTTOM, fill=X)
Button(root, text='Upload', command=upload).pack()

root.mainloop()
