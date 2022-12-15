import streamlit as st
from pathlib import Path
import pandas as pd
import pickle
from datetime import date

st.title('🌧️ Predicting Tomorrow\'s Rain')

with open(str(Path(__file__).parents[1]) + '/models/tommorow_rain_classifier.pkl', 'rb') as file:
  model = pickle.load(file)
    
@st.cache
def predict(location, rainfall, humidity_3pm, rain_today):
  return model.predict(pd.DataFrame([[location, rainfall, humidity_3pm, rain_today]],
                                    columns=('Location', 'Rainfall', 'Humidity3pm', 'RainToday')))

location_options = {
  0: 'Adelaide',
  1: 'Albury',
  2: 'AliceSprings',
  3: 'BadgerysCreek',
  4: 'Ballarat',
  5: 'Bendigo',
  6: 'Brisbane',
  7: 'Cairns',
  8: 'Canberra',
  9: 'Cobar',
  10: 'CoffsHarbour',
  11: 'Dartmoor',
  12: 'Darwin',
  13: 'GoldCoast',
  14: 'Hobart',
  15: 'Katherine',
  16: 'Launceston',
  17: 'Melbourne',
  18: 'MelbourneAirport',
  19: 'Mildura',
  20: 'Moree',
  21: 'MountGambier',
  22: 'MountGinini',
  23: 'Nhil',
  24: 'NorahHead',
  25: 'NorfolkIsland',
  26: 'Nuriootpa',
  27: 'PearceRAAF',
  28: 'Penrith',
  29: 'Perth',
  30: 'PerthAirport',
  31: 'Portland',
  32: 'Richmond',
  33: 'Sale',
  34: 'SalmonGums',
  35: 'Sydney',
  36: 'SydneyAirport',
  37: 'Townsville',
  38: 'Tuggeranong',
  39: 'Uluru',
  40: 'WaggaWagga',
  41: 'Walpole',
  42: 'Watsonia',
  43: 'Williamtown',
  44: 'Witchcliffe',
  45: 'Wollongong',
  46: 'Woomera',
}
wind_gust_dir_options = {
  0: 'E',
  1: 'ENE',
  2: 'ESE',
  3: 'N',
  4: 'NE',
  5: 'NNE',
  6: 'NNW',
  7: 'NW',
  8: 'S',
  9: 'SE',
  10: 'SSE',
  11: 'SSW',
  12: 'SW',
  13: 'W',
  14: 'WNW',
  15: 'WSW',
}
bool_options = {0: 'No', 1: 'Yes'}

# _date = st.date_input('Date (YYYY/MM/DD):', date.today())
location = st.selectbox('Location:', options=list(location_options.keys()), format_func=lambda x: location_options[x])
rainfall = st.number_input('Rainfall (mm):', min_value=0.0)
# wind_gust_dir = st.selectbox('Wind Gust Direction:', options=list(wind_gust_dir_options.keys()), format_func=lambda x: wind_gust_dir_options[x])
# wind_gust_speed = st.number_input('Wind Gust Speed (km/h):', min_value=0.0)
# wind_speed_3pm = st.number_input('Wind Speed at 3pm (km/h):', min_value=0.0)
humidity_3pm = st.slider('Humidity at 3pm:', 0, 100, format='%f%%')
# temp_3pm = st.number_input('Temperature at 3pm (°C):', min_value=0.0)
rain_today = st.radio('Is Today Raining?', horizontal=True, options=list(bool_options.keys()), format_func=lambda x: bool_options[x])

if st.button('Predict'):
  prediction = predict(location, rainfall, humidity_3pm, rain_today)
  
  if prediction[0]:
    st.success('It will rain tomorrow.')
  else:
    st.warning('It will not rain tomorrow.')