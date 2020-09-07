# Creating gui that takes height and width from user and create gui according that height and width

from tkinter import *
root = Tk()
width = int(input('enter gui width = '))
height = int(input('enter gui height = '))
root.geometry(f'{width}x{height}')


def getvals():
    root.geometry(f'{widthvalue.get()}x{heightvalue.get()}')


Label(root, text='Enter gui value', font="Arial 20 bold", pady=10).grid(row=0, column=1)
width = Label(root, text='Width', font='normal 10 bold', padx=5)
width.grid(row=1, column=0)
height = Label(root, text='Height', font='normal 10 bold', padx=5)
height.grid(row=2, column=0)
widthvalue = IntVar()
heightvalue = IntVar()
widthentry = Entry(root, textvariable=widthvalue)
heightentry = Entry(root, textvariable=heightvalue)
widthentry.grid(row=1, column=1)
heightentry.grid(row=2, column=1)
Button(text="submit to gui width and height", command=getvals).grid(row=3, column=1)
root.mainloop()
