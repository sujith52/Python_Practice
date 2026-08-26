print("excuting the sql query using the python var")

import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

new_user = ("Dr DOOM", 50000)

# insert_statement = '''
# INSERT INTO users(name,age) VALUES (?,?)
# '''

see_statement = '''
SELECT * FROM users
'''

# cursor.execute(insert_statement, new_user)
cursor.execute(see_statement)
rows = cursor.fetchall()
for x in rows:
    print(x)

conn.commit()
conn.close()