# 🏠 House Price Prediction

A machine learning project that predicts **residential property prices** based on property characteristics, location, size, amenities, accessibility, and other housing-related features.

---

## 📌 Project Overview

**House Price Prediction** is a supervised machine learning project designed to estimate the price of a residential property using historical property data.

The project uses information such as:

* Location
* Property type
* Number of bedrooms (BHK)
* Property size
* Year built
* Furnishing status
* Floor information
* Property age
* Nearby schools and hospitals
* Public transport accessibility
* Parking availability
* Security
* Amenities
* Property facing
* Owner type
* Availability status

The target variable for prediction is:

> **`Price_in_Lakhs`**

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and price prediction.

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze the factors affecting house prices.
2. Perform exploratory data analysis on the housing dataset.
3. Clean and preprocess categorical and numerical data.
4. Convert categorical features into machine-readable form.
5. Train machine learning regression models.
6. Evaluate model performance using appropriate regression metrics.
7. Identify important features influencing property prices.
8. Predict the estimated price of new properties.

---

## 📂 Dataset

The dataset contains **999 property records** and **23 features**.

### Dataset Features

| Feature                          | Description                              | Type             |
| -------------------------------- | ---------------------------------------- | ---------------- |
| `ID`                             | Unique property identifier               | Numerical        |
| `State`                          | State where the property is located      | Categorical      |
| `City`                           | City where the property is located       | Categorical      |
| `Locality`                       | Locality identifier/name                 | Categorical      |
| `Property_Type`                  | Type of property                         | Categorical      |
| `BHK`                            | Number of bedrooms, hall and kitchen     | Numerical        |
| `Size_in_SqFt`                   | Property area in square feet             | Numerical        |
| `Price_in_Lakhs`                 | Property price in lakhs; target variable | Numerical        |
| `Price_per_SqFt`                 | Price per square foot                    | Numerical        |
| `Year_Built`                     | Year in which the property was built     | Numerical        |
| `Furnished_Status`               | Furnishing condition                     | Categorical      |
| `Floor_No`                       | Floor number of the property             | Numerical        |
| `Total_Floors`                   | Total floors in the building             | Numerical        |
| `Age_of_Property`                | Age of the property                      | Numerical        |
| `Nearby_Schools`                 | Number of nearby schools                 | Numerical        |
| `Nearby_Hospitals`               | Number of nearby hospitals               | Numerical        |
| `Public_Transport_Accessibility` | Accessibility to public transportation   | Categorical      |
| `Parking_Space`                  | Availability of parking                  | Categorical      |
| `Security`                       | Availability of security                 | Categorical      |
| `Amenities`                      | Available property amenities             | Categorical/Text |
| `Facing`                         | Direction the property faces             | Categorical      |
| `Owner_Type`                     | Type of property owner/seller            | Categorical      |
| `Availability_Status`            | Current availability status              | Categorical      |

---

## 🧠 Machine Learning Problem

This project is a **Supervised Learning – Regression** problem.

### Input

Property-related features such as:

```text
State
City
Property_Type
BHK
Size_in_SqFt
Year_Built
Furnished_Status
Floor_No
Total_Floors
Age_of_Property
Nearby_Schools
Nearby_Hospitals
Public_Transport_Accessibility
Parking_Space
Security
Amenities
Facing
Owner_Type
Availability_Status
```

### Output

```text
Predicted House Price
```

The target variable is:

```text
Price_in_Lakhs
```

---

## 🔄 Project Workflow

```text
                    ┌─────────────────────┐
                    │   Housing Dataset   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Exploratory Data    │
                    │ Analysis (EDA)      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Train-Test Split    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Model Training      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Model Evaluation    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ House Price         │
                    │ Prediction          │
                    └─────────────────────┘
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – Machine learning and preprocessing
* **Jupyter Notebook / Google Colab** – Development and experimentation

---

## 📦 Python Libraries

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## 🧹 Data Preprocessing

The following preprocessing steps can be performed:

### 1. Data Loading

The CSV dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv("house_price_dataset.csv")
```

### 2. Data Inspection

The dataset is inspected using:

```python
df.head()
df.info()
df.describe()
df.isnull().sum()
```

This helps identify:

* Dataset structure
* Data types
* Missing values
* Numerical distributions
* Potential outliers

### 3. Handling Categorical Variables

Categorical columns such as:

```text
State
City
Property_Type
Furnished_Status
Public_Transport_Accessibility
Parking_Space
Security
Facing
Owner_Type
Availability_Status
```

can be encoded using techniques such as:

* One-Hot Encoding
* Label Encoding

### 4. Feature Selection

The target variable is:

```text
Price_in_Lakhs
```

The `ID` column should generally not be used as a predictive feature because it is only an identifier.

---

## 📊 Exploratory Data Analysis

EDA can be performed to understand relationships between property characteristics and prices.

Recommended visualizations include:

### Price Distribution

```python
sns.histplot(df["Price_in_Lakhs"], kde=True)
```

### Property Size vs Price

```python
sns.scatterplot(
    data=df,
    x="Size_in_SqFt",
    y="Price_in_Lakhs"
)
```

### BHK vs Price

```python
sns.boxplot(
    data=df,
    x="BHK",
    y="Price_in_Lakhs"
)
```

### Correlation Analysis

A correlation heatmap can be used to analyze relationships among numerical variables.

```python
sns.heatmap(df.corr(numeric_only=True), annot=True)
```

---

## 🤖 Machine Learning Models

Different regression algorithms can be trained and compared.

### Recommended Models

#### 1. Linear Regression

Provides a simple baseline model for predicting house prices.

#### 2. Decision Tree Regressor

Captures nonlinear relationships between property characteristics and price.

