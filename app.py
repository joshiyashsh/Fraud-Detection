import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "model/fraud_pipeline.pkl"
)

st.title("Fraud Detection System")

step = st.number_input("Step")

amount = st.number_input("Amount")

oldbalanceOrg = st.number_input("Old Balance Sender")

newbalanceOrig = st.number_input("New Balance Sender")

oldbalanceDest = st.number_input("Old Balance Receiver")

newbalanceDest = st.number_input("New Balance Receiver")

transaction_type = st.selectbox(
    "Transaction Type",
    ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT']
)

if st.button("Predict"):

    data = pd.DataFrame({
        'step': [step],
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Safe Transaction")