import streamlit as st
import datetime 
import pandas as pd
import sqlite3

def create_connection():
    conn = sqlite3.connect('medicine.db')
    return conn

def update_record(conn,cursor,id, name, price, qty, shelf_num_rows, date_added):
    
    cursor = conn.cursor()
    cursor.execute("UPDATE medicine_details SET name=?, price=?, qty=?, shelf_num_rows=?, date_added=? WHERE id=?",
                   (name, price, qty, shelf_num_rows, date_added, id))
    conn.commit()
    conn.close()

def update_record_form():
    st.header('Update Record')
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT name FROM medicine_details")
    all_medicine_names = [row[0] for row in cursor.fetchall()]
    selected_name = st.selectbox('Select Medicine Name to Update', all_medicine_names)
    if selected_name:
        cursor.execute("SELECT * FROM medicine_details WHERE name=?", (selected_name,))
        record = cursor.fetchone()
        if record:
            id, name, price, qty, shelf_num_rows, date_added = record
            id=st.number_input('ID',value=id)
            new_name = st.text_input('New Medicine Name', value=name)
            new_price = st.number_input('New Price', value=price)
            new_qty = st.number_input('New Quantity', value=qty, min_value=0, step=1)
            new_shelf_num_rows = st.number_input('New Shelf Num Rows', value=shelf_num_rows, min_value=1, step=1)
            date_added = datetime.datetime.strptime(date_added, '%Y-%m-%d').date()
            new_date_added = st.date_input('New Date Added', value=date_added)
            if st.button('Update'):
                update_record(conn, cursor, id, new_name, new_price, new_qty, new_shelf_num_rows, new_date_added)
                st.success('Record updated successfully.')
        else:
            st.warning('No record found for the selected medicine name.')
    else:
        st.info('Select a medicine name to update.')


