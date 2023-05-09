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


PAGE_TITLE = "Angela Walks Dogs"
PAGE_ICON = ":dog:"
NAME = "Angela Pelky"
DESCRIPTION = '''Hi! My name is Angela, and I an animal lover through and through! 
I am a responsible student at the University of Oregon looking to spend time with dogs. I have a wonderful pup of my own 
named Lacy, and I have a lot of experience dog walking and pet sitting. I can’t wait to meet your amazing pet. I know how dear they are
to your heart, so I will be sure to take amazing care of them :)'''
CONTACT = [
    ":envelope: contact.angelawalksdogs@gmail.com", 
    ":calling:214-984-8144"
]
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/angela-pelky/",
    "Instagram" : "https://www.instagram.com/contact.angelawalksdogs/"
}
OFFERINGS = [
    ":woman-running: Walks: When you book a walk with me, I will take your pup on a 20-minute or 30-minute walk. These walks are fast-paced in order to ensure you pup gets the exercise and mental stimulation they need.",
    ":house: Drop-In Visits: When you book a drop-in visit with me, I make sure to give your fur baby the love and attention they need. These 20 or 30 minute drop-in visits include play time, potty time, and feeding time!"
]

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

IMAGE = Image.open('home.png')

col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(IMAGE, width=350)
with col2:
    st.title(PAGE_TITLE)
    st.write(DESCRIPTION)

st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for i, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f"[{platform}]({link})")

st.write('#')
st.subheader("Experience & Specialties")
st.write(
    """
    - 4 years of dog walking experience 
    - 200+ 5:star: reviews
    - Garaunteed 1+ mile travelled per walk
    """
)

st.write("#")
st.subheader("Offerings")
for offering in OFFERINGS:
    st.write(offering)

st.write("#")
st.subheader("Questions?")
col1,col2 = st.columns(2, gap="small")
with col1:
    st.write(CONTACT[0])
with col2:
    st.write(CONTACT[1])

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"