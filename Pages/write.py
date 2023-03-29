import streamlit as st
import os

file = ""
def clear():
    st.session_state["text"] = ""
    
def submit():
    st.session_state.something = st.session_state.text
    st.session_state.text = ''
    with open(f"{file}.txt","w") as f:
        f.write(st.session_state.something)

def app():
    st.header('Net Server Write Page')

    # st.subheader("")
    
    text = ""
    count=0
    global file
    file = st.text_input("Enter server name",key="server")

    if 'Enter message here' not in st.session_state:
        st.session_state.something = ''
    if file:
        if os.path.isfile(f"{file}.txt"):
            st.success("Connected to db")    
            message = st.text_input("Enter message here",key="text", on_change=submit)
            if message:
                submit()
        else:
            st.error("Server not found!") 