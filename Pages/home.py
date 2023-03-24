import streamlit as st

file=""

def startServer():
    global file
    with open(file+".txt","w") as f:
        pass
    st.experimental_set_query_params(f=file)
    # st.change_page("main")
    
    
def joinServer():
    st.experimental_set_query_params(file)
    st.change_page("join")

def app():
    st.header('Net Server Home Page')

    st.subheader("")
    join = st.button("Join server")
    start = st.button("Start server")

    if start:
        file = st.text_input("Enter server name",key="server")
        if file:
            startServer()
    if join:
        file = st.text_input("Enter server name",key="server")
        if file:
            joinServer()