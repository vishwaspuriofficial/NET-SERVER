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
    st.success("Server Created")
    getDB()
    
     
def stopServer():
    os.remove(filename)

a = st.button("Start server")
b = st.button("Stop server")
if a:
    file = st.text_input("Enter server name",key="server", on_change=submit)
        

if b:
    stopServer()