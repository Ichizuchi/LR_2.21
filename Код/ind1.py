import sqlite3

def display_table(headers, data):
    """
    Отображает данные в виде таблицы.
    """
    print("┌", end="")
    for header in headers[:-1]:
        print("─" * 20 + "┬", end="")
    print("─" * 20 + "┐")
    
    print("│", end="")
    for header in headers:
        print(f" {header:<18}│", end="")
    print("\n├", end="")
    for header in headers[:-1]:
        print("─" * 20 + "┼", end="")
    print("─" * 20 + "┤")
    
    for row in data:
        print("│", end="")
        for item in row:
            print(f" {item:<18}│", end="")
        print()
        
    print("└", end="")
    for header in headers[:-1]:
        print("─" * 20 + "┴", end="")
    print("─" * 20 + "┘")


def find_store(cursor, store_id):
    """
    Находит магазин по его идентификатору.
    """
    cursor.execute('SELECT * FROM stores WHERE store_id = ?', (store_id,))
    store = cursor.fetchone()
    if store:
        print("Найден магазин:")
        print("ID:", store[0])
        print("Название:", store[1])
        print("Адрес:", store[2])
    else:
        print("Магазин с указанным ID не найден.")

# Создание соединения с базой данных
conn = sqlite3.connect('shops.db')

# Создание курсора для выполнения операций с базой данных
cursor = conn.cursor()

# Отображение содержимого таблицы магазинов
cursor.execute('SELECT * FROM stores')
stores = cursor.fetchall()
print("Содержимое таблицы магазинов:")
display_table(['ID', 'Название', 'Адрес'], stores)

# Отображение содержимого таблицы товаров
cursor.execute('SELECT * FROM products')
products = cursor.fetchall()
print("\nСодержимое таблицы товаров:")
display_table(['ID', 'Название', 'Цена', 'ID магазина'], products)

# Поиск магазина по его идентификатору
store_id_to_find = int(input("Введите ID магазина для поиска: "))
find_store(cursor, store_id_to_find)

# Закрытие курсора и соединения
cursor.close()
conn.close()
