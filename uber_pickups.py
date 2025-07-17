import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in Coimbatore")
st.subheader("Real-time Data")
DATA_URL='other-American_B01362.csv'

@st.cache_data
def load_data(nrows):
  data=pd.read_csv(DATA_URL, nrows=nrows)
  # Convert TIME column to datetime to extract hour information
  data['TIME'] = pd.to_datetime(data['TIME'], format='%I:%M:%S %p')
  return data

data_load_state=st.text('Loading data...')
data=load_data(1000)
st.write(data)
data_load_state.text('Loading data...done!')
st.subheader("Data Overview")
TIME='TIME'
hist_values=np.histogram(data[TIME].dt.hour,bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour',0,23,17)
filtered_data=data[data[TIME].dt.hour==hour_to_filter]

st.subheader(f'Map all the pickups at {hour_to_filter}:00')
st.write(filtered_data)






  