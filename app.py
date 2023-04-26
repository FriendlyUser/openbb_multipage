import streamlit as st
import os
import sys
import dotenv
import shutil

def remove_existing_file():
    stream = os.popen('cd ~ && pwd')
    root_dir = stream.read()
    if os.path.exists(os.path.join(root_dir.strip(), ".openbb_terminal", ".env")) == False:
        # copy .env file to new path
        # get python script runtime path
        runtime_path = os.path.dirname(os.path.realpath(__file__))
        print(runtime_path)
        shutil.copyfile(os.path.join(runtime_path, ".env"), os.path.join(root_dir.strip(), ".openbb_terminal", ".env"))
remove_existing_file()
st.write("""
# Technical Analysis Web Application
Leveraging the openbb sdk, we can build a web application to display 
technical analysis graphs for any stock.
""")