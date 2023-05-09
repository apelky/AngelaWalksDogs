'''
Authenticator.py last edited on May 9.

Angela Pelky

This is the helper progam Authenticator.py to used to authenticate users and build the Google Calendar in order to insert an event into it.

----------------------------------------

Authenticator.py uses Python 3.10
'''

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Our scope is to read, write, and edit the 'Angela Walks Dogs' calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main_auth(event):
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes 
    # for the first time. Remove this file if an expiration message shows up.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Build our calendar
        service = build('calendar', 'v3', credentials=creds, cache_discovery=False)

        # Call the Calendar API
#-------------------------------------------------------------------------------------------------------------------------------------
# In this section you can modify the caledarID and the return message.
        event = service.events().insert(calendarId='contact.angelawalksdogs@gmail.com', body=event).execute()
        return_message = 'Your event has been created. Thank you for choosing Angela Walks Dogs!'
# Stop modifications here.
#-------------------------------------------------------------------------------------------------------------------------------------
    except HttpError as error:
        return_message = 'An error occurred: %s' % error
    return return_message
