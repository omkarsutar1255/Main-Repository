from tkinter import *
root = Tk()
root.geometry('1000x600')
def getvals():
    print(f"The Username is = {uservalue.get()}")
    print(f"The Password is = {passvalue.get()}")
user = Label(root, text='USERNAME')
password = Label(root, text='PASSWORD')
user.grid()
password.grid(row=1)
# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid(row=3, column=1)

root.mainloop()
