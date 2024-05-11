import streamlit as st 
#st.session_state is a dict. It can have keys & values

# counter=0
# st.write(counter)

# if st.button('up'):
#    counter+=1
#    st.write(counter)
#https://www.youtube.com/watch?v=dOl51vhOGRc
if 'counter' not in st.session_state:
    st.session_state.counter=0

if st.button('up'):
    st.write(st.session_state.counter)
    st.session_state.counter+=1

if st.button('reset'):
   st.session_state.counter=0


