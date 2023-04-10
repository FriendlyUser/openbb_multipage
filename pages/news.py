import streamlit as st
from openbb_terminal.common.feedparser_model import get_news

def fetch_news(keyword):
    # This is where you would call a news API or scrape a news website
    # to get news articles related to the user's keyword
    # For this example, we'll just return a string with the keyword
    return get_news(keyword)

# Create a text input and store the user's input in a variable
user_input = st.text_input("Enter a keyword to search for news articles")

# Call the get_news function with the user's input and display the results
if user_input:
    news = get_news(user_input)
    st.write(news)