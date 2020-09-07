from tkinter import *
root = Tk()
root.geometry("1000x600")
def getvals():
    print("successfully added")
    print(f'{checkbuttonvalue.get()}')
    print(f'{foodservicevalue.get()}')

# creating Heading of form
Label(root, text="welcome to kolhapur", font='normal 18 bold', pady=15).grid(row=0, column=3)

# creating label of form to be filled
name = Label(root, text="Name", font='Arial 13 bold')
number = Label(root, text="MOBILE", font='Arial 13 bold')
# creating grid(place) for setting label in form
name.grid(row=1, column=2)
number.grid(row=2, column=2)

# setting datatypes of value to be entered in form
namevalue = StringVar()
numbervalue = StringVar()
foodservicevalue = IntVar()        # checkbutton values gives 0 or 1 for offvalue and onvalue
checkbuttonvalue = StringVar()    # we can give string values to checkbutton

# creating value entry box in form
nameentry = Entry(root, textvariable=namevalue)
numberentry = Entry(root, textvariable=numbervalue)
# setting value entry box in form
nameentry.grid(row=1, column=3)
numberentry.grid(row=2, column=3)

# creating checkbox in form
foodservice = Checkbutton(root, text="want to prebook your meals?", variable=foodservicevalue)
# setting grid in form
foodservice.grid(row=3, column=3)

checkbutton = Checkbutton(root, text="getting string value", variable=checkbuttonvalue, offvalue='fail', onvalue='success')
# we can set checkbutton values as offvalues and onvalue
checkbutton.grid(row=4, column=4)

# creating button and assign it a command that will perform functions
Button(root, text="submit to omkar travel", command=getvals).grid(row=4, column=3)

root.mainloop()
