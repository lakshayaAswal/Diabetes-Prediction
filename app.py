import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

st.set_page_config(page_title="Diabetes Prediction App", layout="centered")

st.title("🩺 Diabetes Prediction Model")
st.write("Enter the medical details below to predict the likelihood of diabetes.")

# Create input fields for the 8 features
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=150, step=1)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, step=1)

with col2:
    insulin = st.number_input("Insulin Level (IU/mL)", min_value=0, max_value=1000, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.000, max_value=3.000, step=0.001)
    age = st.number_input("Age", min_value=1, max_value=120, step=1)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                            insulin, bmi, dpf, age]])
    std_data = scaler.transform(input_data)
    prediction = model.predict(std_data)
    
    st.markdown("---")
    if prediction[0] == 0:
        st.success("✅ The model predicts: **The person is NOT diabetic.**")
    else:
        st.error("⚠️ The model predicts: **The person is diabetic.**")