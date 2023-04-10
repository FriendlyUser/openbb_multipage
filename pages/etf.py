import streamlit as st
from openbb_terminal.etf.stockanalysis_model import get_all_names_symbols

etf_symbols = get_all_names_symbols()

st.write(etf_symbols)