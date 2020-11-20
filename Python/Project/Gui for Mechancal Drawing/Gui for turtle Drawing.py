from tkinter import *
import tkinter.messagebox as tmsg
import turtle


def turtle1(a, ly):
    global omk
    try:
        omk.setpos(turtle.pos())
    except:
        omk = turtle.Turtle()
    omk.rt(a)
    omk.fd(ly)
    turtle.mainloop()


def okclick():
    angular = angle.get()
    longitute = length.get()
    turtle1(angular, longitute)


root = Tk()
root.geometry("600x400+120+120")
root.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')

lt1 = Label(root, text="Angle", fg="black", font=("REVAMPED", 15, "bold"))
lt1.place(x=75, y=100)
lt2 = Label(root, text="Length", fg="black", font=("REVAMPED", 15, "bold"))
lt2.place(x=75, y=150)
angle = IntVar()
length = IntVar()
angle.set("")
length.set("")
en1 = Entry(root, textvariable=angle, font=("REVAMPED", 15, "bold"), justify='right')
en2 = Entry(root, textvariable=length, font=("REVAMPED", 15, "bold"), justify='right')
en1.place(x=200, y=100)
en2.place(x=200, y=150)
but1 = Button(root, text="Ok", command=okclick, font=("REVAMPED", 13, "bold"))
but1.place(x=200, y=200)

root.mainloop()
