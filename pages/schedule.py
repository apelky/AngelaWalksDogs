import streamlit as st
import datetime
import streamlit.components.v1 as components

'''Goal: To get creative! I don't want to pay for a scheduling service, so I am going to build my own
Not including house sitting rn for simplicity
'''

def duration():
    duration = st.selectbox(
        'Select a duration',
        ('20 Minutes - $15', '30 Minutes - $20', '60 Minutes - $30')
    )
    return duration

def schedule():
    d = st.date_input(
        'Select a day',
        datetime.datetime.now()
        )
    return d

def time():
    t = st.time_input('See calendar, select a time when I am not already "busy"', datetime.time(9, 00))
    return t

def schedule_builder():
    r_duration = duration()
    r_day = schedule()
    r_time = time()

    return r_duration, r_day, r_time

# bootstrap 4 collapse example
components.html(
    """
<iframe src="https://calendar.google.com/calendar/embed?src=fjfn243lp31qaff16qc1gmlo10%40group.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="600" height="600" frameborder="0" scrolling="no"></iframe>
    """,
    height=700,
)

option = st.selectbox(
    'What kind of service would you like to book?',
    ('Walk', 'Drop-In')
)

if option == 'Walk':
    walk_duration, walk_day, walk_time = schedule_builder()

if option == 'Drop-In':
    drop_duration, drop_day, drop_time = schedule_builder()
