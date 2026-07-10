import streamlit as st
import numpy as np
import pickle

# Load saved model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("🏠 House Price Prediction")

st.write("Enter House Details:")

# Inputs (MUST match training feature order)
bedrooms = st.number_input("Bedrooms", min_value=0.0)
bathrooms = st.number_input("Bathrooms", min_value=0.0)
sqft_living = st.number_input("Sqft Living", min_value=0.0)
sqft_lot = st.number_input("Sqft Lot", min_value=0.0)
floors = st.number_input("Floors", min_value=0.0)
waterfront = st.selectbox("Waterfront (0 = No, 1 = Yes)", [0, 1])
view = st.slider("View (0-4)", 0, 4)
condition = st.slider("Condition (1-5)", 1, 5)
grade = st.slider("Grade (1-13)", 1, 13)
sqft_basement = st.number_input("Sqft Basement", min_value=0.0)
lat = st.number_input("Latitude", format="%.6f")
long = st.number_input("Longitude", format="%.6f")
sqft_living15 = st.number_input("Sqft Living15", min_value=0.0)
sqft_lot15 = st.number_input("Sqft Lot15", min_value=0.0)
house_age = st.number_input("House Age", min_value=0.0)
is_renovated = st.selectbox("Is Renovated (0 = No, 1 = Yes)", [0, 1])

if st.button("Predict Price"):

    input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                            waterfront, view, condition, grade, sqft_basement,
                            lat, long, sqft_living15, sqft_lot15,
                            house_age, is_renovated]])

    prediction = model.predict(input_data)

    if np.isinf(prediction[0]) or np.isnan(prediction[0]):
        st.error("Prediction Error. Please check inputs.")
    else:
        st.success(f"Estimated House Price: {round(float(prediction[0]), 2)}")
