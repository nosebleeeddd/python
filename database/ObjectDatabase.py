# Database implementation with python
# using OOP and python classes
# with sqllite

import sqlite3

class Person:

    def __init__(self, id_number, first, last, age):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = connection.cursor()


    # load person from table and convert to python object
    def load_person(self, id_number):
        cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """).format(id_number)

        # instead list of tuples we get a tuple of first element
        results = cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()


# Creates a new table
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

# Inserts data into table we created
cursor.execute("""
INSERT INTO persons VALUES
(1,'Paul', 'Smith', 24),
(2,'Mark', 'Johnson', 42),
(3,'Anna', 'Smith', 34)
""")


# selects only persons with this name
cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Smith'
""")

# prints all data in the db
rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()


