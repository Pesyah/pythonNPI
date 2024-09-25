"""
6. Написать функцию, которая принимает наименование
таблицы, имя поля и возвращает все записи по полученному
полю из указанной таблицы.
"""

import sqlite3

def fetch_records_by_field(db_name, table_name, field_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT {field_name} FROM {table_name}")
    records = cursor.fetchall()
    
    conn.close()
    return records

# age можно поменять на email, name
records = fetch_records_by_field('6/test.db', 'users', 'age')
for record in records:
    print(record)

"""
Снизу код, если необходимо заполнить базу!
"""

# import sqlite3
# import random
# import string

# def create_and_fill_table(db_name, table_name):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

#     cursor.execute(f'''
#     CREATE TABLE IF NOT EXISTS {table_name} (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         email TEXT NOT NULL
#     )
#     ''')

#     for _ in range(50):
#         name = ''.join(random.choices(string.ascii_letters, k=7))
#         age = random.randint(18, 65)
#         email = f"{name.lower()}@example.com"

#         cursor.execute(f'''
#         INSERT INTO {table_name} (name, age, email)
#         VALUES (?, ?, ?)
#         ''', (name, age, email))

#     conn.commit()
#     conn.close()

# create_and_fill_table("6/test.db", "users")
