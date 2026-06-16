import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

cursor.execute('SELECT title, price FROM books WHERE price > 500')
print(cursor.fetchall())
