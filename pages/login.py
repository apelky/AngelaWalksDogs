'''
login.py last edited on ?.

Angela Pelky

This is a page where users can login and get authenticated. It stores users data in database.yaml.

----------------------------------------

login.py uses Python 3.10
'''

import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

from streamlit_authenticator.authenticate import Authenticate

from user_manager import *

# Loading local database file
with open('database.yaml') as file:
    database = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = Authenticate(
    database['credentials'],
    database['cookie']['name'], 
    database['cookie']['key'], 
    database['cookie']['expiry_days'],
    database['preauthorized']
)

if 'username' not in st.session_state:
    st.session_state['username'] = ''

# creating a login widget
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(f'Welcome *{name}*')
    st.session_state['username'] = username
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# Creating a password reset widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

# Creating a new user registration widget
try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
        create_usertable()
        add_user(username,name)
        if "un" not in st.session_state:
            st.session_state["un"] 
        if "run" not in st.session_state:
            st.session_state["run"] = False
except Exception as e:
    st.error(e)

# Creating a forgot password widget
try:
    username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    if username_forgot_pw:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)

# Creating a forgot username widget
try:
    username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
    if username_forgot_username:
        st.success('Username sent securely')
        # Username to be transferred to user securely
    elif username_forgot_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)

# Creating an update user details widget
if authentication_status:
    try:
        if authenticator.update_user_details(username, 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

# Saving config file
with open('database.yaml', 'w') as file:
    yaml.dump(database, file, default_flow_style=False)