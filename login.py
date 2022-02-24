import sqlite3 as sql
con = sql.connect('loginDB.db')
print("Opened database successfully")

# command = "create table UserID (ID integer primary key autoincrement, username text not null, password text not null);"

# con.execute(command)
# print("Table created")

# def UserInput(username, password):
#     con = sql.connect("loginID.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO UserID(username, password) VALUES (?, ?)", (username, password))
#     con.commit()
#     con.close()

# def UserRetrive():
#     con = sql.connect("loginID.db")
#     cur = con.cursor()
#     cur.execute("SELECT username, password FROM UserID")
#     UserID = cur.fetchall()
#     con.close()
#     return UserID

con.execute("insert into UserID values(1, 'xyz@gmail.com','XYZ123abc')")
con.execute("insert into UserID values(2, 'abc@gmail.com','XYZ123')")
con.commit()
print("Records created successfully")
