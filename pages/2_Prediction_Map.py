import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import sklearn
import folium
from streamlit_folium import st_folium
import openmeteo_requests
import requests_cache
import pgeocode
from datetime import date, timedelta

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from xgboost import XGBClassifier

import warnings
import pickle
warnings.filterwarnings('ignore')

model = st.sidebar.radio('Select Model:', options = ['AdaBoost', 'Random Forest', 'XGBoost', 'Ensemble Voting'])

@st.cache_resource
def load_model(file):
    x = open(file, 'rb')
    y = pickle.load(x)
    x.close()
    return y

ada_ml = load_model('ada_ml.pickle')
rf_ml = load_model('rf_ml.pickle')
xg_ml = load_model('xg_ml.pickle')
ensemble_ml = load_model('ensemble_ml.pickle')

st.title('Prediction Map')
st.text('This page allows users to select anywhere in California and see the probability of a wildfire occurring there. ' \
'This prediction is made based off of recent climate data pulled from an open-source API.')

@st.cache_resource
def get_map():
    map = folium.Map(location = [37.1661, -119.449], zoom_start = 6)

    folium.LatLngPopup().add_to(map)
    return map

state = st_folium(
    get_map(),
    width=800,
    height=500,
    returned_objects=["last_clicked"],  
    key="main_map",
    )

clicked = state.get('last_clicked')

zipcode = st.number_input('Input Zip Code:', value = 0, format = "%05d")
button = st.button('Use ZIP')
country_code = pgeocode.Nominatim('US')
code = country_code.query_postal_code(zipcode)

if "last_source" not in st.session_state:
    st.session_state.last_source = None
if "last_zip" not in st.session_state:
    st.session_state.last_zip = None
if "last_click" not in st.session_state:
    st.session_state.last_click = (None, None)


clicked_ok = bool(clicked) and ("lat" in clicked) and ("lng" in clicked)
zip_ok = (
    code is not None and
    pd.notna(code.latitude) and pd.notna(code.longitude) and
    32.53 <= float(code.latitude) <= 42 and -124.26 <= float(code.longitude) <= -114.08
)

if clicked_ok:
    click_tuple = (round(float(clicked["lat"]), 6), round(float(clicked["lng"]), 6))
    if click_tuple != st.session_state.last_click:
        st.session_state.last_click = click_tuple
        st.session_state.last_source = "map"

zip_str = str(zipcode).strip()
if button:
    if zip_ok:
        st.session_state.last_zip = zip_str
        st.session_state.last_source = "zip"
        st.session_state.last_click = (None, None)
    else:
        st.warning('Please enter a valid 5-digit California ZIP Code')


lat = lon = None
if st.session_state.last_source == "map":
    if clicked_ok:
        lat, lon = float(clicked["lat"]), float(clicked["lng"])

elif st.session_state.last_source == "zip":
    if zip_ok:
        lat, lon = float(code.latitude), float(code.longitude)



if lat is None or lon is None:
    st.info("Click on the map or enter a ZIP and press **Use ZIP** to get a prediction.")
else:
    st.subheader("Coordinates")
    st.write(f"Lat: **{lat:.5f}**, Long: **{lon:.5f}**")

    yesterday = date.today() - timedelta(days=1)

    def get_openmeteo_client():
        cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
        return openmeteo_requests.Client(session=cache_session)

    openmeteo = get_openmeteo_client()

    df = pd.DataFrame(columns=[
        'Elevation', 'temperature_2m_max', 'temperature_2m_min', 'daylight_duration',
        'sunshine_duration', 'uv_index_max', 'precipitation_sum',
        'precipitation_hours', 'wind_speed_10m_max', 'wind_gusts_10m_max',
        'et0_fao_evapotranspiration', 'cloud_cover_mean',
        'relative_humidity_2m_max', 'relative_humidity_2m_min',
        'surface_pressure_max', 'surface_pressure_min'
    ])

    url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
    params = {
        "latitude": float(lat),
        "longitude": float(lon),
        "start_date": yesterday.isoformat(),
        "end_date": yesterday.isoformat(),
        "daily": [
            "temperature_2m_max", "temperature_2m_min", "daylight_duration", "sunshine_duration",
            "uv_index_max", "precipitation_sum", "precipitation_hours", "wind_speed_10m_max",
            "wind_gusts_10m_max", "et0_fao_evapotranspiration", "cloud_cover_mean",
            "relative_humidity_2m_max", "relative_humidity_2m_min",
            "surface_pressure_max", "surface_pressure_min"
        ],
        "models": "best_match",
        "timezone": "America/Los_Angeles",
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()

    def get_var(idx):
        try:
            arr = list(daily.Variables(idx).ValuesAsNumpy())
            return None if len(arr) == 0 else arr[0]
        except Exception:
            return None

    row = {
        "Elevation": response.Elevation(),
        "temperature_2m_max": get_var(0),
        "temperature_2m_min": get_var(1),
        "daylight_duration": get_var(2),
        "sunshine_duration": get_var(3),
        "uv_index_max": get_var(4),
        "precipitation_sum": get_var(5),
        "precipitation_hours": get_var(6),
        "wind_speed_10m_max": get_var(7),
        "wind_gusts_10m_max": get_var(8),
        "et0_fao_evapotranspiration": get_var(9),
        "cloud_cover_mean": get_var(10),
        "relative_humidity_2m_max": get_var(11),
        "relative_humidity_2m_min": get_var(12),
        "surface_pressure_max": get_var(13),
        "surface_pressure_min": get_var(14),
    }
    df.loc[len(df)] = row

    if model == 'AdaBoost':
        probability = ada_ml.predict_proba(df)
    elif model == 'Random Forest':
        probability = rf_ml.predict_proba(df)
    elif model == 'XGBoost':
        probability = xg_ml.predict_proba(df)
    elif model == 'Ensemble Voting':
        probability = ensemble_ml.predict_proba(df)
    else:
        probability = None

    if probability is None:
        st.error("Could not compute a prediction. Check model/inputs.")
    else:
        x = float(probability[0][1])
        if x <= 0.5:
            st.success(f'**Probability of Fire Occurring:** {x*100:.2f}%')
        else:
            st.warning(f'**Probability of Fire Occurring:** {x*100:.2f}%')
    

# For this section of the project, AI assisted me with the integration of Folium mapping
# as well as the session_state usage that allowed me to add the zip code box and give users another way to find the problem
# Finally, it helped me work with the open_meteo API and process the data that it is pulling.