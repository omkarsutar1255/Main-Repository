from tkinter import *             # to avoid tkinter.modulename and directly import any modulename
from PIL import Image, ImageTk

root = Tk(screenName=None, baseName=None, className='Tk',
                 useTk=1, sync=0, use=None)
# gui logic here

root.geometry("644x434")                            # giving width and height to gui window
root.minsize(400, 300)                              # setting minimum size to gui window
root.maxsize(1200, 600)                              # setting maximum size to gui window

# photo = PhotoImage(file="gui.png")                  # setting .png file to a variable as photoimage

image = Image.open("C:\\Users\\dell\\Omkar Programme\\Python Files\\IMG_1586.JPG")
# opening jpg file and assign it to a variable
photo = ImageTk.PhotoImage(image)                    # converting jpg file to Tkinter supporting photoimage

omkar = Label(image=photo)                           # for use photoimage variable as label
# omkar = Label(text="WELCOME TO PYCHARM IDE")
omkar.pack()                                        # .pack to connecting label to gui window


root.mainloop(n=0)



