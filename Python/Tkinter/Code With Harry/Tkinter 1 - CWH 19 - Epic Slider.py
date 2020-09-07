# =========== Slider =========== #
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('500x300')
root.title("slider tutorial")


def getmoney():
    tmsg.showinfo("credit balance", f'we have credited {myslider2.get()} rupees to your dollar')

myslider = Scale(root, to=200, length=250, width=10, sliderlength=50)         # slider that can slide upto 200
# lenght of slider is 250 and width of slider can be adjusted and we can set length of slider
myslider.place(x=20, y=20)             # placing slider in x and y coordinate

Label(root, text="how many rupees do you want").pack()
myslider2 = Scale(root, orient=VERTICAL, to=300,  tickinterval=100)  # silder that can slide horizontal and vertically
# tickinterval are show every 100th number upto 300 at after slider
myslider2.set(30)                       # set slider initially at 30
myslider2.pack(side=RIGHT, fill=Y)
Button(root, text="get money", pady=10, command=getmoney).pack()  # button to perform function after click on it

root.mainloop()
