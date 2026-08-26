import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

marvel = [
    ("Iron man", 70),("Thanos",10000),("ultron",2)
]

# cursor.executemany("INSERT INTO users(name,age) VALUES (?,?)", marvel)
cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()
for id, name, age in rows:
    print(f"id : {id} , Name : {name} , Age : {age}")

connection.commit()
connection.close()