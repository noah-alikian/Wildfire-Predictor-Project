import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Wildfire Prediction App')
st.image('Wildfire.jpg')
st.text('Welcome to the home page!')

with st.expander('App Functions'):
    st.markdown('This app allows a user to click anywhere on a map of California and see the probability of ' \
    'a wildfire occurring at that location. It also provides insights on the selected model as well as data visualizations ' \
    'displaying historical statistics about wildfires in California. Finally, the app introduces information on what to do in ' \
    'case a wildfire happens in your community.')


st.sidebar.markdown('- **Home:** This page introduces the app to the user')
st.sidebar.markdown('- **Model Types:** This page presents each process used by the model to make its predictions')
st.sidebar.markdown('- **Prediction Map:** This page is where you go to see wildfire probabilities based on latitude and longitude')
st.sidebar.markdown('- **Model Insights:** This page displays visualizations depicting the performance of each model')
st.sidebar.markdown('- **Wildfire Statistics:** This page uses historical data to develop unique statistics about wildfires in California')
st.sidebar.markdown('- **Wildfire Information:** This page introduces different ways to prepare for a wildfire as well as ways to prevent wildfires from occurring')