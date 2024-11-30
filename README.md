# database_101


## How to create a database in SQLITE3

**format**:
```python

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)") 

res = cur.execute("SELECT * FROM movie")

res.fetchall()

```

## How to create a table in sqlite3

```SQL
CREATE TABLE table_name(column1, column2, column3, ...);
```

## How to insert data into a table in sqlite3

```SQL

INSERT INTO table_name VALUES (value1, value2, ..., valueN);

```


## how to set data types of a column in a table

```SQL

CREATE TABLE table_name(column1 INTEGER, column2 TEXT, column3 REAL);

```

`TEXT = string`
`INTEGER = integer`
`REAL = float`

> If the input is not of the correct type, it will be converted to the correct type.( for real and integer)
> But for text, if there are no quotes given, then it will not take the input in the table.

> If you input a string in an column of any kind or datatype, it wont be converted to the correct type, it will be stored as a string.

> If you input a numeric value with a quote in a nunmeric column, it will be converted in to the right column type.

## How to add a row permanently in a table

```python

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title TEXT, year INTEGER, score REAL)") 

cur.execute("INSERT INTO movie VALUES ('PRISONERS', '10', '9')")

res = cur.execute("SELECT * FROM movie") ## read all data from movie table

## we can add any datatype 
## not permanently stored

con.commit() # this will add the data into the database


print(res.fetchall())
    
```
## How to delete a row from a talble in sqlite3

```SQL
DELETE FROM table_name WHERE column_name = 'value'
```
## How to update a row from a talble in sqlite3

```SQL
cur.execute("""UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition""") """ is used for multiple line of commands 
```
### How to delete a table in sqlite3
```SQL
DROP TABLE table_name;
```

## How to set a column as primary key in sqlite3

- Rename the existing table
```SQL	
 ALTER TABLE old_table_name RENAME TO new_table_name;
 ```

- make a new table with the same name as the old talble
- set the primary key in the new table
Example:
```SQL	
cur.execute("CREATE TABLE employee(name TEXT , age INTEGER , salary REAL, department TEXT, id INTEGER PRIMARY KEY)")
```
- Copy the whole data from the old table
```SQL
cur.execute("INSERT INTO new_table SELECT * FROM table_old")
```
- remove the whole table