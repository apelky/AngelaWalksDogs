import streamlit as st
from user_manager import get_userdata

def run():
    return True

if not run():
    st.warning("You must log-in to see the content of this sensitive page! Head over to the log-in page.")
    st.stop()