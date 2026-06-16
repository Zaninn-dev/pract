import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

target_author = 'Достоевский'
cursor.execute("SELECT * FROM books WHERE author = ?", (target_author,))
for row in cursor.fetchall():
    print(row)





