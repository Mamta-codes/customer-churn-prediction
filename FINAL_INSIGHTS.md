# FINAL BUSINESS INSIGHTS

Customer Churn Prediction Analysis

1. Overall Customer Churn Distribution

---

The dataset contains 7,032 customers after data cleaning.

* 73.42% of customers have not churned and are still active customers.
* 26.58% of customers have churned and left the company.

This indicates that around one-fourth of the customers are at risk of leaving, making churn prediction important for improving customer retention strategies.

---

2. Impact of Contract Type on Customer Churn

---

Contract type is one of the most important factors affecting customer churn.

* Customers with month-to-month contracts show a higher tendency to churn.
* Customers with one-year and two-year contracts have a lower churn probability.

This suggests that encouraging customers to choose long-term contracts may help reduce churn and improve customer loyalty.

---

3. Role of Customer Dependents

---

According to the Logistic Regression model, customers with dependents show a lower tendency to churn.

Customers with family responsibilities may have stronger reasons to continue using the company's services compared to customers without dependents.

---

4. Internet Service Analysis

---

Internet service type has a significant relationship with churn prediction.

* Fiber optic customers show a higher churn tendency in the model.
* This may indicate possible issues related to pricing, service experience, or customer expectations.

Further analysis can help identify the reasons behind higher churn among fiber optic users.

---

5. Importance of Online Security and Technical Support

---

Additional support services play an important role in customer retention.

Customers who have:

* Online Security
* Tech Support

show a lower tendency to churn.

Providing better customer assistance and additional services can improve customer satisfaction and reduce customer loss.

---

6. Machine Learning Model Performance

---

Three machine learning algorithms were trained and evaluated:

1. Logistic Regression

   * Accuracy: 80.67%

2. Random Forest Classifier

   * Accuracy: 79.82%

3. Decision Tree Classifier

   * Accuracy: Approximately 74%

Among all tested models, Logistic Regression achieved the highest accuracy and was selected as the final prediction model.

---

7. Important Features Influencing Churn Prediction

---

The Logistic Regression feature importance analysis identified the following important factors:

* Dependents status
* Contract type
* Internet service type
* Phone service
* Online Security
* Tech Support
* Payment method
* Paperless billing

These features have a significant impact on whether a customer is likely to churn or stay.

---

8. Final Prediction System

---

The final Logistic Regression model was saved using Joblib.

The saved model can be loaded and used to predict churn for new customers.

Example:

Customer Churn Prediction: No

Actual Churn: No

The prediction system successfully identifies customer churn patterns using machine learning.

---

9. Business Recommendation

---

Based on the analysis, the company can reduce churn by:

* Encouraging customers to choose long-term contracts.
* Improving services for fiber optic customers.
* Providing better technical support and security services.
* Identifying high-risk customers early using the machine learning model.
* Creating targeted retention strategies for customers likely to churn.

## Conclusion

This project demonstrates how machine learning can help businesses understand customer behavior and predict churn.

The Logistic Regression model achieved approximately 80.67% accuracy and provided insights into the major factors affecting customer retention.
