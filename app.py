import streamlit as st
import os
import dotenv
from openbb_terminal.core.config.paths import SETTINGS_ENV_FILE

stream = os.popen('cd ~ && pwd')
root_dir = stream.read()
# check for .openbb_terminal/env in root_dir
if os.path.exists(os.path.join(root_dir.strip(), ".openbb_terminal", ".env")) == False:
    print("Did not find .openbb_terminal/.env")
    # create it
    os.mkdir(os.path.join(root_dir.strip(), ".openbb_terminal"))
    # make .env file
    env_file = open(os.path.join(root_dir.strip(), ".openbb_terminal", ".env"), "w")
    # dotenv.set_key(SETTINGS_ENV_FILE, "PLOT_ENABLE_PYWRY", "0")
    dotenv.set_key(SETTINGS_ENV_FILE,"OPENBB_PLOT_ENABLE_PYWRY", 0)

st.write("""
# Technical Analysis Web Application
Leveraging the openbb sdk, we can build a web application to display 
technical analysis graphs for any stock.
""")