'''
booked.py last edited on May 8th.

Angela Pelky

This is a page where users can view their booked services. It interacts with UserManager to extract user data.

----------------------------------------

booked.py uses Python 3.10
'''

import streamlit as st
import datetime as dt

from UserManager import get_userdata
from pathlib import Path


current_dir = Path('pages').parent
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

# Helper function that formats our date 
def d_format(string):
    index = string.rfind('-')
    string = string[:index].replace('T', ' ')
    return dt.datetime.strptime(string,"%Y-%m-%d %H:%M:%S")

# Force user login
if st.session_state["username"] == '':
    st.warning("Welcome to the Booked Page! If you haven't yet, please login.")
    st.stop()
else:
    user_data = get_userdata(st.session_state["username"])
    st.title(f"Welcome {user_data[0][0]}!")
    st.subheader("Booked")
    col1,col2,col3 = st.columns(3, gap="small")
    with col1:
        st.write("TYPE")
    with col2:
        st.write("DATE")
    with col3:
        st.write("TIME")

    # Display each booked event if and only if it is in the future
    for event in user_data:
        formatted = d_format(event[1])
        if formatted > dt.datetime.now():
            with col1:
                st.write(event[3])
            with col2:
                st.write(formatted.strftime("%a, %b %d"))
            with col3:
                st.write(formatted.strftime("%I:%M %p"))