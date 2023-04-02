import streamlit as st

# Custom imports
from pages import MultiPage
from Pages import add, multiply, home

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Home", home.app)
# The main app
app.run()