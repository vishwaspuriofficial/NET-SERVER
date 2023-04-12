import streamlit as st
from Pages import home
from Pages import main
from Pages import write

# Custom imports
from pages import MultiPage

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Main", main.app)
app.add_page("Write", write.app)
# The main app
app.run()