from tkinter import *
root = Tk()
root.geometry("1000x600")
frame = Frame(root, bd=6, bg="blue", relief=RIDGE).place(x=50, y=50, height=37, width=48)
# creating frame giving area and position
b11 = Button(frame, fg='red', text='print').place(x=56, y=56)  # giving button position to press

def hello():             # creating function so when call it by command it will perform action which defined in function
    print('omkar sutar')

frame = Frame(root, bd=6, bg="blue", relief=RIDGE)
frame.pack(side=LEFT, anchor='nw')
b1 = Button(frame, fg='red', text='print', command=hello)  # button are taking command from user to perform functions
b1.pack(side=LEFT, padx=23)
b2 = Button(frame, fg='red', text='print')
b2.pack(side=LEFT, padx=23)
root.mainloop()

# ========= CREATING SMALL CALCULATOR FOR PRACTICE ============
from tkinter import *
root = Tk()
root.geometry('1000x600')
def frame(a, b):
    Frame(root, bd=6, bg="blue", relief=RIDGE).place(x=a, y=b, height=40, width=55)
def a1():
    print("you pressed digit one")
def a2():
    print("you pressed digit Two")
def a3():
    print("you pressed digit Three")
def a4():
    print("you pressed digit Four")
def button(a, b, c, d, e):
    Button(c, fg='red', text=d, height=1, width=4, command=e).place(x=a, y=b)
f1 = frame(50, 50)
f2 = frame(50, 150)
f3 = frame(150, 50)
f4 = frame(150, 150)
b1 = button(56, 56, f1, 1, a1)
b2 = button(156, 56, f2,2, a2)
b3 = button(56, 156, f3, 3, a3)
b4 = button(156, 156, f4, 4, a4)
root.mainloop()
