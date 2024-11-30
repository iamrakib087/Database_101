import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

#cur.execute("CREATE TABLE employee(name TEXT , age INTEGER , salary REAL, department TEXT, id INTEGER)")
#cur.execute("INSERT INTO employee VALUES ('Rajib' , 30 , 15000, 'IT', 20246969 )")
#cur.execute("INSERT INTO employee VALUES ('Ruhi' , 23 , 50000, 'IT', 20244204 )")
#cur.execute("INSERT INTO employee VALUES ('Rishat' , 26 , 115000, 'CEO', 20247777 )")
#cur.execute("INSERT INTO employee VALUES ('Plabon' , 23 , 40000, 'IT', 20249999 )")
#cur.execute("""UPDATE movie SET year = 1972  WHERE year = 1973""")
#cur.execute("DELETE FROM employee WHERE name = 'Rajib'")
#cur.execute("ALTER TABLE employee RENAME TO kormochari;") 
#cur.execute("CREATE TABLE employee(name TEXT , age INTEGER , salary REAL, department TEXT, id INTEGER PRIMARY KEY)")
#cur.execute("INSERT INTO employee VALUES ('Risat', 23 , 140000, 'IT', 20247777)")
#cur.execute("DROP TABLE kormochari;")
cur.fetchall()
con.commit()
cur.execute("SELECT * FROM employee")

print(cur.fetchall())