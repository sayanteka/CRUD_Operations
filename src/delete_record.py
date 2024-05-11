import streamlit as st 
import pandas as pd
import sqlite3

def create_connection():
    conn = sqlite3.connect('medicine.db')
    return conn

def delete_record(conn, cursor, id):
    cursor.execute("DELETE FROM medicine_details WHERE id=?", (id,))
    conn.commit()

def delete_record_form():
    st.header('Delete Record')
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicine_details")
    all_records = cursor.fetchall()
    #record0=key=id
    #rest are values
    records_dict = {record[0]: f"{record[1]} - {record[2]} - {record[3]} - {record[4]} - {record[5]}" for record in all_records}
    selected_id = st.selectbox('Select Record ID to Delete', list(records_dict.keys()))
    if selected_id:
        selected_record_info = records_dict[selected_id]
        if st.button('Delete'):
            delete_record(conn, cursor, selected_id)
            st.success(f"Record with ID {selected_id} ({selected_record_info}) deleted successfully.")
    else:
        st.info('Select a record to delete.')
