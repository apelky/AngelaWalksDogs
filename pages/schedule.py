import streamlit as st
import datetime
import streamlit.components.v1 as components

from Authenticator import main_auth

DEFAULT = 'America/Los_Angeles'

# a dictionary where the username is the key and the value is a dictionary with their event details
# TODO: create a dictionary of dictionaries or use session state?
# events = {}
# event dictionary is sent to Google Calendar
event = {}
test_event = {
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

def duration():
    duration = st.selectbox(
        'Select a duration',
        ('20 Minutes - $15', '30 Minutes - $20', '60 Minutes - $30')
    )
    return duration[:2]

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

# embed calendar for viewing within my app
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

get_user = st.text_input(
  'Enter your username'
)

get_pet = st.text_input(
  'Enter your pets name'
)

get_location = st.text_input(
  'Enter your address'
)

get_notes = st.text_input(
  'Enter any access instructions I would need to get inside the home. For example: the access code is xyz or I left the key under the mat!'
)

if option == 'Walk':
    walk_duration, walk_day, walk_time = schedule_builder()
    run = st.button('Done')
    
    # must convert it to a full datetime object before adding walk duration
    datetime_obj = (datetime.datetime.combine(walk_day, walk_time))
    end_time = (datetime_obj + datetime.timedelta(minutes=int(walk_duration)))
    datetime_obj = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S-08:00')
    if datetime_obj == test_event['start']['dateTime']:
        print("Exactly!")
    end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S-08:00')
    print(end_time)

    event['summary'] = 'Walk with '+get_pet
    event['location'] = get_location
    event['description'] = get_notes
    event['start'] = {'dateTime': datetime_obj, 'timeZone':DEFAULT}
    if(event['start']['dateTime'] != test_event['start']['dateTime']):
        print("fml")
        print(event['start']['dateTime'])
        print(test_event['start']['dateTime'])
    event['end'] = {'dateTime': end_time, 'timeZone':DEFAULT}
    if run:
        #start = test_event['start']
        #start = start['dateTime']
        #print(type(start))
        main_auth(event)

if option == 'Drop-In':
    #TODO
    drop_duration, drop_day, drop_time = schedule_builder()