import mysql.connector                                     # import module for connection
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")         # connnection to mysql database
print(mydb)
if mydb:
    print("connection is successfull")
else:
    print("connection is unsuccessfull")


# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")
print(mydb)
mycursor = mydb.cursor()                                   # use cursor for execute commands
print(mycursor)
mycursor.execute("show databases")                         # enter command in mysql cursor
print(mycursor)
for db in mycursor:
    print(db)                                             # retrieve the values that stored in mysql


# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="omkar")
mycursor = mydb.cursor()
mycursor.execute("create table newwi( rollno int (10), name varchar (20), mobileno int (10) )")
# create new table# in sharad database
mycursor.execute("show tables")                        # retrieve all tables from dabase
for tb in mycursor:
    print(tb)


# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mycursor = mydb.cursor()
sqlform = "insert into new(rollno, name, mobileno) values(%s, %s, %s)"         # insert values into table
employees = [(55, "omakr", 906354), (56, "rakesh", 757789)]                    # values of table to enter
mycursor.executemany(sqlform, employees)
mydb.commit()


# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mycursor = mydb.cursor()
# mycursor.execute("select name from new")
mycursor.execute("select * from new")
# myresult = mycursor.fetchone()                       # get one value from column name of table new
myresult = mycursor.fetchall()                       # get all values from column name of table new
for row in myresult:
    print(row)                                      # retrieve all value
