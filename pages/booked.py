import streamlit as st
from user_manager import get_userdata

if st.session_state["username"] == '':
    st.warning("Welcome to the Booked Page! If you haven't yet, please login.")
    st.stop
else:
    user_data = get_userdata(st.session_state["username"])
    st.write('Welcome, ',user_data[0][0],'!')
    st.write("You have a", user_data[0][3], "booked for:", user_data[0][1],". I'll see you then!")