import streamlit as st
import os

stream = os.popen('cd ~ && pwd')
root_dir = stream.read()
# check for .openbb_terminal/env in root_dir
if os.path.exists(os.path.join(root_dir.strip(), ".openbb_terminal", ".env")) == False:
    print("Did not find .openbb_terminal/.env")
    # create it
    os.mkdir(os.path.join(root_dir.strip(), ".openbb_terminal"))
    # make .env file
    env_file = open(os.path.join(root_dir.strip(), ".openbb_terminal", ".env"), "w")

st.write("""
# Technical Analysis Web Application
Leveraging the openbb sdk, we can build a web application to display 
technical analysis graphs for any stock.
""")