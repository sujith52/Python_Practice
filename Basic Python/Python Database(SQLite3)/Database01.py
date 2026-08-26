print("creating a database using the sqlite2 module with in python !")
import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT , age INTEGER)")
students = [
    ("Sujith",22),
    ("Sreejas", 22),
    ("Lathas", 22)
]
# cursor.executemany("INSERT INTO users(name,age) VALUES (?,?)", students)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for x in rows:
    print(x)

connection.commit()
connection.close()