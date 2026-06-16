import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()


cursor.execute('''
SELECT readers.name, books.title, loans.loan_date
FROM loans
JOIN books ON loans.book_id = books.id
JOIN readers ON loans.reader_id = readers.id
WHERE loans.return_date IS NULL
''')
print("Книги на руках:")
for row in cursor.fetchall():
    print(row)
