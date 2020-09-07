from tkinter import *
import datetime
from view_people import Mypeople
date = datetime.datetime.now().date()
date = str(date)


class Application(object):  # inheritance from object is by default in python 3
    def __init__(self, master):
        self.master = master  # this allow to use master in other def function as self.master

        # Frame
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        # top frame design in frame
        self.top_image = PhotoImage(file='C:\\Users\\dell\\Omkar Programme\\Python Files\\newimage.png')
        self.top_image_label = Label(self.top, image=self.top_image)  # giving image as label on it
        self.top_image_label.place(x=130, y=25)

        # heading design in frame
        self.heading = Label(self.top, text='My Phonebook App', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=230, y=60)

        # date design in frame
        self.date_lbl = Label(self.top, text="Date : " + date, font='arial 12 bold', fg='#ebb434', bg='white')
        self.date_lbl.place(x=450, y=110)

        # View people button
        self.viewbutton = Button(self.bottom, text=' My People ', font='arial 12 bold', fg='white', bg='black',
                                 command=self.my_people)
        self.viewbutton.place(x=250, y=70)

        # Add people button
        self.addbutton = Button(self.bottom, text='Add People', font='arial 12 bold', fg='white', bg='black')
        self.addbutton.place(x=250, y=130)

        # About us
        self.aboutbutton = Button(self.bottom, text='  About Us  ', font='arial 12 bold', fg='white', bg='black')
        self.aboutbutton.place(x=250, y=190)

    def my_people(self):
        people = Mypeople()


def main():
    root = Tk()
    app = Application(root)
    root.title('Passbook App')
    root.geometry('650x550+350+200')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
