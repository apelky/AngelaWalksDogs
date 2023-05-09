'''
home.py

Author: Angela Pelky
Last Edit: 05/06/2023
Description: Home page of the multipage app, AngelaWalksDogs. Users will be routed to the page by default. Purpose of this page is to inform the user
about Angela and the services that she provides. 

----------------------------------------

Sources: https://github.com/Sven-Bo/digital-resume-template-streamlit
'''

from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "main.css"

# -------------------------------------------------------------------------------------------------------------------------------------
# In this section you can personalize your page by modifying anything in quotation marks.

# Title displayed on the page.
PAGE_TITLE = "Angela Walks Dogs"

# Description written under the title.
DESCRIPTION = '''Hi! My name is Angela, and I an animal lover through and through! 
I am a responsible student at the University of Oregon looking to spend time with dogs. I have a wonderful pup of my own 
named Lacy, and I have a lot of experience dog walking and pet sitting. I can’t wait to meet your amazing pet. I know how dear they are
to your heart, so I will be sure to take amazing care of them :)'''

# Fill in whatever contact information you'd like to display. If you say a name inside ": :" like ":envelope:", that represents an emoji.
# To see a full list of emoji shortcodes, follow this link: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
CONTACT = [
    ":envelope: contact.angelawalksdogs@gmail.com", 
    ":calling:214-984-8144"
]

# Include whatever social media links you'd like to display. Please note that if you add a new link it must match the format listed
# below. For example, if I wanted to add a link for TikTok, it would look like
# SOCIAL_MEDIA = {
#    "LinkedIn" : "https://www.linkedin.com/in/angela-pelky/",
#    "Instagram" : "https://www.instagram.com/contact.angelawalksdogs/",
#    "TikTok" : "https://mytiktokurl.com"
#}
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/angela-pelky/",
    "Instagram" : "https://www.instagram.com/contact.angelawalksdogs/"
}

# Describe your offerings here.
OFFERINGS = [
    ''':woman-running: Walks: When you book a walk with me, I will take your pup on a 20-minute or 30-minute walk. These walks are fast
    -paced in order to ensure you pup gets the exercise and mental stimulation they need.''',
    ''':house: Drop-In Visits: When you book a drop-in visit with me, I make sure to give your fur baby the love and attention they 
    need. These 20 or 30 minute drop-in visits include play time, potty time, and feeding time!'''
]

# Describe your experience here. If you'd like your next line to be a bullet point, make sure to inlcue the "-" at the beginning of
# your sentence.
EXPERIENCE = """
    - 4 years of dog walking experience 
    - 200+ 5:star: reviews
    - Garaunteed 1+ mile travelled per walk
"""

# Modiciations stop here. Do not alter anything past this line.
# -------------------------------------------------------------------------------------------------------------------------------------

# Setting the format for the page
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

# Opening profile picture
IMAGE = Image.open('home.png')

# Displaying title and image data side-by-side
col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(IMAGE, width=350)
with col2:
    st.title(PAGE_TITLE)
    st.write(DESCRIPTION)

# Displaying social media in a horizontal format
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for i, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f"[{platform}]({link})")

# Displaying experience as bulletted list
st.write('#')
st.subheader("Experience & Specialties")
st.write(EXPERIENCE)

# Displaying services provided 
st.write("#")
st.subheader("Offerings")
for offering in OFFERINGS:
    st.write(offering)

# Displaying contact information
st.write("#")
st.subheader("Questions?")
st.write('#')
cols = st.columns(len(CONTACT))
for i, c in enumerate(CONTACT):
    cols[i].write(c)

# Initalizing session state objects
if 'username' not in st.session_state:
    st.session_state['username'] = ''

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"