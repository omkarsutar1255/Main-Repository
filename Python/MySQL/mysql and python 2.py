import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mycursor = mydb.cursor()
sql = "update new set mobileno=123456 where name='omakr'"
mycursor.execute(sql)
mydb.commit()

# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mydb.cursor().execute("insert into new values(888, 'qwe', 888), (999, 'tyu', 999);")
mydb.commit()

# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mydb.cursor().execute("delete from new where name='qwe';")
mydb.commit()

# import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="tiger", database="sharad")
mycursor = mydb.cursor()                                       # mycurspr is required for fetchall
mycursor.execute("select * from new")
for row in mycursor.fetchall():
    print(row)
