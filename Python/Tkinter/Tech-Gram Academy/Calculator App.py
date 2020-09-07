from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('380x550+200+100')
root.resizable(False, False)  # user can not resize window of calculator


def enternumber(x):
    all_text = entry.get()
    last_char = all_text[-1:]
    if entry.get() == '0':
        if x == '.':
            entry.insert(1, '.')
        else:
            entry.delete(0, END)
            entry.insert(0, str(x))
    elif last_char == '.' and x == '.':
        pass
    else:
        length = len(entry.get())
        entry.insert(length, str(x))


def enter_operator(x):
    if entry.get() != '0':
        length = len(entry.get())
        all_text = entry.get()
        last_char = all_text[-1:]
        if last_char in ['+', '-', '/'] or all_text[-2:] == '**':
            pass
        else:
            entry.insert(length, btn_operator[x]['text'])


def funclr():
    entry.delete(0, END)
    entry.insert(0, '0')


history = []


def funcal():
    content = entry.get()
    result = eval(content)
    entry.delete(0, END)
    entry.insert(0, result)
    history.append(content + '=' + str(result))
    history.reverse()
    status.configure(text='History : ' + ' | '.join(history[:4]), font='verdana 10 bold')


def fundlt():
    length = len(entry.get())
    entry.delete(length - 1, END)
    if length == 1:
        entry.insert(0, '0')


# entry box
entry = Entry(root, font='verdana 14 bold', width=22, bd=6, justify=RIGHT, bg='#e6e6fa')
# justify is for location of value in entry widget
entry.insert(0, '0')
entry.place(x=30, y=20)
btnnum = []
for i in range(10):
    btnnum.append(Button(width=7, text=str(i), bd=6, command=lambda x=i: enternumber(x)))
# Lamba function takes value of i as x and give it to function enterNumber as x
btmtext = 1
for i in range(0, 3):
    for j in range(0, 3):
        btnnum[btmtext].place(x=30 + j * 90, y=70 + i * 70)
        btmtext += 1
btn_zero = Button(width=34, text='0', bd=5, command=lambda x=0: enternumber(x))
btn_zero.place(x=25, y=280)
btn_dot = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x='.': enternumber(x))
btn_dot.place(x=110, y=340)
btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=funcal)
btn_equal.place(x=200, y=340)
btn_clear = Button(width=4, text='C', font='times 15 bold', bd=5, command=funclr)
btn_clear.place(x=25, y=340)
btn_delete = Button(width=4, text='D', font='times 15 bold', bd=5, command=fundlt)
btn_delete.place(x=300, y=340)
status = Label(root, text='History : ', relief=SUNKEN, height=3, anchor=W, font='verdana 11 bold')
status.pack(side=BOTTOM, fill=X)
# operator button
btn_operator = []
for i in range(4):
    btn_operator.append(Button(width=5, font='verdana 10 bold', bd=6, command=lambda x=i: enter_operator(x)))
btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'
for i in range(4):
    btn_operator[i].place(x=300, y=70 + i * 70)
root.mainloop()
