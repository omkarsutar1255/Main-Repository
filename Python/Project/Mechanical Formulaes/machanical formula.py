from tkinter import *
import tkinter.messagebox as tmsg
from math import sqrt, pi, ceil


def calculation(sin):
    global value3
    outputvalue1.delete(0, END)
    if sin == "add":
        value3 = float(inputvalue1.get()) + float(addvalue1.get())
    elif sin == "sub":
        value3 = float(inputvalue1.get()) - float(addvalue1.get())
    elif sin == "mul":
        value3 = float(inputvalue1.get()) * float(addvalue1.get())
    elif sin == "did":
        value3 = float(inputvalue1.get()) / float(addvalue1.get())
    else:
        print("enter correct option")
    outputvalue1.insert(0, value3)


def addition():
    calculation("add")


def subtractiion():
    calculation("sub")


def multiplication():
    calculation("mul")


def division():
    calculation("did")


def clear():
    inputvalue1.delete(0, END)
    addvalue1.delete(0, END)
    outputvalue1.delete(0, END)


def resto2():
    root2.destroy()
    m3()


def formulafunc(sign, funna):
    global root2, inputvalue, addvalue, outputvalue, inputvalue1, addvalue1, outputvalue1
    root2 = Tk()
    window(root2)
    inputvalue = IntVar()
    addvalue = IntVar()
    outputvalue = IntVar()
    root4.destroy()
    f6 = Frame(root2, width=650, height=384)
    f7 = Frame(root2, width=650, height=50)
    lt = Label(f6, text="Addition formula", fg="black", font=("REVAMPED", 15, "bold"))
    lt.pack(side=TOP, padx=9, pady=9)

    inputvalue1 = Entry(f6, textvariable=inputvalue, font=("REVAMPED", 15, "bold"), justify='right')
    addvalue1 = Entry(f6, textvariable=addvalue, font=("REVAMPED", 15, "bold"), justify='right')
    outputvalue1 = Entry(f6, textvariable=outputvalue, font=("REVAMPED", 15, "bold"), justify='right')
    inputvalue1.place(x=100, y=100)
    addvalue1.place(x=100, y=150)
    outputvalue1.place(x=100, y=200)

    l2 = Label(f6, text=sign, fg="black", font=("REVAMPED", 15, "bold"))
    l2.place(x=205, y=125)

    l3 = Label(f6, text="=", fg="black", font=("REVAMPED", 15, "bold"))
    l3.place(x=205, y=175)

    Button(f7, text="OK", command=funna, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    Button(f7, text="clear", command=clear, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    Button(f7, text="Back", command=resto2, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    f6.pack(side=TOP, fill=BOTH, expand=True)
    f7.pack(side=BOTTOM, fill=BOTH, expand=False)
    root2.mainloop()


def add():
    formulafunc("+", addition)


def sub():
    formulafunc("-", subtractiion)


def mul():
    formulafunc("*", multiplication)


def did():
    formulafunc("/", division)


def formulaname():
    pass

def putvalue(line, x, y):
    l12 = Label(f6, text=line, fg="black", font=("REVAMPED", 10, "bold"))
    l12.place(x=x, y=y)

def roor():
    root5.destroy()
    cotter()


def omcal():
    force1applied = float(force1.get())
    Nf1applied = float(Nf1.get())
    Sytss1applied = float(Sytss1.get())
    Sycss1applied = float(Sycss1.get())
    Sysss1applied = float(Sysss1.get())
    Sytc1applied = float(Sytc1.get())

    stss = Sytss1applied / Nf1applied
    scss = (Sytss1applied * Sycss1applied) / Nf1applied
    tss = (Sytss1applied * Sysss1applied) / Nf1applied
    stc = Sytc1applied / Nf1applied
    scc = (Sytc1applied * Sycss1applied) / Nf1applied
    tc = (Sytc1applied * Sysss1applied) / Nf1applied
    d = ceil(sqrt((force1applied / stss) * (4 / pi))) + 4
    t = ceil(0.3 * d)
    l1 = (t * (4 / pi)) / 2
    l2 = sqrt((-l1) ** 2 + 4 * (force1applied / stss) * (4 / pi)) / 2
    l3 = [l1 - l2, l1 + l2]
    d1s = max(l3)
    d1c = force1applied / (scc * t)
    d1 = ceil(max([d1s, d1c]))
    d2 = ceil(sqrt((4 * force1applied) / (pi * scss) + d1 ** 2))
    t1 = ceil(force1applied / (pi * d1 * tss))
    a = ceil(force1applied / (2 * d1 * tss))
    h1 = (4 * t) / pi
    h2 = sqrt(h1 ** 2 + 4 * ((d1 ** 2) - ((d1 * t) * (4 / pi)) + (force1applied / stss) * (4 / pi)))
    D1 = ceil(max([(h1 + h2) / 2, (h1 - h2) / 2]))
    D2 = ceil((force1applied / (scc * t)) + d1)
    c = ceil(force1applied / (2 * tss * (D2 - d1)))
    b1 = force1applied / (2 * t * tc)
    b2 = sqrt((6 * ((D2 / 2) * (((D2 - d1) / 6) + (d1 / 4)))) / (t * stc))
    b = ceil(max([b1, b2]))

    global root5, f6, f7
    root5 = Tk()
    window(root5)
    root3.destroy()
    f6 = Frame(root5, width=650, height=384, bg="blue")
    f7 = Frame(root5, width=650, height=50, bg="green")
    lt = Label(f6, text="Cotter Joint", fg="black", font=("REVAMPED", 15, "bold"))
    lt.pack(side=TOP, padx=9, pady=9)
    putvalue(f"Sigma tension for spigot and socket = {stss} N/mm^2", 5, 40)
    putvalue(f"Sigma Compression for Spigot and Socket = {scss} N/mm^2", 5, 60)
    putvalue(f"Sigma Shear for Spigot and Socket = {tss} N/mm^2", 5, 80)
    putvalue(f"Sigma tension in cotter = {stc} N/mm^2", 5, 100)
    putvalue(f"Sigma compression in cotter = {scc} N/mm^2", 5, 120)
    putvalue(f"Sigma Shear for cotter = {tc} N/mm^2", 5, 140)
    putvalue(f"Diameter of Rod(d) = {d}", 5, 160)
    putvalue(f"Thickness of cotter(t) = {t}", 5, 180)
    putvalue(f"Diameter of Spigot(d1) = {d1}", 5, 200)
    putvalue(f"Diameter of Spigot collar(d2) = {d2}", 5, 220)
    putvalue(f"Sigma Shear for cotter = {t1} N/mm^2", 5, 240)
    putvalue(f"Sigma Shear for cotter = {a} N/mm^2", 5, 260)
    putvalue(f"Outside diameter of socket(D1) = {D1}", 5, 280)
    putvalue(f"Diameter of socket collar(D2) = {D2}", 5, 300)
    putvalue(f"Thickness of socket(c) = {c}", 5, 320)
    putvalue(f"Width of cotter(b) = {b}", 5, 340)

    Button(f7, text="Back", command=roor, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)

    f6.pack(side=TOP, fill=BOTH, expand=True)
    f7.pack(side=BOTTOM, fill=BOTH, expand=False)
    root5.mainloop()


def resto3():
    root3.destroy()
    mdn()

def clear1():
    force1.delete(0, END)
    Nf1.delete(0, END)
    Sytss1.delete(0, END)
    Sycss1.delete(0, END)
    Sysss1.delete(0, END)
    Sytc1.delete(0, END)

def cotter1():
    root4.destroy()
    cotter()

def cotter():
    global root3, force, Nf, Sytss, Sycss, Sysss, Sytc, force1, Nf1, Sytss1, Sycss1, Sysss1, Sytc1
    root3 = Tk()
    window(root3)
    force = IntVar()
    Nf = IntVar()
    # todo: Socket and Spigot
    Sytss = IntVar()
    Sycss = IntVar()
    Sysss = IntVar()

    # todo: Cotter
    Sytc = IntVar()

    f6 = Frame(root3, width=650, height=384)
    f7 = Frame(root3, width=650, height=50)
    lt = Label(f6, text="Cotter Joint", fg="black", font=("REVAMPED", 15, "bold"))
    lt.pack(side=TOP, padx=9, pady=9)

    l12 = Label(f6, text="Force   = ", fg="black", font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=35)

    l12 = Label(f6, text="Factor of Safety   = ", fg="black", font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=70)

    l12 = Label(f6, text="Yield Strength in Tension for Socket and Spigot = ", fg="black", font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=105)

    l12 = Label(f6, text="Yield Strength percentage in Compression\nfor Socket and Spigot = ", fg="black",
                font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=140)

    l12 = Label(f6, text="Yield Strength percentage in Shear\nfor Socket and Spigot = ", fg="black",
                font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=210)

    l12 = Label(f6, text="Yield Strength in Tension for Cotter = ", fg="black",
                font=("REVAMPED", 15, "bold"))
    l12.place(x=5, y=280)

    force1 = Entry(f6, textvariable=force, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    Nf1 = Entry(f6, textvariable=Nf, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    Sytss1 = Entry(f6, textvariable=Sytss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    Sycss1 = Entry(f6, textvariable=Sycss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    Sysss1 = Entry(f6, textvariable=Sysss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    Sytc1 = Entry(f6, textvariable=Sytc, font=("REVAMPED", 15, "bold"), justify='right', width=15)
    force1.place(x=150, y=35)
    Nf1.place(x=250, y=70)
    Sytss1.place(x=500, y=105)
    Sycss1.place(x=430, y=160)
    Sysss1.place(x=400, y=230)
    Sytc1.place(x=400, y=280)

    Button(f7, text="OK", command=omcal, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    Button(f7, text="clear", command=clear1, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    Button(f7, text="Back", command=resto3, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    f6.pack(side=TOP, fill=BOTH, expand=True)
    f7.pack(side=BOTTOM, fill=BOTH, expand=False)
    root3.mainloop()


def knuckle():
    pass


def turnbuckle():
    pass


def okclick(a, b, c, d):
    value = list1.curselection()
    if len(value) == 0:
        tmsg.showinfo("Error", "Select one of formulas")
    elif value[0] == 0:
        a()
    elif value[0] == 1:
        b()
    elif value[0] == 2:
        c()
    elif value[0] == 3:
        d()
    else:
        print("select one of option")


def okclick8():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick7():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick6():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick5():
    okclick(cotter1, knuckle, turnbuckle, formulaname)


def okclick4():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick3():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick2():
    okclick(formulaname, formulaname, formulaname, formulaname)


def okclick1():
    okclick(add, sub, mul, did)


def restore():
    root4.destroy()
    mainupper()


def subjects(list6, okcommand):
    global root4, list1
    root4 = Tk()
    window(root4)
    f6 = Frame(root4, width=650, height=384, bg="blue")
    f7 = Frame(root4, width=650, height=50, bg="green")

    lt = Label(f6, text="Formulas", fg="black", font=("REVAMPED", 15, "bold"))
    lt.pack(side=TOP, padx=9, pady=9)

    scrollbar = Scrollbar(f6)  # Scroll bar on root assign to scrollbar variable
    scrollbar.pack(side=RIGHT, fill=Y)
    list1 = Listbox(f6, height=10, font=("REVAMPED", 15, "bold"), yscrollcommand=scrollbar.set)
    n = 0
    u = list6
    for i in u:
        n += 1
        list1.insert(n, i)
    list1.pack(side=TOP, fill=BOTH, expand=True)
    scrollbar.config(command=list1.yview)
    Button(f7, text="OK", command=okcommand, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    Button(f7, text="Back", command=restore, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
    f6.pack(side=TOP, fill=BOTH, expand=True)
    f7.pack(side=BOTTOM, fill=BOTH, expand=False)
    root4.mainloop()


def tom():
    subjects(["Add", "tom", "Formulas"], okclick8)


def apm():
    subjects(["Add", "apm", "Formulas"], okclick7)


def mqc():
    subjects(["Add", "mqc", "Formulas"], okclick6)


def mdn():
    subjects(["Cotter Joint", "Knuckle Joint", "Turn Buckle"], okclick5)


def ht():
    subjects(["Add", "ht", "Formulas"], okclick4)


def thermo():
    subjects(["Add", "thermo", "Formulas"], okclick3)


def fm():
    subjects(["Add", "FM", "Formulas"], okclick2)


def m3():
    subjects(["Addition", "Subtraction", "Multiplication", "Divide"], okclick1)


def new_com(j):
    root.destroy()
    j()


def new_col8():
    new_com(tom)


def new_col7():
    new_com(apm)


def new_col6():
    new_com(mqc)


def new_col5():
    new_com(mdn)


def new_col4():
    new_com(ht)


def new_col3():
    new_com(thermo)


def new_col2():
    new_com(fm)


def new_col1():
    new_com(m3)


def mainfunc(mm, mech, aa=None, bb=None, cc=None, dd=None, ee=None, ff=None, gg=None, hh=None):
    submenu1 = Menu(mm, tearoff=0)
    mm.add_cascade(label=mech, menu=submenu1)
    submenu1.add_command(label=aa, command=new_col1)
    submenu1.add_command(label=bb, command=new_col2)
    submenu1.add_command(label=cc, command=new_col3)
    submenu1.add_command(label=dd, command=new_col4)
    submenu1.add_command(label=ee, command=new_col5)
    submenu1.add_command(label=ff, command=new_col6)
    submenu1.add_command(label=gg, command=new_col7)
    submenu1.add_command(label=hh, command=new_col8)
    root.config(menu=mm)


def window(a):
    a.geometry('800x400+120+120')
    a.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')


def mainupper():
    global root
    root = Tk()
    window(root)
    mainmenu = Menu(root)
    label1 = Label(root, text="Welcome to Sharad Institute of technology", font=("REVAMPED", 20, "bold"))
    label1.pack(side=TOP, pady=10)
    mainfunc(mainmenu, 'Mechanical', 'Engineering Mathematics-III', 'Fluid Mechanics', 'Thermodynamics',
             'Heat Transfer', 'Machine Design-1', 'Metrology and Quality Control', 'Applied Thermodynamics',
             'Theory of machine-2')
    mainfunc(mainmenu, 'Electrical')
    mainfunc(mainmenu, 'Civil')
    mainfunc(mainmenu, 'Computer')
    mainfunc(mainmenu, 'Metallurgy')
    root.mainloop()


if __name__ == '__main__':
    mainupper()
