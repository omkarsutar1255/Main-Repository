from tkinter import *
root = Tk()
root.geometry("1000x600")
def getvals():
    print("submitting form")
    # Getting entered values by user and printing it on console
    print(f"{namevalue.get(), numbervalue.get(), foodservicevalue.get()}")
    print('submitted')

    with open("Tkinter.txt", "a") as f:                # Creating file to save information in it
        # Getting user entered values and write them in files
        f.write(f"{namevalue.get(), numbervalue.get(), foodservicevalue.get()}\n")
Label(root, text="welcome to kolhapur", font='normal 18 bold', pady=15).grid(row=0, column=3)
name = Label(root, text="Name", font='Arial 13 bold')
number = Label(root, text="MOBILE", font='Arial 13 bold')
name.grid(row=1, column=2)
number.grid(row=2, column=2)
namevalue = StringVar()
numbervalue = StringVar()
foodservicevalue = IntVar()
nameentry = Entry(root, textvariable=namevalue)
numberentry = Entry(root, textvariable=numbervalue)
nameentry.grid(row=1, column=3)
numberentry.grid(row=2, column=3)
foodservice = Checkbutton(text="want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=3, column=3)
Button(text="submit to omkar travel", command=getvals).grid(row=4, column=3)

root.mainloop()
