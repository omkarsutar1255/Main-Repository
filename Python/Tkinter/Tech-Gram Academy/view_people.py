from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mycursor = mydb.cursor()

class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+600+200')
        self.title('My People')
        self.resizable(False, False)
