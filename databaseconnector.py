
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3300,
    user="root",
    password="bhakti6000"
)

print("Database connected successfully!")

cur = conn.cursor()

# Create database
cur.execute("CREATE DATABASE IF NOT EXISTS college")

# Select database
cur.execute("USE college")

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    name VARCHAR(20),
    age INT,
    rollno INT
)
""")

# Insert records
sql = """
INSERT INTO student(name, age, rollno)
VALUES (%s, %s, %s)
"""

data = [
    ('bhakti', 20, 12),
    ('apeksha', 22, 10),
    ('sushil', 25, 2)
]

cur.executemany(sql, data)

conn.commit()

# Display records
cur.execute("SELECT * FROM student")

for res in cur.fetchall():
    print(res)

cur.close()
conn.close()
