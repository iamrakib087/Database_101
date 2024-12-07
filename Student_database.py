import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

#cur.execute("CREATE TABLE Students(SID TEXT PRIMARY KEY , Name TEXT , Mobile INTEGER)")
cur.execute("INSERT INTO Students VALUES ('IST0011' , 'Mahid' , 01556564844)")
cur.execute("INSERT INTO Students VALUES ('IST0012' , 'Farhan' , 01556564844)")
cur.execute("INSERT INTO Students VALUES ('IST0013' , 'Shahed' , 01557454844)")
cur.execute("CREATE TABLE Courses(CID TEXT PRIMARY KEY , Course_Name TEXT , SID TEXT,FOREIGN KEY(SID) REFERENCES Students(SID))")
cur.execute("INSERT INTO Courses VALUES ('CSE101', 'Computer Introduction' , 'IST0011')")
cur.execute("INSERT INTO Courses VALUES ('CSE102', 'Database Management' , 'IST0011')")
cur.execute("INSERT INTO Courses VALUES ('CSE103', 'Linear Algebra' , 'IST0011')")

cur.fetchall()
con.commit()
cur.execute("SELECT * FROM Students")
cur.execute("SELECT * FROM Courses")


print(cur.fetchall())