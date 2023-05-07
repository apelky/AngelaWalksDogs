from pathlib import Path
import streamlit as st
from user_manager import get_userdata
import datetime as dt

current_dir = Path('pages').parent
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

def d_format(string):
    index = string.rfind('-')
    string = string[:index]
    string = string.replace('T', ' ')
    string = dt.datetime.strptime(string,"%Y-%m-%d %H:%M:%S")
    return string



if st.session_state["username"] == '':
    st.warning("Welcome to the Booked Page! If you haven't yet, please login.")
    st.stop()
else:
    user_data = get_userdata(st.session_state["username"])
    st.write('Welcome, ',user_data[0][0],'!')
    for event in user_data:
        date_cmp = d_format(event[1])
        if date_cmp > dt.datetime.now():
            st.write("You have a", event[3], "booked for:", event[1],". I'll see you then!")