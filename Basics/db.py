import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

#cur.execute("CREATE TABLE movie(title, year, score)")
#cur.execute("CREATE TABLE student(id, name, phone)")
cur.execute("INSERT INTO movie VALUES ('PRISONERS' , 2013 , 8.2)")


res = cur.execute("SELECT * FROM movie") #read all data from movie table
res = cur.execute("SELECT * FROM student") #read all data from student table

res.fetchall()
print(res.fetchall())