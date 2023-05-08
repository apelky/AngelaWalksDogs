'''
schedule.py last edited on ?.

Angela Pelky

This acts as a page of my web app that prompts the user to schedule a service and adds it to my calendar.
Please note that this is a prototype, and some of the questions prompted such as address and key code could be compromisable.
Upon release of this app please ensure that all security measures have been met. Furthermore, this schedule does not include the need
for driving time between bookings. It would also be nice if I could find a way to make Google Calendar look nicer. Another possible addition
is to make sure that the person pays by deleting the event if payment is not processed using the Stripe API. This program calls 
upon the helper progam Authenticator.py to build the Google Calendar and insert an event into it.

----------------------------------------

schedule.py uses Python 3.10
'''

import streamlit as st
import datetime
import streamlit.components.v1 as components
#from streamlit_extras.switch_page_button import switch_page

from Authenticator import main_auth
from user_manager import add_userdata

DEFAULT = 'America/Los_Angeles'
STRIPE_CHECKOUT = 'https://buy.stripe.com/test_dR69B6bnldfk3pC8wx'

# event dictionary is sent to Google Calendar
event = {}


# Helper function that asks the user how long they'd like their service to be.
# Parameters: None
# Return: Duration(string)
def duration():
    duration = st.selectbox(
        'Select a duration',
        ('20 Minutes - $15', '30 Minutes - $20', '60 Minutes - $30')
    )
    return duration[:2]


# Helper function that asks the user which day they'd like their service to be on.
# Parameters: None
# Return: d(datetime.date)
def schedule():
    d = st.date_input(
        'Select a day',
        datetime.datetime.now()
        )
    return d


# Helper function that asks the user what time they'd like their service to occur at.
# Parameters: None
# Return: t(datetime.time)
def time():
    t = st.time_input('See calendar, select a time when I am not already "busy"', datetime.time(9, 00))
    return t

# Helper function that prints out confirmation messages.
# Parameters: None
# Returns: None
def next_steps():
    st.markdown(
    f'<a href={STRIPE_CHECKOUT} class="button">👉 Complete booking with payment</a>',
    unsafe_allow_html=True,
    )
    st.write('Once payment has been received you can navigate to the login page to see your confirmed booking!')

# embed calendar for viewing within my app
components.html(
    """
    <iframe src="https://embed.styledcalendar.com/#Vtfe1NOESzQO771n1k10" title="Styled Calendar" class="styled-calendar-container" style="width: 100%; border: none;" data-cy="calendar-embed-iframe"></iframe>
<script async type="module" src="https://embed.styledcalendar.com/assets/parent-window.js"></script>
    """, width=750,height=500,scrolling=True
)

# prompt user for various information
option = st.selectbox(
    'What kind of service would you like to book?',
    ('Walk', 'Drop-In')
)

registered = st.selectbox("Are you a registered user?", ('Yes', 'No'))
if registered == 'Yes':
    get_user = st.text_input(
    'Enter your username'
    )
else:
    "Please register on the 'login' page before scheduling a service with me if you'd like to have increased functionality such as viewing your booked walks on the booked page" 

get_name = st.text_input(
  "Enter your pet's name"
)

get_location = st.text_input(
  'Enter your address'
)

get_notes = st.text_input(
  'Enter any access instructions I would need to get inside the home. For example: the access code is xyz or I left the key under the mat!'
)


# Helper function that builds the event dictionary in preparation for calling the Google Calendar API.
# Parameters: w_or_drop(str)
# Return: event(dict)
def schedule_builder(w_or_drop):
    r_duration = duration()
    r_day = schedule()
    r_time = time()

    # must convert it to a full datetime object before adding the duration
    datetime_obj = (datetime.datetime.combine(r_day, r_time))
    # add the duration to the start time to create an end time
    end_time = (datetime_obj + datetime.timedelta(minutes=int(r_duration)))
    # convert our start and end time to match Google Calendar requirements
    datetime_obj = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S-08:00')
    end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S-08:00')

    event['summary'] = w_or_drop+get_name
    event['location'] = get_location
    event['description'] = get_notes
    event['start'] = {'dateTime': datetime_obj, 'timeZone':DEFAULT}
    event['end'] = {'dateTime': end_time, 'timeZone':DEFAULT}

    return event

if option == 'Walk':
    event = schedule_builder('Walk with ')
    run = st.button('Done')

    if run:
        confirmation = main_auth(event)
        st.write(confirmation)
        next_steps()
        add_userdata(get_user,event)

if option == 'Drop-In':
    event = schedule_builder('Drop-In with ')
    run = st.button('Done')

    if run:
        confirmation = main_auth(event)
        st.success(confirmation)
        next_steps()
        add_userdata(get_user, event)