import streamlit as st
import pandas as pd
from openbb_terminal.etf.stockanalysis_model import get_all_names_symbols

etf_symbols = get_all_names_symbols()
etf_dict = {'Symbols': etf_symbols[0], 'Names': etf_symbols[1]}
etf_df = pd.DataFrame(etf_dict)
st.write(etf_df)