#### 3. Random Forest Regressor

Uses multiple decision trees and generally provides stronger performance for complex tabular datasets.

#### 4. Gradient Boosting Regressor

Builds models sequentially to reduce prediction errors and can perform well on structured datasets.

---

## 📏 Model Evaluation

Since this is a regression problem, the following metrics can be used.

### Mean Absolute Error — MAE

Measures the average absolute difference between actual and predicted prices.

```text
MAE = Average(|Actual Price - Predicted Price|)
```

Lower MAE indicates better performance.

### Mean Squared Error — MSE

Penalizes larger prediction errors more heavily.

```text
MSE = Average((Actual Price - Predicted Price)²)
```

Lower MSE is better.

### Root Mean Squared Error — RMSE

The square root of MSE.

```text
RMSE = √MSE
```

Lower RMSE indicates better prediction performance.

### R² Score

Measures how well the model explains the variation in house prices.

```text
R² = 1 - (SS_res / SS_tot)
```

A value closer to **1.0** indicates better model performance.

---

## 🏗️ Suggested Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── house_price_dataset.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   └── house_price_prediction.py
│
├── models/
│   └── house_price_model.pkl
│
├── README.md
│
└── requirements.txt
```

---

## 🚀 Implementation Steps

### Step 1 — Load Dataset

Load the CSV file using Pandas.

### Step 2 — Understand the Data

Check:

* Shape
* Columns
* Data types
* Missing values
* Duplicate records
* Statistical summary

### Step 3 — Clean the Dataset

Handle:

* Missing values
* Duplicate records
* Invalid values
* Categorical data
* Outliers where appropriate

### Step 4 — Perform EDA

Analyze how different features affect property prices.

### Step 5 — Prepare Features and Target

```python
X = df.drop("Price_in_Lakhs", axis=1)
y = df["Price_in_Lakhs"]
```

Remove non-predictive identifiers such as `ID` where appropriate.

### Step 6 — Encode Categorical Features

Categorical variables should be converted into numerical representations using an appropriate encoding technique.

### Step 7 — Split the Dataset

The dataset can be divided into training and testing sets.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Step 8 — Train Regression Models

Train multiple regression algorithms and compare their performance.

### Step 9 — Evaluate Models

Calculate:

* MAE
* MSE
* RMSE
* R² Score

### Step 10 — Select the Best Model

The model with the best overall evaluation performance can be selected for final house price prediction.

---

## 🔮 Prediction Example

After training the final model, new property information can be supplied to obtain an estimated price.

Example input:

```text
Property Type       : Apartment
BHK                 : 3
Size                : 1800 Sq.Ft
Year Built          : 2015
Furnished Status    : Furnished
Parking             : Yes
Security            : Yes
Transport Access    : High
```

The trained model produces an estimated:

```text
Predicted Price: XX Lakhs
```

> The actual predicted value depends on the trained model and supplied property features.

---

## 📈 Expected Outcomes

The project is expected to:

* Identify important factors affecting property prices.
* Discover relationships between property size, location, BHK, age, and price.
* Compare different regression algorithms.
* Select an appropriate model for price prediction.
* Provide estimated property prices for new observations.

---

## ⚠️ Important Dataset Consideration

The dataset contains both **`Price_in_Lakhs`** and **`Price_per_SqFt`**.

Before model training, feature selection should be handled carefully because `Price_per_SqFt` is directly related to property price and property size.

Including it may introduce **target leakage**, depending on how `Price_per_SqFt` was calculated in the original dataset.

For a more realistic house-price prediction system, consider training:

**Model 1 — Without `Price_per_SqFt`**

```text
Size + Location + BHK + Property Features → Price
```

and optionally comparing it with:

**Model 2 — Including `Price_per_SqFt`**

```text
Size + Location + Property Features + Price_per_SqFt → Price
```

This makes the model comparison more meaningful.

---

## 💡 Future Enhancements

The project can be extended with:

* Hyperparameter tuning
* Cross-validation
* Advanced ensemble models
* XGBoost or other gradient boosting algorithms
* Feature importance analysis
* Interactive prediction interface
* Streamlit web application
* Model deployment using cloud services
* Location-based visualization
* Automated model retraining
* Real-time property price estimation

---

## 🌐 Possible Application

A trained model can be integrated into a web application where users enter property details and receive an estimated house price.

```text
User
  │
  ▼
Property Details
  │
  ▼
Preprocessing
  │
  ▼
Trained ML Model
  │
  ▼
Predicted Price
  │
  ▼
Display Result
```

---

## 📚 Learning Outcomes

Through this project, the following concepts can be learned:

* Data preprocessing
* Exploratory data analysis
* Data visualization
* Feature engineering
* Categorical encoding
* Regression algorithms
* Train-test splitting
* Model evaluation
* Feature selection
* Model comparison
* Machine learning prediction
* Model deployment

---

## 👨‍💻 Project Information

**Project Name:** House Price Prediction

**Project Type:** Machine Learning – Regression

**Dataset Size:** 999 records × 23 columns

**Target Variable:** `Price_in_Lakhs`

**Programming Language:** Python

**Domain:** Real Estate / Machine Learning

---

## 📄 License

This project is intended for **educational and academic purposes**. The dataset and project implementation should be used according to the applicable terms of the original dataset source.

---

## ⭐ Conclusion

The **House Price Prediction** project demonstrates how machine learning can be used to estimate residential property prices from structured housing data.

By combining property characteristics, location information, accessibility, amenities, and other relevant attributes, regression algorithms can learn patterns in historical housing data and provide price estimates for new properties.

The project provides a practical implementation of the complete **machine learning lifecycle — from data preprocessing and analysis to model training, evaluation, and prediction**.
