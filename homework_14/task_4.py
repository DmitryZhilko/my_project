import sqlite3

conn = sqlite3.connect('test_4.db')
cursor = conn.cursor() 

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ''')
cursor.execute('''INSERT INTO tab_1(name) VALUES ('apple'), ('orange'), ('banana')''') 
conn.commit()

class Removal():
    def __init__(self, id, ):
        self.id = id

    def deleting_entry(self):
        cursor.execute(f'''DELETE FROM tab_1 WHERE id = '{self.id}' ''')
        conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 
entry = Removal(2)
entry.deleting_entry()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 
