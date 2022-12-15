import streamlit as st
from pathlib import Path
import pandas as pd
import pickle

st.title('🚕 Predicting Lyft and Uber Price')

cab_type_options = {0: 'Lyft', 1: 'Uber'}
ride_type_options = ['Black', 'Black SUV', 'Lux', 'Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL', 'Shared', 'UberPool', 'UberX', 'UberXL', 'WAV']

with open(str(Path(__file__).parents[1]) + '/models/lyft_uber_price_regressor.pkl', 'rb') as file:
  model = pickle.load(file)
    
@st.cache
def predict(distance, surge_multiplier, visibility, cab_type, ride_type):
  input = [distance, surge_multiplier, visibility]
  
  for i in range(0, len(cab_type_options)):
    input.append(1.0 if cab_type_options[i] == cab_type else 0.0)
    
  for i in range(0, len(ride_type_options)):
    input.append(1.0 if ride_type_options[i] == ride_type else 0.0)

  return model.predict(pd.DataFrame([input],
                                    columns=('distance', 'surge_multiplier', 'visibility', 'cab_type_Lyft', 'cab_type_Uber', 'name_Black', 'name_Black SUV', 'name_Lux', 'name_Lux Black', 'name_Lux Black XL', 'name_Lyft', 'name_Lyft XL', 'name_Shared', 'name_UberPool', 'name_UberX', 'name_UberXL', 'name_WAV')))

distance = st.number_input('Distance (mile):', min_value=0.0)
surge_multiplier = st.slider('Surge Multiplier:', 0.0, 3.0)
visibility = st.slider('Visibility:', 0.0, 10.0)
cab_type = st.radio('Cab Type:', horizontal=True, options=list(cab_type_options.keys()), format_func=lambda x: cab_type_options[x]) 
ride_type = st.selectbox('Ride Type:', ride_type_options)


if st.button('Predict'):
  prediction = predict(distance, surge_multiplier, visibility, cab_type, ride_type)
  
  print(prediction)
  if prediction[0]:
    st.success(f'Your estimated price for the ride is ${prediction[0]:.2f}.')