import streamlit as st 
from src.create_record import *
from src.view_record import *
from src.update_record import *
from src.delete_record import *

st.set_page_config(page_title="StreamlitDashboard", page_icon=r"C:\Users\Sayantika\Downloads\Crud_using_streamlit\Images\Screenshot 2024-05-11 152028.png",layout="wide")
st.markdown("<h1 id='title'> Medicine Record Management</h1>", unsafe_allow_html=True)
st.markdown("<style>#title{text-align:center;}</style>", unsafe_allow_html=True)
st.markdown("<style>div.block-container{padding-top:2rem;text-align:center;}</style>", unsafe_allow_html=True)

option = st.sidebar.selectbox(
        'Select Option',
        ('Create Record', 'View Record', 'Update Record', 'Delete Record')
    )

if option == 'Create Record':
    st.header('Create Record')
    name = st.text_input('Medicine Name')
    price = st.number_input('Price')
    qty = st.number_input('Quantity', min_value=0, step=1)
    shelf_num_rows = st.number_input('Shelf Num Rows', min_value=1, step=1)
    date_added = st.date_input('Date Added')
    if st.button('Create'):
            create_record(name, price, qty, shelf_num_rows, date_added)
            st.success('Record created successfully.')

elif option == 'View Record':
        st.header('View Record')
        #search_name = st.text_input('Search Medicine Name')
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM medicine_details")
        all_medicine_names = [row[0] for row in cursor.fetchall()]
        selected_name = st.selectbox('Select Medicine Name', all_medicine_names)
        if st.button('Search'):
           records = search_record(selected_name)
           display_records(records)

elif option == 'Update Record':
      update_record_form()
      
elif option=='Delete Record':
      delete_record_form()