from tkinter import *
root = Tk(screenName=None, baseName=None, className='Tk',
                 useTk=1, sync=0, use=None)
root.geometry("1200x400")                      # Setting geometry in form of =widthxheight+x+y
root.title("My GUI with Omkar")               # Setting the title of this widget

# Important Label Options
# text - adds the text
# bg - background - setting color to the background
# fg - foreground - setting color for text
# font - sets the font - font takes font style, size and type
# padx - x padding - width of background area
# pady - y padding - height of background area
# relief - border stying = SUNKEN, RAISED, GROOVE, RIDGE, FLAT, SOLID
title_label = Label(text="""
activebackground activeforeground anchor background bitmap borderwidth
cursor disabledforeground font foreground, highlightbackground
highlightcolor highlightthickness image justify padx pady
relief takefocus text textvariable underline wraplength""", bg="green", fg="white", padx=150, pady=200, font=("Ink Free", 25, "bold"), borderwidth=30, relief=RIDGE)

# Important pack options
# anchor - "w" to shift label to west side of screen and similar for other direction
# side - left, right, top, bottom to shift label at any side of direction
# fill - stretching label in whole screen in x or y direction
# padx - left some space around label in x direction
# pady - left some space around label in y direction
title_label.pack(side=BOTTOM, anchor="w", fill=BOTH, padx=20, pady=20)

# placing takes x and y values and place in gui
title_label.place(x=100, y=100)

# grid takes row and column values and set in gui
title_label.grid(row=1, column=2)

root.mainloop()                               # Calling the mainloop of Tk
