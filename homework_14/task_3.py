import sqlite3

conn = sqlite3.connect('test_3.db')
cursor = conn.cursor() 

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ''')
cursor.execute('''INSERT INTO tab_1(name) VALUES ('apple'), ('orange'), ('banana')''') 
conn.commit()

class RecordSubstitution():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def value_update(self):
        cursor.execute(f'''UPDATE tab_1 SET name = '{self.name}' WHERE id = '{self.id}' ''')
        conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 
entry = RecordSubstitution(3, 'cherry')
entry.value_update()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 
