import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS books(
    id integer primary key autoincrement,
    title text not null,
    author text not null,
    year integer,
    price real
    )
'''
)
# таблица книг
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reader(
    id integer primary key autoincrement,
    name text not null,
    email text unique
    )
'''
)
#таблица читателей

cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans(
    id integer primary key autoincrement,
    book_id integer,
    reader_id integer,
    loan_date text,
    return_date text,
    FOREIGN KEY (book_id) REFERENCES books(id), 
    FOREIGN KEY (reader_id) REFERENCES reader(id)
    )
'''
)
print('Таблицы созданы')

books_data = [
    ('Олений пенис', 'Электрослабость', 2020, 375),
    ('Тимур','Игорь Желудь', 2019,200),
    ('Саша','Игорь Желудь', 2020,300)
]
cursor.executemany('INSERT INTO books(title, author, year, price) VALUES(?,?,?,?)', books_data)
#добавляет в БД много чего

reader_data = [
    ('Алексей', 'mail@mail.ru'),
    ('Петр','WWffpidor@mail.ru'),
    ('Владислав','Goddame@mail.ru')
]
cursor.executemany('INSERT INTO reader(name, email) VALUES(?,?)', reader_data)
# добавляет в БД имена и имейлы типов


# Email читателя, которого мы ищем
target_email = 'ivan@example.com'

# SQL-запрос с двойным JOIN
query = '''
SELECT 
    reader.name, 
    books.title, 
    books.author
FROM reader
JOIN loans ON reader.id = loans.reader_id
JOIN books ON loans.book_id = books.id
WHERE reader.email = ?
'''

cursor.execute(query, (target_email,))
results = cursor.fetchall()

if results:
    print(f"Книги, которые брал(а) {results[0][0]}:")
    for _, title, author in results:
        print(f"- {title} (автор: {author})")
else:
    print(f"Для email {target_email} записей не найдено.")

conn.close()