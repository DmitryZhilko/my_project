import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

class NewTable():
    def __init__(self, table_name):
        self.table_name = table_name

    def table_validation(self):
        cursor.execute(f'''SELECT count(name) FROM sqlite_master WHERE TYPE= 'table' AND name='{self.table_name}' ''')
        if cursor.fetchone()[0] == 1:
            print('Таблица уже существует')
        else:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT); ''')
            cursor.execute(f'''INSERT INTO {self.table_name}(name) VALUES ('test') ''')
            conn.commit()

a = NewTable('tab_1')
a.table_validation()
cursor.execute(f'''SELECT * FROM {a.table_name}''')
tab = cursor.fetchall()
print(tab)






