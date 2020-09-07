# Handling Events in Tkinter
from tkinter import *
root = Tk()
def omkar(event):
    print(f"You clicked once at {event.x}, {event.y}")

root.title("EVENT in Tkinter")
root.geometry("1000x600")
widget = Button(root, text="Click me Please")
widget.pack()
widget.bind("<Button-1>", omkar)
widget.bind("<Double-1>", quit)

root.mainloop()
