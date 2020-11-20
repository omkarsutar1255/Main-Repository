from tkinter import *
import mysql.connector
import tkinter.messagebox as tmsg


def pack1(rootname, text):
    lablename = Label(rootname, text=text,
                      bg="#eb9234",
                      fg="white",
                      padx=5,
                      pady=5,
                      font=("REVAMPED", 25, "bold"),
                      borderwidth=20,
                      relief=RIDGE)
    lablename.pack(side=TOP, fill="x")


def place(rootname, text, y):
    labelname = Label(rootname, text=text,
                      padx=5,
                      pady=5,
                      font=("REVAMPED", 25, "bold"))
    labelname.place(x=5, y=y)


def toot(a):
    a.geometry("650x434+120+120")
    a.minsize(600, 300)
    a.maxsize(1200, 600)
    a.title("Your passwords")


def upper():
    root4.destroy()
    sutar()


def apple(mycursor1):
    global root4
    root4 = Tk()
    toot(root4)
    u = {}
    for k, c in mycursor1:
        u[k] = c
    f6 = Frame(root4, width=650, height=384, bg="blue")
    f7 = Frame(root4, width=650, height=50, bg="green")

    lt = Label(f6, text="USERNAME : PASSWORD", fg="black", font=("REVAMPED", 15, "bold"))
    lt.pack(side=TOP, anchor=NW, padx=9, pady=9)

    scrollbar = Scrollbar(f6)  # Scroll bar on root assign to scrollbar variable
    scrollbar.pack(side=RIGHT, fill=Y)
    list1 = Listbox(f6, height=10, font=("REVAMPED", 15, "bold"), yscrollcommand=scrollbar.set)
    n = 0
    for i, j in u.items():
        n += 1
        list1.insert(END, f"{n}){i} : {j}")
    list1.pack(side=TOP, fill=BOTH, expand=True)
    scrollbar.config(command=list1.yview)
    Button(f7, text="Back", command=upper, font=("REVAMPED", 13, "bold")).pack(side=TOP, anchor=NW, padx=9, pady=9)
    f6.pack(side=TOP, fill=BOTH, expand=True)
    f7.pack(side=BOTTOM, fill=BOTH, expand=False)
    root4.mainloop()


def getval1():
    mydb1 = mysql.connector.connect(host="localhost", user="root", password="tiger", database="password_saver")
    mycursor1 = mydb1.cursor()
    sqlform = "insert into sub_password(username, password) values(%s, %s)"
    employees = [(uservalue.get(), passvalue.get())]
    mycursor1.executemany(sqlform, employees)
    mydb1.commit()
    tmsg.showinfo('Done', 'Successfully Saved')
    uservalue.set('')
    uservalue1.update()
    passvalue.set('')
    passvalue1.update()


def value(rootname, getvalname):
    global uservalue, passvalue, uservalue1, passvalue1
    uservalue = StringVar()
    passvalue = StringVar()
    uservalue1 = Entry(rootname, textvariable=uservalue, font=("REVAMPED", 15, "bold"))
    passvalue1 = Entry(rootname, textvariable=passvalue, font=("REVAMPED", 15, "bold"))
    uservalue1.place(x=250, y=170)
    passvalue1.place(x=250, y=218)
    Button(rootname, text="Submit", command=getvalname, font=("REVAMPED", 13, "bold")).place(x=300, y=250)


def retrieve():
    mydb1 = mysql.connector.connect(host="localhost", user="root", password="tiger", database="password_saver")
    mycursor1 = mydb1.cursor()
    mycursor1.execute("select * from sub_password")
    root1.destroy()
    apple(mycursor1)


def sutar():
    global root1
    root1 = Tk()
    toot(root1)
    pack1(root1, """Add New Password""")
    place(root1, "Username : ", 150)
    place(root1, "Password : ", 200)
    value(root1, getval1)
    Button(root1, text="Open my Passwords", command=retrieve, font=("REVAMPED", 13, "bold")).place(x=250, y=290)
    root1.mainloop()


def getvals2():
    mydb1 = mysql.connector.connect(host="localhost", user="root", password="tiger", database="password_saver")
    mycursor1 = mydb1.cursor()
    mycursor1.execute("select username from main_password")
    for i in mycursor1:
        if i[0] == uservalue.get():
            mycursor1.execute("select password from main_password")
            for j in mycursor1:
                if j[0] == passvalue.get():
                    root.destroy()
                    sutar()
                else:
                    tmsg.showerror('Error', 'Password not correct')
        else:
            tmsg.showerror('Error', 'Username not correct')


def omkar():
    global root
    root = Tk()
    toot(root)
    pack1(root, """Login ID Password""")
    place(root, "Username : ", 150)
    place(root, "Password : ", 200)
    value(root, getvals2)
    root.mainloop()


def getvals3():
    mydb1 = mysql.connector.connect(host="localhost", user="root", password="tiger", database="password_saver")
    mycursor1 = mydb1.cursor()
    sqlform = "insert into main_password(Username, Password) values(%s, %s)"
    employees = [(uservalue.get(), passvalue.get())]
    mycursor1.executemany(sqlform, employees)
    mydb1.commit()
    tmsg.showinfo('Done', 'Saved Successfully')


try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")
    mycursor = mydb.cursor()
    mycursor.execute("create database password_saver")
    mycursor.execute("use password_saver")
    mycursor.execute("CREATE TABLE main_password("
                     "Username varchar (40) NOT NULL,"
                     "Password varchar (40) NOT NULL);")
    mycursor.execute("CREATE TABLE sub_password("
                     "Username varchar (40) NOT NULL,"
                     "Password varchar (40) NOT NULL);")
    root3 = Tk()
    toot(root3)
    pack1(root3, """welcome
    Create your account""")
    place(root3, "Username : ", 150)
    place(root3, "Password : ", 200)
    value(root3, getvals3)
    root3.mainloop()
    omkar()

except Exception:
    omkar()
