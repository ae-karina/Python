import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE PLAYER
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           VARCHAR（20）    NOT NULL);
       ''')

print("create successful!")
dconn.close()