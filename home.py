'''
home.py last edited on ?.

Angela Pelky

This is a home page where users can learn about me and get to know me better.
----------------------------------------

home.py uses Python 3.10
'''

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Angela Walks Dogs",
    page_icon="",
)

st.markdown("# Meet your walker! 👋")

st.sidebar.success("Select a page to navigate to above")

image = Image.open('home.jpg')

st.image(image, caption=None, width=300, 
use_column_width="auto", clamp=False, channels="RGB", 
output_format="auto")

st.write("""Hi! My name is Angela, and I an animal lover through 
and through! I am a responsible student at the University of Oregon 
looking to spend time with dogs. I have a wonderful pup of my own 
named Lacy, and I have a lot of experience dog walking and pet sitting. 
Also, I’m a vegetarian if that helps give insight to how much I love 
animals! I can’t wait to meet your amazing dog. I know how dear they are
to your heart, so I will be sure to take 
amazing care of them :)""")