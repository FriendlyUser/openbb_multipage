import streamlit as st
from openbb_terminal.etf.stockanalysis_model import symbols

etf_symbols = symbols()

st.write(etf_symbols)