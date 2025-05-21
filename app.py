import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('crop_model.pkl')

# Title
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and weather details to get a crop suggestion.")

# Input sliders
n = st.slider("Nitrogen (N)", 0, 140, 90)
p = st.slider("Phosphorus (P)", 5, 145, 42)
k = st.slider("Potassium (K)", 5, 205, 43)
temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 10.0, 100.0, 80.0)
ph = st.slider("pH", 3.5, 9.5, 6.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 200.0)

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
