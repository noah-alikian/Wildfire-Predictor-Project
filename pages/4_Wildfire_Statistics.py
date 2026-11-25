import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Wildfire Statistics')
st.text('This page provides some interesting statistics and data visualizations for wildfires in California.')
st.subheader('Counties with Most Fires')
st.image('county_fires.svg', use_container_width = True)
st.caption('Counties with the highest count of fires')
st.subheader('Average Max Temperature for Days With or Without a Fire')
st.image('temp_diff.svg', use_container_width = True)
st.caption('Temperature difference on days with a fire and without a fire')
st.subheader('Trend of Fire Count Over a Year')
st.image('yearly_trend.svg', use_container_width = True)
st.caption('Yearly trend of fire frequency')
st.subheader('Yearly Count of Fires')
st.image('yearly_fires.svg', use_container_width = True)
st.caption('Count of fires over the past 12 years')

st.subheader('Biggest Fires (By Square Mileage)')
sm_burned = pd.read_csv('square_mileage.csv', index_col = 0)
st.dataframe(sm_burned)
st.caption('Top 5 fires that burned the most square mileage in the past 15 years')