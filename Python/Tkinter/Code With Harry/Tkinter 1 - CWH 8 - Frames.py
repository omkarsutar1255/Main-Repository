from tkinter import *
root = Tk()
root.geometry("1000x600")
f1 = Frame(root, bg="blue", bd=6, relief=RIDGE)   # creating frames means cutting root in pieces
f1.pack(side=LEFT, fill="y", pady=50)

f2 = Frame(root, bg="green", bd=6, relief=RIDGE)
f2.pack(side=TOP, fill="x")

lt = Label(f1, text="Tkinter Project - Pycharm", bg="green", fg="white")  # adding labels not in root bt in frame
lt.pack(padx=20, pady=20)

lt = Label(f2, text="welcome to sublime", bg="blue", fg="white") # this label in second frame so used f2 instead of root
lt.pack(padx=20, pady=9)

root.mainloop()
