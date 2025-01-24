import os
import streamlit as st
import numpy as np
import pickle

# Load the trained model
#Gets the folder where your script (app.py) is located and then add trained_model.pkl to it.
model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

# Load the pre-fitted scaler
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
st.title("Insurance Charges Prediction")
st.write("Enter the details below to predict insurance charges.")

# User input
age = st.number_input("Age", min_value=18, max_value=100, value=18, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1)

# Predict button
if st.button("Predict Charges"):
    # Prepare the custom data
    custom_data = np.array([age, bmi, children]).reshape(1, -1)

    # Scale the custom data using the pre-fitted scaler
    custom_data_scaled = scaler.transform(custom_data)

    # Make the prediction
    y_pred_custom = loaded_model.predict(custom_data_scaled)

    # Display the result
    st.write(f"Predicted Insurance Charges: ${y_pred_custom[0]:.2f}")