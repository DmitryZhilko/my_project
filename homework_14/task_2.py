import sqlite3

conn = sqlite3.connect('test_2.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ''')
cursor.execute('''INSERT INTO tab_1(name) VALUES ('hello')''') 
conn.commit()

class NewEntry():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def record_verification(self):
        cursor.execute(f'''SELECT * FROM tab_1 WHERE id='{self.id}' ''')
        if cursor.fetchone() == None:
            cursor.execute(f'''INSERT INTO tab_1 VALUES ('{self.id}', '{self.name}')''')
            conn.commit()
        else:
            print('Такой id уже существует')
            

entry = NewEntry(3, 'world')
print(f'Выбранный id - {entry.id}')
entry.record_verification()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 