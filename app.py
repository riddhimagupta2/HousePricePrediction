import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter house details to predict the estimated sale price.")

MODEL_PATH = "house_price_model.pkl"
COLUMNS_PATH = "columns.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(COLUMNS_PATH):
    st.error("Model file not found. First run: python train_model.py")
    st.stop()

model = joblib.load(MODEL_PATH)
columns = joblib.load(COLUMNS_PATH)

overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Living Area in sq ft", min_value=300, max_value=10000, value=1500)
garage_cars = st.number_input("Garage Cars", min_value=0, max_value=5, value=2)
total_bsmt_sf = st.number_input("Total Basement Area", min_value=0, max_value=5000, value=800)
year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)
full_bath = st.number_input("Full Bathrooms", min_value=0, max_value=5, value=2)
bedroom_abvgr = st.number_input("Bedrooms", min_value=0, max_value=10, value=3)

input_data = pd.DataFrame(0, index=[0], columns=columns)

values = {
    "OverallQual": overall_qual,
    "GrLivArea": gr_liv_area,
    "GarageCars": garage_cars,
    "TotalBsmtSF": total_bsmt_sf,
    "YearBuilt": year_built,
    "FullBath": full_bath,
    "BedroomAbvGr": bedroom_abvgr
}

for col, val in values.items():
    if col in input_data.columns:
        input_data[col] = val

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction:,.0f}")