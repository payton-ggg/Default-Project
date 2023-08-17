import sqlite3 as sql 

conn = sql.connect('it.sqlite')
cur = conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS users (
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(200),
	password varchar(200) 
	) ''')
conn.commit()

name_user = input("Enter Your Name: ")
password_user = input("Enter Your Password: ")
cur.execute('INSERT INTO users(name, password) VALUES (\'%s\', \'%s\')'%(name_user, password_user))
conn.commit()

print('List Users:')
cur.execute('SELECT * FROM users')
users = cur.fetchall()

for user in users:
	print(f'Name User: {user[1]} | Password User: {user[2]}')

cur.close()
conn.close()