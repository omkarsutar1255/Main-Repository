# class omakr:
#     def tom(self, val):
#         # sutar.newcal(self)
#         print("tom calling", val)
#         self.hupper()
#
#     def banka(self):
#         print("start of omakr.banka")
#         self.root = 45 + 543
#
#         print(self.root)
#         print("end of omakr.banka")
#
#     def new(self):
#         print("start of omakr.new")
#         self.banka()
#         print(self.root)
#         print("end of omakr.new")
#
#
# class sutar(omakr):
#     def newcal(self):
#         print("start sutar.newcal")
#         print("end sutar.newcal")
#         self.tom("upper")
#
#     def hkh(self):
#         print("hkh calling")
#
#
# class diff(sutar):
#     def tom2(self):
#         self.tom("upper")
#
#     def hupper(self):
#         print("name of king")
#
# if __name__ == '__main__':
#     aa = diff()
#     aa.tom2()

# from math import ceil
# print(ceil(1.3))
# 5357.16
# from math import pi
# stss = 90.0
# P = 90000.0
# d1 = 72
# t = 12
# print((d1**2) - (d1*t)*(4/pi) + (P/stss)*(4/pi))
from tkinter import *
root = Tk()
root.geometry('800x400+120+120')
root.title('Sharad Institute of Technology, College of Engineering Ichalkaranji')

f6 = Frame(root, width=650, height=384, bg="blue")
f7 = Frame(root, width=650, height=50, bg="red")
f6.pack(side=TOP, fill=BOTH, expand=True)
f7.pack(side=BOTTOM, fill=BOTH, expand=False)
root.mainloop()
