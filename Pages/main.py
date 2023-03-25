import streamlit as st
import os

filename = ""
a = ""

def submit():
    global filename
    filename=str(st.session_state.server)+".txt"
    print(filename)
    startServer()

def update():
    global filename
    for i in a:
        i = i.replace("\n","")
        st.write(i)

def getDB():
    while True:
        global filename
        global a
        with open(filename,"r") as f:
            new = f.readlines()
            if a != new: 
                a = new
                update()
                
def startServer():
    global filename
    with open(filename,"w") as f:
        pass
    st.success(f"Server Connected to {filename}")
    getDB()
    
     
def stopServer():
    global filename
    os.remove(os.getcwd()+f"\{filename}")
    st.success(f"Server Disconnected")

def app():
    st.header('Net Server Main Page')

    st.subheader("")
    a = st.button("Start server")
    b = st.button("Stop server")

    if a:
        file = st.text_input("Enter server name",key="server", on_change=submit)

    if b:
        stopServer()