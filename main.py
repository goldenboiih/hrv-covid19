import streamlit as st
import pandas as pd
import numpy as np

# https://docs.streamlit.io/library/get-started/create-an-app


@st.cache
def load_data(data_path: str, nrows: int):
    data = pd.read_csv(data_path, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

st.title('Covid-19 Data Visualisation')
st.sidebar.markdown("Covid-19 Data Visualisation")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
participants_df = load_data("data/participants.csv", 10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done loading! (using st.cache)")

st.subheader("Participants")
participants_df