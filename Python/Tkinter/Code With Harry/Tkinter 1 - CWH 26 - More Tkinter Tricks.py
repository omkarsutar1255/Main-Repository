from tkinter import *
root = Tk()
root.geometry('1000x400')
root.title('Omkar - Title of my GUI')
# root.wm_iconbitmap('1.ico')              # if we have ico format file then we can set it to tile pic
root.configure(background="grey")          # background color of gui
width = root.winfo_screenwidth()           # getting info about screen width and height
height = root.winfo_screenheight()
print(f'{width}x{height}')
Button(text='Close', command=root.destroy).pack()       # exit function for gui

root.mainloop()
