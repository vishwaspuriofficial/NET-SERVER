import streamlit as st
from Page import home
from Page import main

# Custom imports
from pages import MultiPage

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Home", home.app)
# The main app
app.run()