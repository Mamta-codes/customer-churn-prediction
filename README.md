# Customer Churn Prediction

## Project Overview

This project focuses on predicting whether a customer is likely to churn (leave the company) using machine learning techniques.

The project includes data cleaning, exploratory data analysis (EDA), feature preprocessing, machine learning model training, model evaluation, feature importance analysis, and customer churn prediction.

The final model can be used to predict whether an individual customer is likely to churn or stay with the company.

---

## Project Goal

The main goal of this project is to:

* Analyze customer churn patterns.
* Identify factors associated with customer churn.
* Build machine learning models to predict customer churn.
* Compare the performance of different machine learning algorithms.
* Select the best-performing model.
* Save and load the trained model for future predictions.

---

## Dataset

The dataset contains customer information and service details, including:

* Customer demographics
* Contract information
* Internet and phone services
* Online security and support services
* Monthly and total charges
* Customer tenure
* Churn status

The dataset contains **7,043 customer records and 33 columns** before data cleaning.

After removing rows with missing `Total Charges` values, the final dataset contained **7,032 customer records** for machine learning.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Git & GitHub

---

## Data Cleaning and Preprocessing

The following preprocessing steps were performed:

* Loaded and explored the dataset.
* Checked dataset shape, columns, data types, and summary statistics.
* Checked for missing values.
* Checked for duplicate records.
* Converted `Total Charges` into a numeric data type.
* Removed 11 rows with missing `Total Charges` values.
* Removed unnecessary columns that could cause data leakage or were not required for prediction.
* Separated the target variable (`Churn Label`) from the input features.
* Applied One-Hot Encoding to categorical variables.
* Split the dataset into training and testing sets.

### Machine Learning Dataset

```text
Original Dataset
7032 × 33
       ↓
Remove unnecessary columns
       ↓
Separate Target Variable
       ↓
One-Hot Encoding
       ↓
Train-Test Split
       ↓
Train: 5625 samples
Test: 1407 samples
```

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer churn patterns.

The analysis included:

* Overall churn distribution.
* Churn percentage.
* Churn based on gender.
* Churn based on senior citizen status.
* Analysis of customer service and subscription-related factors.
* Feature importance analysis.

Overall churn distribution:

* **Customers who did not churn: 73.42%**
* **Customers who churned: 26.58%**

---

## Machine Learning Models

The following machine learning models were trained and evaluated:

### 1. Logistic Regression

Accuracy: **80.67%**

### 2. Random Forest Classifier

Accuracy: **79.82%**

### 3. Decision Tree Classifier

Accuracy: **74% approximately**

Logistic Regression achieved the highest accuracy among the tested models and was selected as the final model.

---

## Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

The Logistic Regression model achieved an overall accuracy of approximately **80.67%** on the test dataset.

The model's performance on the churn class (`Yes`) was also evaluated using precision, recall, and F1-score to understand how effectively the model identifies customers who are likely to churn.

---

## Key Insights

### 1. Overall Customer Churn

26.58% of customers have churned, while 73.42% have remained with the company. This indicates that approximately one-fourth of the customer base is at risk of churn.

### 2. Contract Type

Contract type is an important factor in churn prediction. Customers with one-year and two-year contracts show a lower tendency to churn compared with customers on month-to-month contracts.

### 3. Dependents

Customers with dependents show a lower tendency to churn according to the Logistic Regression model.

### 4. Internet Service

Fiber optic internet service is associated with a higher churn tendency in the model, making it a factor that may require further investigation.

### 5. Online Security and Tech Support

Customers with Online Security and Tech Support show a lower tendency to churn, suggesting that additional support and security services may contribute to better customer retention.

### 6. Model Performance

Among the tested machine learning models, Logistic Regression achieved the highest accuracy of approximately 80.67% and was selected as the final model.

### 7. Final Prediction System

The trained Logistic Regression model was successfully saved using Joblib and loaded again to make predictions for individual customers.

---

## Visualizations

The project includes visualizations to understand customer churn patterns and important factors influencing churn prediction.

The visualizations are stored in the `visualizations` folder.

Key visualizations include:

* Customer churn distribution.
* Churn analysis by customer characteristics.
* Churn analysis by service-related factors.
* Top 10 feature importance visualization.

---

## Model Prediction

The trained Logistic Regression model can be loaded using Joblib and used to predict whether a customer is likely to churn.

Example prediction:

```text
Customer Churn Prediction: No
Actual Churn: No
```

The prediction was correctly classified for the tested customer.

---

## How to Run the Project

### 1. Clone the Repository

Clone this repository to your local machine.

### 2. Install Required Libraries

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib openpyxl
```

### 3. Run the Python Script

Run the main Python file:

```bash
python churn_prediction.py
```

### 4. View the Results

The program will:

* Perform data preprocessing.
* Train machine learning models.
* Evaluate model performance.
* Display classification metrics.
* Generate visualizations.
* Save the trained model.
* Make customer churn predictions.

---

## Project Structure

```text
PROJECT 2
│
├── churn_prediction.py
├── final_insights.txt
├── churn_model.pkl
├── README.md
│
└── visualizations
    └── top_10_feature_importance.png
```

---

## Conclusion

This project demonstrates how machine learning can be used to predict customer churn and identify factors associated with customer retention.

Among the tested models, Logistic Regression achieved the best performance with approximately **80.67% accuracy**. The analysis also highlighted the importance of contract type, dependents, internet service, online security, and technical support in churn prediction.

The project combines **data analysis, visualization, machine learning, model evaluation, and model deployment basics** into a complete end-to-end customer churn prediction workflow.
