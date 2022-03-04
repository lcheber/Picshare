import sqlite3

DATABASE = 'app.db'
db = sqlite3.connect(DATABASE)

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS pictures')
cursor.execute("""CREATE TABLE pictures (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title VARCHAR(200) NOT NULL,
                            date timestamp,
                            category_id INTEGER NOT NULL,
                            description VARCHAR(600),
                            path VARCHAR(200) NOT NULL)
                            """)

cursor.execute('DROP TABLE IF EXISTS comments')
cursor.execute("""CREATE TABLE pictures (id INTEGER PRIMARY KEY AUTOINCREMENT),
                            comment,
                            picture_id
                            date
                            """)

cursor.execute('DROP TABLE IF EXISTS comments')
cursor.execute("""CREATE TABLE pictures (id INTEGER PRIMARY KEY AUTOINCREMENT),
                            comment,
                            picture_id
                            date
                            )""")

db.commit()
db.close()