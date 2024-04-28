# открываем базу
# подключаем SQLite
import sqlite3 as sl

# открываем файл с базой данных
con = sl.connect('mydatabase.db')

with con:
    # получаем количество таблиц с нужным нам именем
    data = con.execute("select count(*) from sqlite_master where type='table' and name='goods'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            
            # создаём таблицу для товаров
            with con:
                con.execute("""
                    CREATE TABLE goods (
                        product VARCHAR(20) PRIMARY KEY,
                        count INTEGER,
                        price INTEGER
                    );
                """)
            # подготавливаем множественный запрос
sql = 'INSERT INTO goods (product, count, price) values(?, ?, ?)'
# указываем данные для запроса
data = [
    ('стол', 2, 3000),
    ('стул', 5, 1000),
    ('табурет', 1, 500)
]

# добавляем с помощью множественного запроса все данные сразу
with con:
    con.executemany(sql, data)

# выводим содержимое таблицы на экран
with con:
    data = con.execute("SELECT * FROM goods")
    for row in data:
        print(row)