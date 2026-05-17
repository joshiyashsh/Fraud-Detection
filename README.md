## this is fraud detection ML project in data science
# AI-Powered Financial Fraud Detection System

## Project Overview

This project is a Machine Learning-based Financial Fraud Detection System developed using Python, Scikit-learn, and Streamlit.

The system analyzes transaction details and predicts whether a transaction is:

- Fraudulent Transaction
- Safe Transaction

The project uses a real-world large-scale financial transaction dataset containing more than 6 million records.

---

# Features

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- OneHotEncoding
- StandardScaler
- Pipeline Implementation
- Logistic Regression Baseline Model
- Random Forest Classifier
- Fraud Prediction Web App using Streamlit
- Classification Report
- Confusion Matrix Visualization

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# Dataset Information

The dataset contains financial transaction records with features such as:

- Transaction Type
- Transaction Amount
- Sender Balance
- Receiver Balance
- Transaction Time Step

Target Variable:

- `0` → Safe Transaction
- `1` → Fraudulent Transaction

---

# Machine Learning Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
OneHotEncoding
      ↓
Standard Scaling
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Evaluation
      ↓
Streamlit Deployment
```

---

# Models Used

## Logistic Regression

Used as the baseline model for binary classification.

## Random Forest Classifier

Used to improve fraud detection performance and handle non-linear fraud patterns.

---

# Model Performance

## Random Forest Results

| Metric | Score |
|---|---|
| Precision | 0.99 |
| Recall | 0.79 |
| F1-Score | 0.88 |

The Random Forest model significantly improved fraud detection performance compared to Logistic Regression.

---

# Project Structure

```text
FraudDetectionProject/
│
├── data/
│   └── fraud.csv
│
├── model/
│   └── fraud_pipeline.pkl
│
├── notebook/
│   └── fraud_detection.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit App

```bash
streamlit run app.py
```

---

# Streamlit Interface

The Streamlit web application allows users to:

- Enter transaction details
- Select transaction type
- Predict fraud probability
- Detect suspicious transactions in real-time

---

# Future Improvements

- XGBoost Implementation
- SHAP Explainability
- Real-time Fraud Monitoring
- Cloud Deployment
- Power BI Dashboard
- Fraud Alert System

---

# Author

Yash Joshi
