# Customer Churn Prediction

## Project Overview

This project focuses on predicting customer churn using machine learning techniques. Customer churn refers to customers who stop using a service, and predicting it helps businesses take proactive steps to retain them.

The dataset contains customer demographic details, service usage information, and account-related features. The goal is to analyze this data, identify key factors influencing churn, and build a predictive model that can classify whether a customer is likely to churn or not.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and interpretation of results to generate actionable business insights.

Customer churn is one of the biggest challenges for businesses because losing customers directly impacts revenue and growth.

This project focuses on building a **Machine Learning model to predict whether a customer is likely to churn or stay**. The project includes complete data analysis, data preprocessing, exploratory data analysis (EDA), machine learning model development, model evaluation, feature importance analysis, and customer churn prediction.

The final model helps identify customers who are at risk of leaving and provides insights that can support customer retention strategies.

---

## Project Objectives

The main objectives of this project are:

* Analyze customer churn patterns.
* Identify important factors affecting customer churn.
* Perform data cleaning and preprocessing.
* Build and compare multiple machine learning models.
* Evaluate model performance using different metrics.
* Select the best-performing model.
* Save the trained model for future predictions.

---

# Dataset

The dataset contains customer information related to demographics, services, and billing details.

### Dataset Features Include:

* Customer demographics
* Gender
* Senior citizen status
* Partner and dependents information
* Contract type
* Internet and phone services
* Online security and support services
* Payment methods
* Monthly charges
* Total charges
* Customer churn status

### Dataset Information:

* Original dataset: **7,043 rows × 33 columns**
* After cleaning: **7,032 rows used for machine learning**

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Git & GitHub

---

# Data Cleaning & Preprocessing

The following preprocessing steps were performed:

* Loaded and explored the dataset.
* Checked dataset structure and statistics.
* Checked missing values and duplicates.
* Converted `Total Charges` into numeric format.
* Removed rows containing missing values.
* Removed unnecessary columns.
* Separated features and target variable.
* Applied One-Hot Encoding to categorical variables.
* Split data into training and testing datasets.

### Machine Learning Data Preparation

```text
Original Dataset
7032 × 33

        ↓

Remove unnecessary columns

        ↓

Separate Target Variable (Churn)

        ↓

One-Hot Encoding

        ↓

Train-Test Split

        ↓

Training Data: 5625 samples
Testing Data: 1407 samples
```

---

# Exploratory Data Analysis (EDA)

EDA was performed to understand customer behavior and churn patterns.

Analysis included:

* Overall churn distribution.
* Churn percentage analysis.
* Churn based on contract type.
* Churn based on internet service.
* Churn based on payment method.
* Customer service analysis.
* Correlation analysis.

### Churn Distribution

* Customers who stayed: **73.42%**
* Customers who churned: **26.58%**

---

# Machine Learning Models

Three classification models were trained and evaluated:

## 1. Logistic Regression

Accuracy:

**80.67%**

---

## 2. Random Forest Classifier

Accuracy:

**79.82%**

---

## 3. Decision Tree Classifier

Accuracy:

**Approximately 74%**

---

## Best Performing Model

Among all tested models, **Logistic Regression achieved the highest accuracy (80.67%)** and was selected as the final model.

---

# Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

The evaluation helped understand how effectively the model predicts customers who are likely to churn.

---

# Feature Importance Analysis

The model identified important factors influencing customer churn.

Top important features include:

* Dependents status
* Contract type
* Fiber optic internet service
* Online Security
* Tech Support
* Payment Method
* Phone Service
* Paperless Billing

---

# Final Business Insights

Detailed analysis and business recommendations are available here:

➡️ [View Final Business Insights](FINAL_INSIGHTS.md)

Main findings:

* Around one-fourth of customers are at risk of churn.
* Long-term contracts reduce churn probability.
* Customers with support services show better retention.
* Fiber optic customers require further investigation due to higher churn tendency.
* Customer retention strategies should focus on high-risk customers.

---

# Model Prediction

The trained Logistic Regression model was saved using Joblib and used for future predictions.

Example:

```text
Customer Churn Prediction: No

Actual Churn: No
```

The model successfully predicted customer churn status for test customers.

---

# Visualizations

All generated graphs are stored inside the `visualizations` folder.

Visualizations include:

* Churn distribution
* Contract vs churn analysis
* Internet service analysis
* Tenure analysis
* Payment method analysis
* Correlation heatmap
* Confusion matrix
* Feature importance visualization

---

# Project Structure

```text
customer-churn-prediction
│
├── churn_prediction.py
├── README.md
├── final_insights.md
├── churn_model.pkl
├── Telco_customer_churn.xlsx
│
└── visualizations
    │
    ├── graph01_churn_distribution.png
    ├── graph02_contract_vs_churn.png
    ├── graph03_internet_service_vs_churn.png
    ├── graph04_tenure_vs_churn.png
    ├── graph05_monthly_charges_vs_churn.png
    ├── graph06_payment_method_vs_churn.png
    ├── graph07_senior_citizen_vs_churn.png
    ├── graph08_gender_vs_churn.png
    ├── graph09_correlation_heatmap.png
    ├── graph10_tenure_distribution.png
    ├── graph11_contract_vs_monthly_charges.png
    ├── graph12_internet_contract_churn.png
    ├── graph13_tech_support_vs_churn.png
    ├── graph14_online_security_vs_churn.png
    ├── graph15_total_charges_vs_churn.png
    ├── graph16_confusion_matrix.png
    └── graph17_feature_importance.png
```

---

# How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/Mamta-codes/customer-churn-prediction.git
```

### 2. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib openpyxl
```

### 3. Run Project

```bash
python churn_prediction.py
```

---

# Conclusion

This project demonstrates an end-to-end machine learning workflow for customer churn prediction.

The project covers:

* Data cleaning
* Exploratory data analysis
* Feature engineering
* Machine learning model building
* Model evaluation
* Feature importance analysis
* Model saving and prediction

The Logistic Regression model achieved the best performance with **80.67% accuracy**, providing useful insights into customer behavior and churn factors.
