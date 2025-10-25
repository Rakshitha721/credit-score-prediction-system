import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1️⃣ Load the trained model
model = joblib.load('models/credit_score_model.pkl')

# 2️⃣ Page setup
st.set_page_config(page_title="Credit Score Prediction", page_icon="💳")

st.title("💳 Credit Score Prediction App")
st.write("Enter financial and credit details to predict your Credit Score category.")

# 3️⃣ Input fields for user
Monthly_Inhand_Salary = st.number_input("Monthly Inhand Salary (₹)", min_value=0.0, step=1000.0)
Num_Bank_Accounts = st.number_input("Number of Bank Accounts", min_value=0, step=1)
Num_Credit_Card = st.number_input("Number of Credit Cards", min_value=0, step=1)
Interest_Rate = st.number_input("Interest Rate (%)", min_value=0.0, step=0.1)
Num_of_Loan = st.number_input("Number of Loans", min_value=0, step=1)
Delay_from_due_date = st.number_input("Average Delay from Due Date (days)", min_value=0, step=1)
Num_of_Delayed_Payment = st.number_input("Number of Delayed Payments", min_value=0, step=1)
Outstanding_Debt = st.number_input("Outstanding Debt (₹)", min_value=0.0, step=1000.0)
Credit_Utilization = st.number_input("Credit Utilization Ratio", min_value=0.0, max_value=10.0, step=0.1)
Credit_Mix = st.selectbox("Credit Mix", ["Poor (0)", "Standard (1)", "Good (2)"])

# Convert Credit_Mix label to integer value
Credit_Mix = int(Credit_Mix.split("(")[1].replace(")", ""))

# 4️⃣ Predict button
if st.button("🔍 Predict Credit Score"):
    # Build input dataframe
    input_data = pd.DataFrame({
        'Monthly_Inhand_Salary': [Monthly_Inhand_Salary],
        'Num_Bank_Accounts': [Num_Bank_Accounts],
        'Num_Credit_Card': [Num_Credit_Card],
        'Interest_Rate': [Interest_Rate],
        'Num_of_Loan': [Num_of_Loan],
        'Delay_from_due_date': [Delay_from_due_date],
        'Num_of_Delayed_Payment': [Num_of_Delayed_Payment],
        'Outstanding_Debt': [Outstanding_Debt],
        'Credit_Utilization': [Credit_Utilization],
        'Credit_Mix': [Credit_Mix]
    })

    # --- Align columns with the model's expectation ---
    expected_features = model.feature_names_in_
    final_input = pd.DataFrame(np.zeros((1, len(expected_features))), columns=expected_features)

    for col, val in input_data.iloc[0].items():
        if col in final_input.columns:
            final_input[col] = val

    # 5️⃣ Make prediction
    prediction = model.predict(final_input)[0]

    # 6️⃣ Display result
    if prediction == 0:
        st.error("Predicted Credit Score: **Poor 💔**")
    elif prediction == 1:
        st.warning("Predicted Credit Score: **Standard 🙂**")
    else:
        st.balloons()
        st.success("Predicted Credit Score: **Good 💚**")

st.markdown("---")

