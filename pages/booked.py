import streamlit as st
from user_manager import get_userdata

def logged_in(username):
    return st.session_state[username]

if not logged_in():
    st.warning("You must log-in to see the content of this sensitive page! Head over to the log-in page.")
    st.stop()  # App won't run anything after this line

def display_booked(username):
    st.write(get_userdata(username))
    # do stuff with date
    # check current date
    # compare it with list dates and only display confirmed bookings after that date
    # make it look pretty! 
    return 

def run(username):
    # DO SOMETHING

    return