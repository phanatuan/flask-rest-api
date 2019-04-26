import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id int, username text, password text)'
cursor.execute(create_table)

user = (1, 'jose', 'yeahh')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

users = [ 
    (2, 'tuan', 'mannn'), 
    (3, 'khanh', 'hello')
]

cursor.executemany(insert_query, users)
connection.commit()
connection.close()