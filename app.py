import streamlit as st
import joblib
import pandas as pd

model = joblib.load("decision_tree_model.pkl")

st.title("Loan Approval Prediction")
st.write("Enter the applicant details below to predict loan approval.")

age = st.number_input("Age", min_value=20, max_value=100, value=30)

income = st.number_input("Annual Income",min_value=0,step=500, value=10000)

loan_amount = st.number_input("Loan Amount",min_value=500,step=500, value=1000)

credit_score = st.number_input("Credit Score",min_value=300,max_value=900,)

if st.button("Predict Loan"):
    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "LoanAmount": [loan_amount],
        "CreditScore": [credit_score]
    })
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")