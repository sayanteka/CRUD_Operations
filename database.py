import sqlite3


conn = sqlite3.connect('medicine.db')


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS medicine_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    qty INTEGER NOT NULL,
    shelf_num_rows INTEGER NOT NULL,
    date_added TEXT NOT NULL
)
''')


conn.commit()


conn.close()
