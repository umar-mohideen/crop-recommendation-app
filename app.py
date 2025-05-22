import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('crop_model.pkl')

# Title
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and weather details to get a crop suggestion.")

# Input boxes
n = st.number_input("Nitrogen (N)", min_value=0, max_value=140, value=90)
p = st.number_input("Phosphorus (P)", min_value=5, max_value=145, value=42)
k = st.number_input("Potassium (K)", min_value=5, max_value=205, value=43)
temperature = st.number_input("Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=80.0)
ph = st.number_input("pH", min_value=3.5, max_value=9.5, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0, value=200.0)

# Predict button
if st.button("Predict Crop"):
    input_data = pd.DataFrame([{
        'N': n,
        'P': p,
        'K': k,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }])
    
    prediction = model.predict(input_data)
    st.success(f"🌱 Recommended Crop: **{prediction[0]}**")
