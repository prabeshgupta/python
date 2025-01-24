import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model
with open(os.path.join(os.path.dirname(__file__),'trained_model.pkl'), 'rb') as file:
    loaded_model = pickle.load(file)

# Load the scaler
with open(os.path.join(os.path.dirname(__file__), 'scaler.pkl'), 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
st.title("House Charges Prediction")
st.write("Enter the details below to predict house charges.")

# User input
gr_liv_area = st.number_input("Garage Area",min_value=0.0, max_value=10000.0, value=1000.0, step=100.0)
overall_quality = st.number_input("Over All Quality",min_value=0.0, max_value=10.0, value=5.0, step=0.5)
garage_cars = st.number_input("Cars fit in Garage", min_value=0, max_value=10, value=0, step=1)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000, step=1)

# Predict button
if st.button("Predict Charges"):
    # Prepare the custom data
    custom_data = np.array([gr_liv_area, overall_quality, garage_cars,year_built]).reshape(1, -1)

    # Scale the custom data
    custom_data_scaled = scaler.transform(custom_data)

    # Make the prediction
    y_pred_custom = loaded_model.predict(custom_data_scaled)

    # Display the result
    st.write(f"Predicted House Charges: ${y_pred_custom[0]:.2f}")