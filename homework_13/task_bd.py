import sqlite3
import random

conn = sqlite3.connect('task.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')

for i in range(3):
    x = random.randint(1,9)
    cursor.execute('''INSERT INTO tab_1(col_1) VALUES (? )''', (x,))
conn.commit()

class WorkingWithDatabase():
    

    def namber_of_arguments(self, *args):

        if len(args) == 1:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')    
            conn.commit()
        elif len(args) == 2 and isinstance(args[1], (int, float)):
            cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
            conn.commit()               
        elif len(args) == 3 and isinstance(args[0], object) and isinstance(args[1], object) and isinstance(args[2], (int, float)):
            cursor.execute('''UPDATE tab_1 SET col_1='77' WHERE id=3''')
            conn.commit()
            
a = WorkingWithDatabase()
a.namber_of_arguments(4)
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(f'Вставляем в таблицу  запись с числом 3 - {k}')
a.namber_of_arguments(5, 6)
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(f'Удаляем первую запись - {k}')
a.namber_of_arguments('b', 3, 7)
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(f'Обновляем запись колонки 3 на число 77 - {k}')