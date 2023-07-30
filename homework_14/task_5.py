import sqlite3

conn = sqlite3.connect('test_5.db')
cursor = conn.cursor() 

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ''')
cursor.execute('''INSERT INTO tab_1(name) VALUES ('apple'), ('orange'), ('banana')''') 
conn.commit()

class Conclusion():
    def record_output(self):
        cursor.execute('''SELECT * FROM tab_1''')
        k = cursor.fetchall()
        for i in k:
            print(i)

a = Conclusion()
a.record_output()


