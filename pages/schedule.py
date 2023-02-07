import streamlit as st
import datetime
import streamlit.components.v1 as components

'''Goal: To get creative! I don't want to pay for a scheduling service, so I am going to build my own
Not including house sitting rn for simplicity
'''

from GoogleCalendarQuickstart import *

event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print 'Event created: %s' % (event.get('htmlLink'))

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
<iframe src="https://calendar.google.com/calendar/embed?src=contact.angelawalksdogs%40gmail.com&ctz=America%2FLos_Angeles" style="border: 0" width="600" height="600" frameborder="0" scrolling="no"></iframe>
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
