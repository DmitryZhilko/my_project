import sqlite3

conn = sqlite3.connect('test_6.db')
cursor = conn.cursor() 

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ''')
cursor.execute('''INSERT INTO tab_1(name) VALUES ('apple'), ('orange'), ('banana')''') 
conn.commit()

class DeleteEverything():
    def delete_all_entries(self):
        cursor.execute('''DELETE FROM tab_1 ''')
        conn.commit()

        
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 
a = DeleteEverything()
a.delete_all_entries()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k) 