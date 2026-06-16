import sqlite3

con = sqlite3.connect('123.bd')
cursor = con.cursor()

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


cursor.execute('SELECT * FROM books')
for row in cursor.fetchall():
    print(row)
#print(cursor.fetchall()) выводит все в одной строке, так что пох
# выбирает все из БД с книгами

email_name = input()



wer = """
SELECT reader.name, books.title, books.author
FROM reader
JOIN books ON loans.book_id = books.id
JOIN loans ON reader.id = loans.reader_id
WHERE reader.email = ?
"""

cursor.execute(wer, (email_name,))
wer1 = cursor.fetchall()

if wer1:
    print(f"Книги, которые брал(а) {wer1[0][0]}:")
    for _, title, author in wer1:
        print(f"- {title} (автор: {author})")
else:
    print(f"Для email {wer1} записей не найдено.")

