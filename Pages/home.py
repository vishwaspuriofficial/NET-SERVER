import streamlit as st

file=""

def startServer():
    global file
    with open(file+".txt","w") as f:
        pass
    st.change_page("main")

a = st.button("Start server")

if a:
    file = st.text_input("Enter server name",key="server")
    # if file:
    #     startServer()