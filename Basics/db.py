import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("CREATE TABLE student(id, name, phone)")

res = cur.execute("SELECT * FROM movie")
res = cur.execute("SELECT * FROM student")

res.fetchall()