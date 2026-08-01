import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("Telco_customer_churn.xlsx", engine="openpyxl")
print(df.head(10))

# UNDERSTANDING THE DATASET

print("Shape:")
print(df.shape)

print("Columns:")
print(df.columns)

print("Dataset Info:")
df.info()

print("Descriptive Statistics:")
print(df.describe())

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())

# NEXT STEP IS DATA CLEANING 

print(df["Total Charges"].unique()[:20])
# nunique = tell me how many unique values 
# unique = show me the unique values

print(pd.to_numeric(df["Total Charges"], errors="coerce").isnull().sum())
print(df[df["Total Charges"].apply(lambda x: str(x).strip() == "")])
print(df.loc[df["Total Charges"].apply(lambda x: str(x).strip() == ""), ["CustomerID", "Tenure Months", "Monthly Charges", "Total Charges"]])

# We need to convert Total Charges from object to a numeric column.

df["Total Charges"] = pd.to_numeric(df["Total Charges"] , errors="coerce")
df = df.dropna(subset=["Total Charges"])
print(df.shape)
print(df["Total Charges"].dtype)
print(df['Total Charges'].isnull().sum())

# HOW MANY CUSTOMERS CHURNED VS STAYED
print(df["Churn Label"].value_counts())
print(df["Churn Label"].value_counts(normalize=True)*100)

#### GRAPHS ####

