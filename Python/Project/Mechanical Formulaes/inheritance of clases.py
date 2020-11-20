from tkinter import *
import tkinter.messagebox as tmsg
from math import sqrt, pi, ceil


class Otherformulas:
    def formulaname(self):
        pass


class Cotter:
    @staticmethod
    def putvalue(line, x, y):
        l12 = Label(f6, text=line, fg="black", font=("REVAMPED", 10, "bold"))
        l12.place(x=x, y=y)

    def roor(self):
        root5.destroy()
        self.cotter()

    def omcal(self):
        force1applied = float(force1.get())
        nf1applied = float(Nf1.get())
        sytss1applied = float(Sytss1.get())
        sycss1applied = float(Sycss1.get())
        sysss1applied = float(Sysss1.get())
        sytc1applied = float(Sytc1.get())

        stss = sytss1applied / nf1applied
        scss = (sytss1applied * sycss1applied) / nf1applied
        tss = (sytss1applied * sysss1applied) / nf1applied
        stc = sytc1applied / nf1applied
        scc = (sytc1applied * sycss1applied) / nf1applied
        tc = (sytc1applied * sysss1applied) / nf1applied
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
        root5.geometry('1000x500+120+120')
        root5.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')
        root3.destroy()
        f6 = Frame(root5, width=650, height=384, bg="blue")
        f7 = Frame(root5, width=650, height=50, bg="green")
        lt = Label(f6, text="Cotter Joint", fg="black", font=("REVAMPED", 15, "bold"))
        lt.pack(side=TOP, padx=9, pady=9)
        self.putvalue(f"Sigma tension for spigot and socket = {stss} N/mm^2", 5, 40)
        self.putvalue(f"Sigma Compression for Spigot and Socket = {scss} N/mm^2", 5, 60)
        self.putvalue(f"Sigma Shear for Spigot and Socket = {tss} N/mm^2", 5, 80)
        self.putvalue(f"Sigma tension in cotter = {stc} N/mm^2", 5, 100)
        self.putvalue(f"Sigma compression in cotter = {scc} N/mm^2", 5, 120)
        self.putvalue(f"Sigma Shear for cotter = {tc} N/mm^2", 5, 140)
        self.putvalue(f"Diameter of Rod(d) = {d} mm", 5, 160)
        self.putvalue(f"Thickness of cotter(t) = {t} mm", 5, 180)
        self.putvalue(f"Diameter of Spigot(d1) = {d1} mm", 5, 200)
        self.putvalue(f"Diameter of Spigot collar(d2) = {d2} mm", 5, 220)
        self.putvalue(f"Sigma Shear for cotter = {t1} N/mm^2", 5, 240)
        self.putvalue(f"Sigma Shear for cotter = {a} N/mm^2", 5, 260)
        self.putvalue(f"Outside diameter of socket(D1) = {D1} mm", 5, 280)
        self.putvalue(f"Diameter of socket collar(D2) = {D2} mm", 5, 300)
        self.putvalue(f"Thickness of socket(c) = {c} mm", 5, 320)
        self.putvalue(f"Width of cotter(b) = {b} mm", 5, 340)

        Button(f7, text="Back", command=self.roor, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)

        f6.pack(side=TOP, fill=BOTH, expand=True)
        f7.pack(side=BOTTOM, fill=BOTH, expand=False)
        root5.mainloop()

    def resto3(self):
        root3.destroy()
        self.mdn()

    @staticmethod
    def clear1():
        force1.delete(0, END)
        Nf1.delete(0, END)
        Sytss1.delete(0, END)
        Sycss1.delete(0, END)
        Sysss1.delete(0, END)
        Sytc1.delete(0, END)

    def cotter1(self):
        root4.destroy()
        self.cotter()

    def cotter(self):
        global root3, force, Nf, Sytss, Sycss, Sysss, Sytc, force1, Nf1, Sytss1, Sycss1, Sysss1, Sytc1
        root3 = Tk()
        root3.geometry('1000x500+120+120')
        root3.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')
        force = IntVar()
        Nf = IntVar()
        # todo: Socket and Spigot
        Sytss = IntVar()
        Sycss = IntVar()
        Sysss = IntVar()

        # todo: Cotter
        Sytc = IntVar()

        f36 = Frame(root3, width=650, height=384)
        f37 = Frame(root3, width=650, height=50)
        lt = Label(f36, text="Cotter Joint", fg="black", font=("REVAMPED", 15, "bold"))
        lt.pack(side=TOP, padx=9, pady=9)

        l12 = Label(f36, text="Force   = ", fg="black", font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=35)

        l12 = Label(f36, text="Factor of Safety   = ", fg="black", font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=70)

        l12 = Label(f36, text="Yield Strength in Tension for Socket and Spigot = ", fg="black",
                    font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=105)

        l12 = Label(f36, text="Yield Strength percentage in Compression\nfor Socket and Spigot = ", fg="black",
                    font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=140)

        l12 = Label(f36, text="Yield Strength percentage in Shear\nfor Socket and Spigot = ", fg="black",
                    font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=210)

        l12 = Label(f36, text="Yield Strength in Tension for Cotter = ", fg="black",
                    font=("REVAMPED", 15, "bold"))
        l12.place(x=5, y=280)

        force1 = Entry(f36, textvariable=force, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        Nf1 = Entry(f36, textvariable=Nf, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        Sytss1 = Entry(f36, textvariable=Sytss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        Sycss1 = Entry(f36, textvariable=Sycss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        Sysss1 = Entry(f36, textvariable=Sysss, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        Sytc1 = Entry(f36, textvariable=Sytc, font=("REVAMPED", 15, "bold"), justify='right', width=15)
        force1.place(x=150, y=35)
        Nf1.place(x=250, y=70)
        Sytss1.place(x=500, y=105)
        Sycss1.place(x=430, y=160)
        Sysss1.place(x=400, y=230)
        Sytc1.place(x=400, y=280)

        Button(f37, text="OK", command=self.omcal, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        Button(f37, text="clear", command=self.clear1, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        Button(f37, text="Back", command=self.resto3, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        f36.pack(side=TOP, fill=BOTH, expand=True)
        f37.pack(side=BOTTOM, fill=BOTH, expand=False)
        root3.mainloop()


class Knuckle:
    def knuckle(self):
        pass


class TurnBuckle:
    def turnbuckle(self):
        pass


class Forsuppor:
    @staticmethod
    def clear():
        inputvalue1.delete(0, END)
        addvalue1.delete(0, END)
        outputvalue1.delete(0, END)

    def resto2(self):
        root2.destroy()
        self.m3()

    @staticmethod
    def calculation(sin):
        global value3
        try:
            outputvalue1.delete(0, END)
            if sin == "add":
                value3 = int(inputvalue1.get()) + int(addvalue1.get())
            elif sin == "sub":
                value3 = int(inputvalue1.get()) - int(addvalue1.get())
            elif sin == "mul":
                value3 = int(inputvalue1.get()) * int(addvalue1.get())
            elif sin == "did":
                value3 = int(inputvalue1.get()) / int(addvalue1.get())
            else:
                print("enter correct option")
        except (ImportError, ValueError, NameError, RuntimeError, TypeError, ZeroDivisionError):
            value3 = "Error"
        outputvalue1.insert(0, value3)

    def formulafunc(self, sign, funna):
        global root2, inputvalue, addvalue, outputvalue, inputvalue1, addvalue1, outputvalue1
        root2 = Tk()
        root2.geometry('1000x500+120+120')
        root2.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')
        inputvalue = IntVar()
        addvalue = IntVar()
        outputvalue = IntVar()
        root4.destroy()
        f26 = Frame(root2, width=650, height=384)
        f27 = Frame(root2, width=650, height=50)
        lt = Label(f26, text="Addition formula", fg="black", font=("REVAMPED", 15, "bold"))
        lt.pack(side=TOP, padx=9, pady=9)

        inputvalue1 = Entry(f26, textvariable=inputvalue, font=("REVAMPED", 15, "bold"), justify='right')
        addvalue1 = Entry(f26, textvariable=addvalue, font=("REVAMPED", 15, "bold"), justify='right')
        outputvalue1 = Entry(f26, textvariable=outputvalue, font=("REVAMPED", 15, "bold"), justify='right')
        inputvalue1.place(x=100, y=100)
        addvalue1.place(x=100, y=150)
        outputvalue1.place(x=100, y=200)

        l2 = Label(f26, text=sign, fg="black", font=("REVAMPED", 15, "bold"))
        l2.place(x=205, y=125)

        l3 = Label(f26, text="=", fg="black", font=("REVAMPED", 15, "bold"))
        l3.place(x=205, y=175)

        Button(f27, text="OK", command=funna, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        Button(f27, text="clear", command=self.clear, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        Button(f27, text="Back", command=self.resto2, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        f26.pack(side=TOP, fill=BOTH, expand=True)
        f27.pack(side=BOTTOM, fill=BOTH, expand=False)
        root2.mainloop()


class AdditionFormula(Forsuppor):
    def addition(self):
        self.calculation("add")

    def add(self):
        self.formulafunc("+", self.addition)


class SubtractionFormula(Forsuppor):
    def subtractiion(self):
        self.calculation("sub")

    def sub(self):
        self.formulafunc("-", self.subtractiion)


class MultiplicationFormula(Forsuppor):
    def multiplication(self):
        self.calculation("mul")

    def mul(self):
        self.formulafunc("*", self.multiplication)


class DivisionFormula(Forsuppor):
    def division(self):
        self.calculation("did")

    def did(self):
        self.formulafunc("/", self.division)


class Subject(AdditionFormula, SubtractionFormula, MultiplicationFormula, DivisionFormula, Cotter, Knuckle, TurnBuckle,
              Otherformulas):
    @staticmethod
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

    def okclick8(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick7(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick6(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick5(self):
        self.okclick(self.cotter1, self.knuckle, self.turnbuckle, self.formulaname)

    def okclick4(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick3(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick2(self):
        self.okclick(self.formulaname, self.formulaname, self.formulaname, self.formulaname)

    def okclick1(self):
        self.okclick(self.add, self.sub, self.mul, self.did)

    def restore(self):
        root4.destroy()
        self.mainupper()

    def subjects(self, list6, okcommand):
        global root4, list1
        root4 = Tk()
        root4.geometry('1000x500+120+120')
        root4.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')
        f16 = Frame(root4, width=650, height=384, bg="blue")
        f17 = Frame(root4, width=650, height=50, bg="green")

        lt = Label(f16, text="Formulas", fg="black", font=("REVAMPED", 15, "bold"))
        lt.pack(side=TOP, padx=9, pady=9)

        scrollbar = Scrollbar(f16)  # Scroll bar on root assign to scrollbar variable
        scrollbar.pack(side=RIGHT, fill=Y)
        list1 = Listbox(f16, height=10, font=("REVAMPED", 15, "bold"), yscrollcommand=scrollbar.set)
        n = 0
        u = list6
        for i in u:
            n += 1
            list1.insert(n, i)
        list1.pack(side=TOP, fill=BOTH, expand=True)
        scrollbar.config(command=list1.yview)
        Button(f17, text="OK", command=okcommand, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        Button(f17, text="Back", command=self.restore, font=("REVAMPED", 13, "bold")).pack(side=LEFT, padx=9, pady=9)
        f16.pack(side=TOP, fill=BOTH, expand=True)
        f17.pack(side=BOTTOM, fill=BOTH, expand=False)
        root4.mainloop()

    def tom(self):
        self.subjects(["Add", "tom", "Formulas"], self.okclick8)

    def apm(self):
        self.subjects(["Add", "apm", "Formulas"], self.okclick7)

    def mqc(self):
        self.subjects(["Add", "mqc", "Formulas"], self.okclick6)

    def mdn(self):
        self.subjects(["Cotter Joint", "Knuckle Joint", 'Turn Buckle'], self.okclick5)

    def ht(self):
        self.subjects(["Add", "ht", "Formulas"], self.okclick4)

    def thermo(self):
        self.subjects(["Add", "thermo", "Formulas"], self.okclick3)

    def fm(self):
        self.subjects(["Add", "FM", "Formulas"], self.okclick2)

    def m3(self):
        self.subjects(["Addition", "Subtraction", "Multiplication", "Divide"], self.okclick1)


class MainRoot(Subject):
    @staticmethod
    def new_com(j):
        root.destroy()
        j()

    def new_col8(self):
        self.new_com(self.tom)

    def new_col7(self):
        self.new_com(self.apm)

    def new_col6(self):
        self.new_com(self.mqc)

    def new_col5(self):
        self.new_com(self.mdn)

    def new_col4(self):
        self.new_com(self.ht)

    def new_col3(self):
        self.new_com(self.thermo)

    def new_col2(self):
        self.new_com(self.fm)

    def new_col1(self):
        self.new_com(self.m3)

    def mainfunc(self, mm, mech, aa=None, bb=None, cc=None, dd=None, ee=None, ff=None, gg=None, hh=None):
        submenu1 = Menu(mm, tearoff=0)
        mm.add_cascade(label=mech, menu=submenu1)
        submenu1.add_command(label=aa, command=self.new_col1)
        submenu1.add_command(label=bb, command=self.new_col2)
        submenu1.add_command(label=cc, command=self.new_col3)
        submenu1.add_command(label=dd, command=self.new_col4)
        submenu1.add_command(label=ee, command=self.new_col5)
        submenu1.add_command(label=ff, command=self.new_col6)
        submenu1.add_command(label=gg, command=self.new_col7)
        submenu1.add_command(label=hh, command=self.new_col8)
        root.config(menu=mm)

    def mainupper(self):
        global root
        root = Tk()
        root.geometry('1000x500+120+120')
        root.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')
        root.configure(bg="white")
        mainmenu = Menu(root)
        label1 = Label(root, text="\n       Welcome to Sharad Institute of technology,       \n"
                                  "College of Engineering, Ichalkaranji\n",
                       font=("REVAMPED", 20, "bold"), bg="green", fg="white", bd=10, relief=RIDGE)
        label1.pack(side=TOP, pady=10)
        photo2 = PhotoImage(file="C:\\Users\\dell\\Omkar Programme\\Python Files\\sharad institute2.png")
        omka = Label(image=photo2)
        omka.pack(side=TOP, pady=10)
        self.mainfunc(mainmenu, 'Mechanical', 'Engineering Mathematics', 'Fluid Mechanics', 'Thermodynamics',
                      'Heat Transfer', 'Machine Design-1', 'Metrology and Quality Control', 'Applied Thermodynamics',
                      'Theory of machine-2')
        self.mainfunc(mainmenu, 'Electrical', 'Electro-Magnetism', 'Control System',
                      'Electricity Technology and Machines',
                      'Circuit Analysis, Electronics', 'Electrical Engineering Material', 'Transmission & Distribution',
                      'Instrumentation', 'Microprocessor interfacing')
        self.mainfunc(mainmenu, 'Civil', 'Surveying in Civil Engineering', 'Strength of Material or Solid Mechanics',
                      'Building Material and Construction Technology', 'Geology in Civil Engineering',
                      'Concrete Technology in Civil Engineering',
                      'Structural Analysis', 'Building Planning and Drawing', 'Design and Drawing of RCC Structures')
        self.mainfunc(mainmenu, 'Computer', 'Engineering Mathematics', 'Electronic Circuits', 'Logic Design',
                      'Discreate Mathematical Structures', 'Data Structure with C', 'Object-Oriented Programming',
                      'Data structure', 'Electronic circuits and logic Design')
        self.mainfunc(mainmenu, 'Metallurgy', 'Physical Metallurgy', 'Thermodynamics of Meta',
                      'Fluid Mechanics of Meta',
                      'Foundry Technology', 'Steel Making', 'Iron Making', 'Transport phenomena', 'Extraction of Metal')
        root.mainloop()


if __name__ == '__main__':
    Mechanical = MainRoot()
    Mechanical.mainupper()
