# Super Store Sales Prediction

## Project Overview

**Super Store Sales Prediction** is a Machine Learning project that predicts the sales of a product at a particular outlet using information about the product and the outlet.

The project uses **K-Nearest Neighbors (KNN) Regression** to learn the relationship between product/outlet characteristics and `Item_Outlet_Sales`.

The dataset contains **8,523 records and 12 columns**.

---

## Problem Statement

Retail stores need accurate sales predictions to support inventory management, business planning, product placement, and sales forecasting.

The objective of this project is to build a **KNN Regression model** that predicts `Item_Outlet_Sales` using available product and outlet-related features.

---

## Dataset

The dataset used in this project is:

`KNN_reg_outlet_sales.csv`

### Dataset Features

| Column | Description |
|---|---|
| `Item_Identifier` | Unique identifier of the product |
| `Item_Weight` | Weight of the product |
| `Item_Fat_Content` | Fat-content category of the product |
| `Item_Visibility` | Visibility of the product in the outlet |
| `Item_Type` | Category/type of the product |
| `Item_MRP` | Maximum Retail Price of the product |
| `Outlet_Identifier` | Unique identifier of the outlet |
| `Outlet_Establishment_Year` | Year the outlet was established |
| `Outlet_Size` | Size of the outlet |
| `Outlet_Location_Type` | Location category of the outlet |
| `Outlet_Type` | Type of outlet |
| `Item_Outlet_Sales` | Sales of the product at the outlet; this is the target variable |

---

## Machine Learning Approach

This project uses **K-Nearest Neighbors (KNN) Regression**.

KNN Regression predicts the value of a new data point by finding the nearest training data points and calculating a prediction based on their target values.

### General Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Handling Missing Values
   ↓
Encoding Categorical Features
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
KNN Regression
   ↓
Sales Prediction
   ↓
Model Evaluation
```

---

## Target Variable

The target variable is:

`Item_Outlet_Sales`

The model uses the remaining relevant product and outlet features to predict the expected sales.

---

## Data Preprocessing

The following preprocessing steps are required:

1. Load the CSV dataset.
2. Inspect the dataset for missing values.
3. Handle missing values in numerical and categorical columns.
4. Convert categorical variables into numerical form using suitable encoding.
5. Remove or transform identifier columns where appropriate.
6. Separate input features (`X`) and target variable (`y`).
7. Split the dataset into training and testing sets.
8. Apply feature scaling because KNN is distance-based.

Feature scaling is especially important for KNN because features with larger numerical ranges can otherwise have a greater influence on distance calculations.

---

## Model

### K-Nearest Neighbors Regression

KNN Regression is a supervised machine learning algorithm used for predicting continuous numerical values.

For a new data point, KNN:

1. Calculates the distance between the new point and training points.
2. Finds the **K nearest points**.
3. Uses the target values of those neighboring points.
4. Calculates their average or weighted average.
5. Uses the result as the predicted sales value.

### Important Parameter

`K` represents the number of nearest neighbors considered during prediction.

A suitable value of K can be selected by testing multiple values and comparing their validation performance.

---

## Model Evaluation

The trained model can be evaluated using regression metrics such as:

- **Mean Absolute Error (MAE)** – measures the average absolute difference between actual and predicted sales.
- **Mean Squared Error (MSE)** – measures the average squared prediction error.
- **Root Mean Squared Error (RMSE)** – represents the square root of MSE and is expressed in the same units as sales.
- **R² Score** – measures how well the model explains the variation in the target variable.

A higher R² score and lower MAE/RMSE generally indicate better model performance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

---

## Project Structure

```text
Super-Store-Sales-Prediction/
│
├── KNN_reg_outlet_sales.csv
├── Super_Store_Sales_Prediction.ipynb
├── README.md
└── requirements.txt
```

---

## Installation

Install the required Python libraries using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

---

## How to Run

1. Download or clone the project.
2. Keep `KNN_reg_outlet_sales.csv` in the project directory.
3. Open the Jupyter Notebook:

```bash
jupyter notebook
```

4. Open `Super_Store_Sales_Prediction.ipynb`.
5. Run the cells in order.
6. The trained KNN Regression model will generate sales predictions and evaluation results.

---

## Applications

The project can be useful for:

- Retail sales forecasting
- Inventory planning
- Product demand analysis
- Outlet performance analysis
- Business decision-making
- Identifying factors affecting product sales

---

## Advantages

- Simple and easy-to-understand algorithm.
- Does not require a complex mathematical model.
- Can model nonlinear relationships.
- Useful for regression problems with suitable feature preprocessing.

## Limitations

- Prediction can be computationally expensive for large datasets.
- Performance depends strongly on the choice of K.
- Feature scaling is important.
- Irrelevant features can affect distance calculations.
- KNN can be sensitive to noisy data and outliers.

---

## Conclusion

The **Super Store Sales Prediction** project applies **K-Nearest Neighbors Regression** to predict product sales at different outlets.

By using product characteristics such as item weight, fat content, visibility, type, and MRP along with outlet characteristics such as outlet size, location, establishment year, and outlet type, the project aims to estimate `Item_Outlet_Sales`.

The resulting model can demonstrate how machine learning can be applied to retail sales prediction and support data-driven business decisions.

---

