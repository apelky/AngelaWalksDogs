'''
user_manager.py last edited on ?.

Angela Pelky

This is a helper program to assist both login.py and schedule.py. In order to create a "bookings" page where
a user can see their booked services, I needed to created another database besides the .yaml one. This is because
the .yaml database is specifically tailored towards the authentication of the user. My data.db database is tailored
toward keeping track of what times/dates the user has booked.

----------------------------------------

user_manager.py uses Python 3.10
'''

import sqlite3 

conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username,name)')
	c.execute('CREATE TABLE IF NOT EXISTS booked(username, dstart, dend, type)')

def add_user(username,name):
	c.execute('INSERT INTO userstable(username,name) VALUES (?,?)',(username,name))
	conn.commit()

def add_userdata(username,event):
    dstart = event['start']['dateTime']
    dend = event['end']['dateTime']
    type = event['summary'][0:4]
    c.execute('INSERT INTO booked(username,dstart,dend,type) VALUES (?,?,?,?)',(username,dstart,dend,type))
    conn.commit()

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_all_booked():
    c.execute('SELECT * FROM booked')
    extra = c.fetchall()
    return extra

def get_userdata(username):
    values = []
    get_row = 'SELECT * FROM booked WHERE username = ?'
    for row in c.execute(get_row, (username,)):
        values.append(row)
    return values