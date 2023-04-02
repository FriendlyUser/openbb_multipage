import streamlit as st
from openbb_terminal.economy.wsj_model import market_overview, us_indices, us_bonds, top_commodities, global_bonds, global_currencies

# openbb.economy.overview
# openbb.economy.indices
# openbb.economy.usbonds
# openbb.economy.glbonds
# openbb.economy.currencies
def openbb_economy():
    """Open the Blackboard website in the default web browser."""
    economy_dfs = []
    file_names = []
    # append two entries to economy dfs from top_commodities and us_bonds
    economy_dfs.append(top_commodities())
    file_names.append("top_commodities")
    economy_dfs.append(us_bonds())
    file_names.append("us_bonds")
    economy_dfs.append(us_indices())
    file_names.append("us_indices")
    economy_dfs.append(global_bonds())
    file_names.append("global_bonds")
    economy_dfs.append(global_currencies())
    file_names.append("global_currencies")
    economy_dfs.append(market_overview())
    file_names.append("market_overview")

    return economy_dfs, file_names

economy_dfs, file_names = openbb_economy()

# output all economy tables with labels above
for i in range(len(economy_dfs)):
    st.write(f"# {file_names[i]}")
    st.write(economy_dfs[i])