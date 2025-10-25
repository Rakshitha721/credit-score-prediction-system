💳 Credit Score Prediction System
📘 Overview

The Credit Score Prediction System is a Machine Learning web application that predicts the creditworthiness of loan applicants based on their financial and behavioral data.
It uses a trained ML model to classify users into categories such as Good, Standard, or Poor, helping financial institutions make informed lending decisions.

🚀 Features

🔍 Data Cleaning & Preprocessing – handles missing values, encodes categorical variables

🧮 Feature Engineering – creates ratios like Credit_Utilization, Debt_to_Income, etc.

🤖 Model Training – Logistic Regression | Random Forest | XGBoost with accuracy comparison

🧾 Model Evaluation – classification report & confusion matrix

💾 Model Serialization – lightweight .pkl for deployment

🌐 Streamlit UI – intuitive web interface for live predictions

☁️ Deployable on Streamlit Cloud – zero-config cloud demo

🧠 Tech Stack
Layer	Technologies
Language	Python 3.11
Libraries	pandas, numpy, matplotlib, seaborn, scikit-learn, joblib, streamlit
Model	Random Forest Classifier (lightweight)
Development Tools	VS Code, Jupyter Notebook, Git & GitHub
Deployment	Streamlit Cloud
📂 Project Structure
CreditScorePrediction/
│
├── data/
│   └── cleaned_credit_score.csv
│
├── models/
│   └── credit_score_model_light.pkl      ← lightweight model (<10 MB)
│
├── notebooks/
│   ├── EDA.ipynb                         ← exploratory data analysis
│   ├── model_building.ipynb              ← feature engineering & training
│   ├── evaluation.ipynb                  ← performance metrics
│   └── lightweight_model.ipynb           ← small model for deployment
│
├── app/
│   └── streamlit_app.py                  ← Streamlit web app
│
├── requirements.txt
└── README.md

⚙️ Installation & Setup
🔹 1. Clone the repository
git clone https://github.com/Rakshitha721/credit-score-prediction-system.git
cd credit-score-prediction-system

🔹 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# or
source .venv/bin/activate   # macOS/Linux

🔹 3. Install dependencies
pip install -r requirements.txt

🔹 4. Run the Streamlit app
streamlit run app/streamlit_app.py


🖥️ Then open your browser at http://localhost:8501
 to test predictions.

📊 Dataset

The dataset originates from a public Kaggle source containing anonymized borrower information such as:

Monthly Income

Number of Bank Accounts

Number of Credit Cards

Outstanding Debt

Average Payment Delays

Credit Mix and Behavior

Credit Score (label) → Poor / Standard / Good

🧮 Model Performance
Model	Accuracy
Logistic Regression	~68 %
Random Forest (Light)	~82 %
XGBoost	~85 %

The final lightweight Random Forest model offers a good balance between performance and deployability.
