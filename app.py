 # Creates an empty Streamlit UI file
import streamlit as st
import requests

st.title("SMA Electrical Resistance Predictor")

# Input fields
temperature = st.number_input("Temperature (°C)", min_value=20.0, max_value=120.0, value=50.0)
stress = st.number_input("Stress (MPa)", min_value=0.0, max_value=500.0, value=200.0)
phase_fraction = st.slider("Phase Fraction", min_value=0.0, max_value=1.0, value=0.5)

# API URL
api_url = "http://127.0.0.1:5000/predict"  # Ensure your backend is running

if st.button("Predict Resistance"):
    # Send request to Flask API
    data = {"Temperature_C": temperature, "Stress_MPa": stress, "Phase_Fraction": phase_fraction}
    response = requests.post(api_url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Electrical Resistance: {result['Predicted_Resistance_Ohms']:.4f} Ω")
    else:
        st.error("Error in prediction. Ensure the API is running.")
