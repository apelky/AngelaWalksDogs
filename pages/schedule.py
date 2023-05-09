'''
schedule.py last edited on May 8th.

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
import webbrowser as wb

from pathlib import Path
from Authenticator import main_auth
from UserManager import add_userdata

# -------------------------------------------------------------------------------------------------------------------------------------
# Modify STRIPE_CHECKOUT with you won Stripe Checkout links

DEFAULT = 'America/Los_Angeles'
STRIPE_CHECKOUT_60 = 'https://buy.stripe.com/test_fZe6oU3UT3EK3pC8wy'
STRIPE_CHECKOUT_30 = 'https://buy.stripe.com/test_dR6bJeezxdfkd0c7sv'
STRIPE_CHECKOUT_20 = 'https://buy.stripe.com/test_8wMaFadvt2AG1hufYY'

# Stop modification
# -------------------------------------------------------------------------------------------------------------------------------------

# Import style and format
current_dir = Path('pages').parent
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)


# event dictionary is sent to Google Calendar
event = {}

# Helper function that asks the user how long they'd like their service to be.
def duration():
    duration = st.radio(
# -------------------------------------------------------------------------------------------------------------------------------------
# Modify prices and times to match specific needs
        "Select service length",
        ["20 Minutes - $15", "30 Minutes - $20", "60 Minutes - $30"],
# End modification
# -------------------------------------------------------------------------------------------------------------------------------------
        horizontal=True
    )
    return duration[:2]

# Helper function that opens Stripe Page once button is clicked
def open_browser(duration):
# -------------------------------------------------------------------------------------------------------------------------------------
# Length of service paired with Stripe Checkout links
    if duration == '20':
        wb.open(STRIPE_CHECKOUT_20)
    elif duration == '30':
        wb.open(STRIPE_CHECKOUT_30)
    elif duration == '60':
        wb.open(STRIPE_CHECKOUT_60)
# End modification
# -------------------------------------------------------------------------------------------------------------------------------------


# Helper function that asks the user which day they'd like their service to be on.
def schedule():
    d = st.date_input(
        'Select a day',
        datetime.datetime.now()
        )
    return d


# Helper function that asks the user what time they'd like their service to occur at.
def time():
    t = st.time_input('See calendar, select a time when I am not already "busy"', datetime.time(9, 00))
    return t

# Authenticate user 
if st.session_state["username"] == '':
    st.warning("Welcome to the Schedule Page! If you haven't yet, please login.")
    st.stop()
else:
    # Embed calendar for viewing within my app
    components.html(
#-------------------------------------------------------------------------------------------------------------------------------------
# Replace with Google Calendar link
        """
        <iframe src="https://embed.styledcalendar.com/#Vtfe1NOESzQO771n1k10" title="Styled Calendar" class="styled-calendar-container" 
        style="width: 100%; border: none;" data-cy="calendar-embed-iframe"></iframe>
        <script async type="module" src="https://embed.styledcalendar.com/assets/parent-window.js"></script>
        """, width=750,height=500,scrolling=True
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------
    )

    # prompt user for various information
    option = st.selectbox(
#-------------------------------------------------------------------------------------------------------------------------------------
# Modify the type of service to fit your needs
        'What kind of service would you like to book?',
        ('Walk', 'Drop-In')
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------
    )

    get_user = st.text_input(
        'Enter your username'
    )

    get_name = st.text_input(
#-------------------------------------------------------------------------------------------------------------------------------------
# Replace with relevant information
    "Enter your pet's name"
    )
# DELETE if location not needed
    get_location = st.text_input(
    'Enter your address'
    )
# Replace with the prompt you'd like the user to provide
    get_notes = st.text_input(
    'Enter any access instructions I would need to get inside the home. For example: the access code is xyz or I left the key under the mat!'
    )
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------

    r_duration = duration()

    # Helper function that builds the event dictionary in preparation for calling the Google Calendar API.
    def schedule_builder(w_or_drop):
        r_day = schedule()
        r_time = time()

        # must convert it to a full datetime object before adding the duration
        datetime_obj = (datetime.datetime.combine(r_day, r_time))
        # add the duration to the start time to create an end time
        end_time = (datetime_obj + datetime.timedelta(minutes=int(r_duration)))
        # convert our start and end time to match Google Calendar requirements
        datetime_obj = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S-07:00')
        end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S-07:00')

        event['summary'] = w_or_drop+get_name
#-------------------------------------------------------------------------------------------------------------------------------------
# DELETE if deleted lines 127-130
        event['location'] = get_location
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------
        event['description'] = get_notes
        event['start'] = {'dateTime': datetime_obj, 'timeZone':DEFAULT}
        event['end'] = {'dateTime': end_time, 'timeZone':DEFAULT}

        return event

#-------------------------------------------------------------------------------------------------------------------------------------
# Set option equal to corresponding changes on line 55
    if option == 'Walk':
        event = schedule_builder('Walk with ')
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------
        run = st.button('Proceed to Payment')

        if run:
            open_browser(r_duration)
            st.write(main_auth(event))
            add_userdata(get_user,event)

#-------------------------------------------------------------------------------------------------------------------------------------
# Set option equal to corresponding changes on line 55
    if option == 'Drop-In':
        event = schedule_builder('Drop-In with ')
# End modification
#-------------------------------------------------------------------------------------------------------------------------------------
        run = st.button('Proceed to Payment')

        if run:
            open_browser(r_duration)
            st.write(main_auth(event))
            add_userdata(get_user, event)