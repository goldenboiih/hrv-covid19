import streamlit as st
from utils.utils import *

# https://docs.streamlit.io/library/get-started/create-an-app

st.title("Plain Data Frames")
st.sidebar.markdown("Plain Data Frames")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load all csv's into dataframes
blood_pressure_df = load_data("data/blood_pressure.csv")
hrv_measurements_df = load_data("data/hrv_measurements.csv")
participants_df = load_data("data/participants.csv")
scales_description_df = load_data("data/scales_description.csv")
sleep_df = load_data("data/sleep.csv")
surveys_df = load_data("data/surveys.csv")
wearables_df = load_data("data/wearables.csv")
weather_df = load_data("data/weather.csv")
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done loading! (using st.cache)")

st.subheader("Participants")
participants_df
st.subheader("Blood Pressure")
blood_pressure_df
st.subheader("HRV Measurements")
hrv_measurements_df
st.subheader("Scales Description")
scales_description_df
st.subheader("Sleep")
sleep_df
st.subheader("Surveys")
surveys_df
st.subheader("Wearables")
wearables_df
st.subheader("Weather")
weather_df
