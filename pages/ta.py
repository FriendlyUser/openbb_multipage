import streamlit as st
import datetime
import pandas as pd
import requests
import random
import os
from pages.utils.util import remove_existing_file
from openbb_terminal.stocks.stocks_helper import load
from openbb_terminal.common.technical_analysis.volatility_view import display_bbands, display_donchian

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

st.sidebar.header('User Input Parameters')

today = datetime.date.today()
def user_input_features():
    ticker = st.sidebar.text_input("Ticker", 'ZIM')
    start_date = st.sidebar.text_input("Start Date", '2020-05-01')
    end_date = st.sidebar.text_input("End Date", f'{today}')
    # ta_range = st.sidebar.number_input("TA Range", min_value=1, max_value=50)
    return ticker, start_date, end_date # , ta_range

symbol, start, end = user_input_features()


# append random int to file name to avoid caching
rand_int = str(random.randint(1, 500000))
ran_bbands_name = f"bbands-{rand_int}.png"
ran_donchian_name = f"donchian-{rand_int}.png"

@remove_existing_file
@st.experimental_memo
def build_bbands_img(data, symbol, window=15, n_std=2, export="bbands.png"):
    return display_bbands(data, symbol, window, n_std, export=export)


@remove_existing_file
@st.experimental_memo
def build_donchian_img(data, symbol, export="donchian.png"):
    return display_donchian(data, symbol, export=export)
company_name = symbol.upper()

start = pd.to_datetime(start)
end = pd.to_datetime(end)

# Read data 
data = load(symbol,start, 1440, end)
st.write(data)
# Adjusted Close Price
st.header(f"Adjusted Close Price\n {company_name}")
st.line_chart(data["Close"])

# get ta graph
bbands_img = build_bbands_img(data, symbol, 15, 2, ran_bbands_name)
# plot ta using open bb sdk in streamlit
st.header(f"Bollinger Bands")
# 
# if bbands.png exists, display it

if bbands_img:
    image = PIL.image(io.BytesIO(bytes(bbands_img, "utf-8")))
    st.image(bbands_img, caption='Bollinger bands chart')

donchian_img = build_donchian_img(data, symbol, ran_donchian_name)
# plot ta using open bb sdk in streamlit
st.header(f"Donchian")

if donchian_img:
    st.image(donchian_img, caption='Donchian Openbb chart') 