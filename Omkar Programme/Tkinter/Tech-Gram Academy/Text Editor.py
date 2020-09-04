from tkinter import *
from tkinter import filedialog

root = Tk()


class TextEditor:
    current_open_file = 'no file'

    def __init__(self, master):
        self.master = master  # this used to allow other def function to use master
        master.title('textpad')  # inside init function we can directly use master
        self.geo()  # setting geometry with function name geo
        self.text_area = Text(master, undo=True)
        self.text_area.pack(fill=BOTH, expand=1)  # for fully expand widget on root use expand is 1
        self.main_menu = Menu(master)
        master.config(menu=self.main_menu)
        # creating file menu on main menu
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', command=self.save_f)
        self.file_menu.add_command(label='Save As', command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=master.quit)  # quit for exit and destroy for back/
        # creating edit menu on main menu
        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Copy', command=self.copy_text)
        self.edit_menu.add_command(label='Cut', command=self.cut_text)
        self.edit_menu.add_command(label='Paste', command=self.paste_text)

    def open_file(self):
        abc = filedialog.askopenfile(initialdir='F:\Omkar', title='select file',
                                     filetypes=(('text files', '.txt'), ('all files', '*.*')))
        if abc is not None:
            self.text_area.delete(1.0, END)
            for line in abc:
                self.text_area.insert(END, line)
            self.current_open_file = abc.name  # open file name will be saved to class variable
            abc.close()

    def save_file(self):
        f = filedialog.asksaveasfile(mode='w', title='select file', defaultextension='.txt')
        if f is None:  # if we cancel then just return
            return
        text2save = self.text_area.get(1.0, END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()

    def save_f(self):
        if self.current_open_file == 'no file':
            self.save_file()
        else:
            f = open(self.current_open_file, 'w+')
            f.write(self.text_area.get(1.0, END))
            f.close()

    def new_file(self):
        self.text_area.delete(1.0, END)
        self.current_open_file = 'no file'

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self):
        self.copy_text()
        self.text_area.delete('sel.first', 'sel.last')

    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())       # INSERT will paste at current position

    def geo(self):
        self.master.geometry('1000x300')  # self.master makes it use master argument outside init function


te = TextEditor(root)
root.mainloop()