sns.countplot(x="Churn Label" , data=df)
# X-axis = What you are comparing / categories
# Y-axis = What you are counting or measuring
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of customers")
plt.savefig("visualizations/graph1_churn_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

# QUICK CHEAT SHEET

# How many categories?             → sns.countplot()
# Compare category + number?       → sns.barplot()
# Distribution of one number?      → sns.histplot()
# Find outliers / spread?          → sns.boxplot()
# Relationship between 2 numbers? → sns.scatterplot()
# Show trend over time?            → sns.lineplot()
# Check correlations?              → sns.heatmap()

#  WHICH CONTRACT TYPE HAS MORE CUSTOMERS CHURNING 
sns.countplot(x="Contract", hue="Churn Label", data=df)

plt.title("Churn Distribution by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.savefig("visualizations/graph2_contract_vs_churn.png", dpi=300, bbox_inches="tight")
plt.close()

# Does the type of internet service affect customer churn?
sns.countplot(x="Internet Service", hue="Churn Label", data=df)

plt.title("Churn Distribution by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.savefig("visualizations/graph3_internet_service_vs_churn.png", dpi=300, bbox_inches="tight")
plt.close()

# Do customers who have been with the company for a longer time churn less?

sns.boxplot(x="Churn Label" , y="Tenure Months" , data=df)
plt.title("Tenure Months vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure Months")
plt.savefig("visualizations/graph4_tenure_vs_churn.png", dpi=300, bbox_inches="tight")
plt.close()
# THIS STATE THAT CHURNED CUSTOMER HAVE LOWER TENURE

# Do customers paying higher monthly charges churn more?

sns.boxplot(x="Churn Label", y="Monthly Charges", data=df)

plt.title("Monthly Charges vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.savefig("visualizations/graph5_monthly_charges_vs_churn.png", dpi=300, bbox_inches="tight")
plt.close()

# Does the payment method affect customer churn?

sns.countplot(x="Payment Method", hue="Churn Label", data=df)

plt.title("Churn Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)
plt.savefig("visualizations/graph6_payment_method_vs_churn.png", dpi=300, bbox_inches="tight")

plt.close()

# Do senior citizens churn more than non-senior citizens?

sns.countplot(x="Senior Citizen" , hue= "Churn Label" , data=df)

plt.title("Churn Distribution by Senior Citizen")
plt.xlabel("Senior Citizen")
plt.ylabel("Number of Customers")
plt.savefig("visualizations/graph7_senior_citizen_vs_churn.png", dpi=300, bbox_inches="tight")
plt.close()

churn_rate = pd.crosstab(df["Senior Citizen"], df["Churn Label"], normalize="index") * 100

print(churn_rate)
# senior citizen have a higher churn rate 

# Does gender have any relationship with customer churn?

sns.countplot(x="Gender", hue="Churn Label", data=df)

plt.title("Churn Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.savefig("visualizations/graph8_gender_vs_churn.png", dpi=300, bbox_inches="tight")

plt.close()


# Churn percentage by Gender
gender_churn_rate = pd.crosstab(df["Gender"], df["Churn Label"], normalize="index") * 100

print(gender_churn_rate)


# Graph 9: Correlation Heatmap
# Purpose: To find relationships between numerical features
# and understand which features are related to churn


plt.figure(figsize=(10,6))

corr = df.select_dtypes(include=["int64", "float64"]).corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")

plt.savefig("visualizations/graph9_correlation_heatmap.png", dpi=300, bbox_inches="tight")

plt.close()




# Graph 10: Tenure Distribution by Churn
# Purpose: To analyze whether customers with shorter
# tenure are more likely to churn


sns.histplot(
    data=df,
    x="Tenure Months",
    hue="Churn Label",
    bins=30,
    kde=True
)

plt.title("Tenure Distribution by Churn")
plt.xlabel("Tenure Months")
plt.ylabel("Number of Customers")

plt.savefig("visualizations/graph10_tenure_distribution.png", dpi=300, bbox_inches="tight")

plt.close()

# Graph 11: Contract Type vs Monthly Charges
# Purpose: To compare monthly charges across
# different contract types


sns.boxplot(
    x="Contract",
    y="Monthly Charges",
    data=df
)

plt.title("Monthly Charges by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Monthly Charges")

plt.savefig("visualizations/graph11_contract_vs_monthly_charges.png", dpi=300, bbox_inches="tight")

plt.close()

# Graph 12: Internet Service vs Contract Churn
# Purpose: To analyze which combination of
# internet service and contract has higher churn


sns.countplot(
    x="Internet Service",
    hue="Contract",
    data=df[df["Churn Label"]=="Yes"]
)

plt.title("Churned Customers by Internet Service and Contract")
plt.xlabel("Internet Service")
plt.ylabel("Number of Churned Customers")

plt.savefig("visualizations/graph12_internet_contract_churn.png", dpi=300, bbox_inches="tight")

plt.close()

# Graph 13: Tech Support vs Churn
# Purpose: To check whether lack of technical
# support increases customer churn


sns.countplot(
    x="Tech Support",
    hue="Churn Label",
    data=df
)

plt.title("Churn Distribution by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.savefig("visualizations/graph13_tech_support_vs_churn.png", dpi=300, bbox_inches="tight")

plt.close()

# Graph 14: Online Security vs Churn
# Purpose: To analyze whether online security
# service affects customer retention

sns.countplot(
    x="Online Security",
    hue="Churn Label",
    data=df
)

plt.title("Churn Distribution by Online Security")
plt.xlabel("Online Security")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.savefig("visualizations/graph14_online_security_vs_churn.png", dpi=300, bbox_inches="tight")

plt.close()


# Graph 15: Total Charges vs Churn
# Purpose: To compare total spending between
# churned and retained customers

df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")

sns.boxplot(
    x="Churn Label",
    y="Total Charges",
    data=df
)

plt.title("Total Charges vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Total Charges")

plt.savefig("visualizations/graph15_total_charges_vs_churn.png", dpi=300, bbox_inches="tight")

plt.close()



print("===== ML PIPELINE STARTED =====") 

# Remove unnecessary columns
# Remove unnecessary columns
df = df.drop([
    "CustomerID",
    "Churn Reason",
    "Churn Value",
    "Churn Score",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "Count"
], axis=1)

print("Unnecessary columns removed")


# Target
y = df["Churn Label"]

# Features
X = df.drop("Churn Label", axis=1)

print("Target created")

# Convert Total Charges to numeric
X["Total Charges"] = pd.to_numeric(
    X["Total Charges"],
    errors="coerce"
)

X["Total Charges"] = X["Total Charges"].fillna(0)

# One Hot Encoding
X = pd.get_dummies(X, drop_first=True)

print("X shape after encoding:")
print(X.shape)

print("Y shape:")
print(y.shape)

""" Original dataset
7032 × 33
       ↓
Removed 12 unnecessary columns
7032 × 21
       ↓
Removed Churn Label from X → target y
X = 7032 × 20
       ↓
One-Hot Encoding
X = 7032 × 31 """  # The 31 is the number of columns the ML model actually uses as input.



# TRAIN-TEST SPLIT


from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data shape:")
print(X_train.shape)

print("Testing data shape:")
print(X_test.shape)

print("Training target shape:")
print(y_train.shape)

print("Testing target shape:")
print(y_test.shape)


# LOGISTIC REGRESSION MODEL


from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

print("Model training completed!")

#  MAKE PREDICTIONS
y_pred = model.predict(X_test)
print("Predictions completed!")
print(y_pred[:10])  # Show first 10 predictions

# How many predictions did our model get correct?
# MODEL ACCURACY
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
#calculate accuracy
accuracy = accuracy_score(y_test, y_pred )
print("Model Accuracy:", accuracy)
print("Model Accuracy (%):", accuracy * 100)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()

plt.title("Confusion Matrix - Logistic Regression")
plt.savefig(
    "visualizations/graph16_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close() 

# CLASSIFICATION REPORT
# will give us precision, recall, f1-score and support for each class
from sklearn.metrics import classification_report
REPORT = classification_report(y_test, y_pred)
print("Classification Report:") 
print(REPORT)


# DECISION TREE MODEL


from sklearn.tree import DecisionTreeClassifier

# Create Decision Tree model
dt_model = DecisionTreeClassifier(
    random_state=42
)

# Train the model
dt_model.fit(X_train, y_train)

print("Decision Tree training completed!")

# Make predictions
dt_pred = dt_model.predict(X_test)

print("Decision Tree predictions completed!")

# DECISION TREE ACCURACY

dt_accuracy = accuracy_score(y_test, dt_pred)

print("Decision Tree Accuracy:", dt_accuracy)
print("Decision Tree Accuracy (%):", dt_accuracy * 100)

# DECISION TREE CLASSIFICATION REPORT

print("Decision Tree Classification Report:")
print(classification_report(y_test, dt_pred))


# RANDOM FOREST MODEL


from sklearn.ensemble import RandomForestClassifier

# Create Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
rf_model.fit(X_train, y_train)

print("Random Forest training completed!")

# Make predictions
rf_pred = rf_model.predict(X_test)

print("Random Forest predictions completed!")


# RANDOM FOREST ACCURACY


rf_accuracy = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy:", rf_accuracy)
print("Random Forest Accuracy (%):", rf_accuracy * 100)

# RANDOM FOREST CLASSIFICATION REPORT

print("Random Forest Classification Report:")
print(classification_report(y_test, rf_pred))

# LOGISTIC REGRESSION HAS MORE ACCURACY THAN DECISION TREE AND RANDOM FOREST. SO WE WILL USE LOGISTIC REGRESSION MODEL FOR PREDICTION.

# SAVE FINAL MODEL

import joblib
# Joblib ek Python library hai jo machine learning models ko save aur load karne ke liye use hoti hai.
# Save the trained Logistic Regression model
joblib.dump(model, "churn_model.pkl")

print("Final Logistic Regression model saved successfully!")


# LOAD SAVED MODEL
# Joblib ek Python library hai jo machine learning models ko save aur load karne ke liye use hoti hai.

loaded_model = joblib.load("churn_model.pkl")

print("Saved model loaded successfully!")

# Test prediction
test_prediction = loaded_model.predict(X_test)

print("Test prediction:")
print(test_prediction[:10])


# FINAL CUSTOMER CHURN PREDICTION
# no new customer data is provided, so we will use the first customer from the test data for prediction.

# Take one customer from test data
customer = X_test.iloc[[0]]

# Predict churn
prediction = loaded_model.predict(customer)

print("Customer Churn Prediction:", prediction[0])

actual = y_test.iloc[0]

print("Actual Churn:", actual)

if prediction[0] == actual:
    print("Prediction is CORRECT!")
else:
    print("Prediction is WRONG!")

# Feature Importance ka matlab:
# Model ke liye kaunse customer factors sabse important hain
# aur customer ke churn hone ya na hone ki prediction par
# sabse zyada influence karte hain, hum unhe identify kar rahe hain.
#
# Example:
# Contract Type, Tenure, Monthly Charges, Internet Service etc.
# customer ke churn hone ya na hone ko influence kar sakte hain.
#
# Positive coefficient:
# Churn = Yes ki taraf influence karta hai.
#
# Negative coefficient:
# Churn = No ki taraf influence karta hai.
#
# Is analysis se hume samajhne mein help milti hai ki
# model ne churn prediction kis customer information ke basis par ki.


# IMPORTANT FEATURES

# Get feature names
feature_names = X_train.columns

# Get Logistic Regression coefficients
coefficients = loaded_model.coef_[0]

# Create DataFrame
feature_importance = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

# Calculate absolute importance
feature_importance["Importance"] = feature_importance["Coefficient"].abs()

# Sort from most important to least important
feature_importance = feature_importance.sort_values(
    "Importance",
    ascending=False
)

# Display top 15 important features
print("Top 15 Important Features:")
print(feature_importance.head(15))

""" X_train ke Feature Names
        ↓
Logistic Regression ke Coefficients
        ↓
Feature + Coefficient ko DataFrame mein rakha
        ↓
Absolute Importance nikali
        ↓
Importance ke according Sort kiya
        ↓
Top 15 Features print kiye """

# "Our Logistic Regression model found Fiber Optic service to be positively associated with churn prediction."


# FEATURE IMPORTANCE VISUALIZATION

# Select top 10 important features
top_features = feature_importance.head(10)

# Create bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)

# Add labels and title
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Top 10 Important Features for Customer Churn Prediction")

# Show the most important feature at the top
plt.gca().invert_yaxis()

# Adjust layout
plt.tight_layout()

# save the figure
plt.savefig(
    "visualizations/graph17_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

# Display graph
plt.show()