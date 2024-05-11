
import pandas as pd
import streamlit as st
import sqlite3


def create_connection():
    conn = sqlite3.connect('medicine.db')
    return conn

def search_record(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicine_details WHERE name=?", (name,))
    records = cursor.fetchall()
    conn.close()
    return records

def display_records(records):
    df = pd.DataFrame(records, columns=['ID', 'Name', 'Price', 'Qty', 'Shelf Num Rows', 'Date Added'])
    st.dataframe(df)





# def search_record(name):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM medicine_details WHERE name=?", (name,))
#     records = cursor.fetchall()
#     conn.close()
#     return records


# def display_records(records):
#     df = pd.DataFrame(records, columns=['ID', 'Name', 'Price', 'Qty', 'Shelf Num Rows', 'Date Added'])
#     st.dataframe(df)