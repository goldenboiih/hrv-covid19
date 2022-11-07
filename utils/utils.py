import pandas as pd
import streamlit as st

@st.cache
def load_data(data_path: str):
    data = pd.read_csv(data_path)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data