# ========= Creating RadioButtons ===========
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('500x300')
root.title("Radiobutton tutorial")


def order():
    tmsg.showinfo("order received", f"we have received your order for {var.get()}. Thanks for ordering")


Label(root, text="what would you like to have sir?", font='lucida 19 bold', justify=LEFT, padx=14).pack()

# Create frames if want various sets of radiobutton
var = StringVar()
var.set('Dosa')
list1 = ["Dosa", "Idly", "Paratha", "Samosa"]
for i in range(len(list1)):
    radio = Radiobutton(root, text=list1[i], padx=14, variable=var, value=list1[i]).pack(anchor='w')

Button(root, text='Order Now', command=order).pack()

root.mainloop()
