from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("creating a news paper")
root.geometry("644x434")
root.minsize(400, 300)
root.maxsize(1200, 600)

om = Label(text="FIRST PHOTO FROM ADITYA MUNJ", bg="green", fg="white", font=("Ink Free", 20, "bold"),
           bd=5, relief=RIDGE)
om.pack(side=LEFT, anchor="n", padx=5, pady=5)

om2 = Label(text="SECOND PHOTO FROM ADITYA MUNJ", bg="green", fg="white", font=("Ink Free", 15, "bold"),
           bd=5, relief=RIDGE).place(x=600, y=1)

image = Image.open("IMG_1586.JPG")
photo = ImageTk.PhotoImage(image)
omkar = Label(image=photo).place(x=1, y=100)

photo2 = PhotoImage(file="imgae.png")
omka = Label(image=photo2).place(x=600, y=60)

root.mainloop()
