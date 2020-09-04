from tkinter import *
root = Tk()

class Mybutton:
    def __init__(self, master):  # master used as root in class
        self.printbutton = Button(master, text='print', command=self.printbutton)
        # when have to call function within class then use self in both like used in printbutton function
        self.printbutton.pack()
        self.Quitbutton = Button(master, text='quit', command=master.quit)
        # when have to call function from tk=root=master then call master like used in quit command
        self.Quitbutton.pack()
    def printbutton(self):  # creating fucntion within class
        print('printing message')
root = Tk()  # root have all inheritance of Tkinter
b = Mybutton(root)  # b have all inheritance of root and mybutton class

# sticky parameter
name = Label(root, text='Name')
pas = Label(root, text='passworddddd')
name.grid(row=0, sticky=E)                     # sticky enable text slide left or right in a grid
pas.grid(row=1)

b = Frame(root, width=300, height=300)                    # we can give frames to bind with command
b = Button(root, text='oakr', command=deffunction)        # neglect command if bind button to it
b.bind('<Button1>', deffunction).pack()
# instead of giving command in button we can bind any button for any function (add event in function)

def delete():
    sel = lbx.curselection()
    for i in sel:
        lbx.delete(i)
def callme():
    sel = lbx.curselection()  # curselection give index value of selected item
    for i in sel:             # retrieve each index number
        print(lbx.get(i))     # getting values of selected index
lbx = Listbox(root, width=30, height=15, selectmode=EXTENDED)
# list box takes width(i.e.how many character in one line) and height (i.e.how many items can add to listbox)
# Valid resource names: background, bd, bg, borderwidth, cursor, exportselection, fg, font, foreground, height,
# highlightbackground, highlightcolor, highlightthickness, relief, selectbackground, selectborderwidth,selectforeground,
# selectmode=BROWSE/SINGLE/MULTIPLE/EXTENDED, setgrid, takefocus, width, xscrollcommand, yscrollcommand, listvariable.
lbx.insert(1, 'python')    # takes index and name to insert in listbox
lbx.insert(2, 'Java')
lbx.insert(3, 'C++')
lbx.insert(4, 'PHP')
lbx.pack()
button = Button(root, text='print', command=callme).pack()
delete_button = Button(root, text="Delete", command=delete).pack()

from tkinter import ttk
def print1():
    value = combo.get()
    print(value)
v = ['C++', 'C#', 'Python']
# v = list(range(1, 19))               # we can give list of number to combobox
combo = ttk.Combobox(root, values=v, width=15, height=5)
# Combobox show list of item in scrolling way 
# height is how many item can show at a time and width is how many character can add in one line
combo.set('select')
combo.pack()
button = Button(root, text="print", command=print1).pack()

from tkinter import font
fonts = list(font.families())            # all font families in list
for item in fonts:                       # retrieve all families form list
    print(item)
    
from tkinter.font import Font
my_font = Font(family='Ink Free', size=16, weight='bold', slant='italic', underline=1, overstrike=1)
# this enable to give multiple arguments regarding to font for labels in gui
label = Label(root, text='Omkar Sutar', font=my_font).pack()


def printme():
    result = text.selection_get()     # getting selected text and assign it to variable
    pos = text.search(result, 1.0, stopindex=END)       # retrieving index position of that text
    print(pos)
text = Text(root, width=20, height=20, wrap=WORD, padx=10, pady=10, bd=5, selectbackground='grey', font='InkFree 10 bold')
text.pack()
# text widget takes width(number of letters in line), height(number of lines), wrap(divide type),
# padx and pady(staring distance from x and y), bd = border size, selectbackground(back color when select lines)
text.insert(INSERT, "welcome omkar")             # giving already wrote text in text widget
button = Button(root, text='print', command=printme).pack()

# programme on search engine wikipedia
import wikipedia  
def getme():
    answer.delete(1.0, END)
    entryvalue = entry.get()
    try:
        answervalue = wikipedia.summary(f'{entryvalue}')
        answer.insert(INSERT, answervalue)
    except:
        answer.insert(INSERT, 'Please check spelling correction or internet connection')
topframe = Frame(root)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text='search', command=getme)
button.pack()
topframe.pack()
botton = Frame(root)
scroll = Scrollbar(botton)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(botton, width=100, height=100, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
botton.pack()

# creating popup window in gui
from tkinter import simpledialog
def getme():
    value = simpledialog.askstring('INPUT STRING', 'Please Enter Your Name')
# we can also get askinteger and askfloat
    print(value)
button = Button(root, text='Popup', command=getme)
button.pack()

# creating multiple window in gui
def openwindow():    # opening second window using Toplevel()
     root2 = Toplevel()          # root2 use as new window's root   
     root2.title("top_window")
     root2.geometry('500x300+120+120')
     button1 = Button(root2, text='close', command=root2.destroy)
     button1.pack()
button = Button(root, text='open window', command=openwindow)
button.pack()

# spinbox are used for getting number from user like getting 5 for 5 pizza
def printme():
    print(spin1.get())
spin1 = Spinbox(root, from_=1, to=5)   # use from_ for from
spin1.pack()
button = Button(root, text="print", command=printme).pack()

frame = LabelFrame(root, text='Input', padx=5, pady=5)     # creating frame and giving it label
entry = Entry(frame).pack()
frame.pack()

from tkinter import filedialog
# open file from MY PC in gui
def open_file():              
    abc = filedialog.askopenfile(initialdir='F:\Omkar', title='select file', filetypes=(('text files', '.txt'), ('all files', '*.*')))
    print(abc)
    for c in abc:                   # reading text files from directory
        print(c)
    abc.close()
button = Button(root, text='open file', command=open_file)
button.pack()

from tkinter import filedialog
# saving file in MY PC
def save_file():
    f = filedialog.asksaveasfile(mode='w', title='select file', defaultextension='.txt')
    if f is None:
        return
    f.write('hellooooooo')
    f.close()
button = Button(root, text='save file', command=save_file)
button.pack()

# getting custom RBG color code and # color code
from tkinter import colorchooser
def callme():
    clr = colorchooser.askcolor(title='select color')
    print(clr)
    root.config(background=clr[1])                 # fetching chose color as background of root
button = Button(root, text="change color", command=callme).pack()

# bind keyboard button for function call
def call_me(event=''):
    print('omkar')
root.bind('<Control-c>', call_me)          # key button can use on root or frame
button = Button(root, text='click here', command=call_me)  # click button use on widgets, button, root and frames
button.pack()

root.geometry('500x300+120+120')          # +120+120 is location for gui
root.mainloop()
