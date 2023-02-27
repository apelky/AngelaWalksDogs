import sqlite3 

conn = sqlite3.connect('data_test.db')
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

def view_other_table():
    c.execute('SELECT * FROM booked')
    extra = c.fetchall()
    return extra

def main():
   data = view_all_users()
   print(data)
   extra = view_other_table()
   print(extra)

if __name__ == "__main__":
    main()