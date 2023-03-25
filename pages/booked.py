import streamlit as st
from user_manager import get_userdata

if "run" not in st.session_state:
    st.session_state["run"]
if "un" not in st.session_state:
    st.session_state["un"]

if not st.session_state["run"]:
    st.warning("Welcome to the Booked Page! If you haven't yet, please login.")
    st.stop

else:
    user_data = st.session_state["un"]
    user_data = get_userdata(user_data)
    st.write('Welcome ,',user_data[0][0],'!')
    st.write("You have a", user_data[0][3], "booked for:", user_data[0][1],". I'll see you then!")