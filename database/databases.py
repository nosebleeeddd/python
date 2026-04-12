# Database implementation with python
# using sqllite

import sqlite3

connection = sqlite3.connect('mydata.db')

cursor = connection.cursor()

# Creates a new table
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

# Inserts data into table we created
cursor.execute("""
INSERT INTO persons VALUES
('Paul', 'Smith', 24),
('Mark', 'Johnson', 42),
('Anna', 'Smith', 34)
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

