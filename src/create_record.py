
import pandas as pd
import sqlite3


def create_connection():
    conn = sqlite3.connect('medicine.db')
    return conn

def create_record(name, price, qty, shelf_num_rows, date_added):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicine_details (name, price, qty, shelf_num_rows, date_added) VALUES (?, ?, ?, ?, ?)",
                   (name, price, qty, shelf_num_rows, date_added))
    conn.commit()
    conn.close()