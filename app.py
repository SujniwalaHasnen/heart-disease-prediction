import streamlit as st
import joblib as jb
import numpy as np
model=jb.load("heart_model.joblib")
st.title("Heart Disease Prediction")
age=st.number_input("Enter the age:")
sex=st.selectbox("Select gender:",["Male","Female"])
sex=1 if sex == "Male" else 0
cp=st.selectbox("Select Chest pain:",[0,1,2,3])
testbps=st.number_input("Resting Blood Pressure")
chol=st.number_input("Serum Cholestoral in mg/dl")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:", ["True", "False"])
fbs = 1 if fbs == "True" else 0
restecg = st.selectbox("Resting Electrocardio results:", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate achieved:")
exang = st.selectbox("Exercise Induced Angina:", ["Yes", "No"])
exang = 1 if exang == "Yes" else 0
oldpeak = st.number_input("ST depression induced by exercise:")
slope = st.selectbox("Slope of the peak exercise ST segment:", [0, 1, 2])
ca = st.selectbox("Number of major vessels:", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal:", [0, 1, 2, 3])
if st.button("Predict"):
    x = [[age, sex, cp, testbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    yp=model.predict(x)
    if yp[0] == 1:
        st.error("Warning: The model predicts a high risk of heart disease.")
    else:
        st.success("Good news: The model predicts no heart disease.")