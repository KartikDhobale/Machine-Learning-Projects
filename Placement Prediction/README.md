# 🎓 Placement Prediction

A machine learning project that predicts whether a student is likely to be **Placed** or **Not Placed** based on academic performance, aptitude, and profile-related attributes.

---

## 📌 Project Overview

**Placement Prediction** is a supervised machine learning classification project designed to predict the placement status of students using important student-related features.

The project uses attributes such as:

* CGPA
* IQ Score
* Profile Score

to predict whether a student is likely to receive a placement.

The target variable is:

> **`Placement`**

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, visualization, model training, evaluation, and prediction.

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze the factors affecting student placement.
2. Understand the relationship between academic performance and placement.
3. Perform exploratory data analysis on student data.
4. Preprocess the dataset for machine learning.
5. Train classification algorithms.
6. Evaluate the performance of trained models.
7. Predict whether a student is likely to be placed.
8. Identify the important factors influencing placement outcomes.

---

## 📂 Dataset

The dataset contains student information related to placement outcomes.

### Dataset Features

| Feature         | Description                                      | Type        |
| --------------- | ------------------------------------------------ | ----------- |
| `CGPA`          | Cumulative Grade Point Average of the student    | Numerical   |
| `IQ`            | Intelligence/aptitude score of the student       | Numerical   |
| `Profile_Score` | Score representing the student's overall profile | Numerical   |
| `Placement`     | Placement outcome of the student                 | Categorical |

### Target Variable

```text
Placement
```

Possible target classes:

```text
Placed
Not Placed
```

This makes the project a **Binary Classification** problem.

---

## 🧠 Machine Learning Problem

This project uses **Supervised Machine Learning – Classification**.

### Input Features

```text
CGPA
IQ
Profile_Score
```

### Output

```text
Placed / Not Placed
```

The model learns patterns from previously observed student records and uses those patterns to classify new students.

---

## 🔄 Project Workflow

```text
                  ┌──────────────────────┐
                  │   Student Dataset    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Data Preprocessing   │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Exploratory Data     │
                  │ Analysis (EDA)       │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Feature Selection    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Train-Test Split     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Model Training       │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Model Evaluation     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Placement Prediction │
                  └──────────────────────┘
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data loading and manipulation
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – Machine learning
* **Jupyter Notebook / Google Colab** – Development and experimentation

---

## 📦 Python Libraries

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## 🧹 Data Preprocessing

### 1. Load the Dataset

The dataset can be loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv("placement.csv")
```

### 2. Inspect the Dataset

The following commands can be used to understand the dataset:

```python
df.head()
df.info()
df.describe()
df.isnull().sum()
```

These operations help identify:

* Number of records
* Available features
* Data types
* Missing values
* Statistical information
* Potential data-quality issues

### 3. Handle Missing Values

Missing values should be identified and handled before training the model.

Depending on the dataset, possible approaches include:

* Removing incomplete records
* Replacing missing numerical values with the mean or median
* Using appropriate imputation techniques

### 4. Encode the Target Variable

The categorical target:

```text
Placed
Not Placed
```

can be converted into numerical values such as:

```text
Placed      → 1
Not Placed  → 0
```

---

## 📊 Exploratory Data Analysis

EDA helps understand which student characteristics may be associated with successful placement.

### CGPA vs Placement

Students with higher academic performance can be analyzed to determine whether they have a higher placement rate.

### IQ vs Placement

The relationship between aptitude/IQ score and placement status can be visualized.

### Profile Score vs Placement

The profile score can be analyzed to determine its relationship with placement outcomes.

### Recommended Visualizations

#### Placement Distribution

```python
sns.countplot(data=df, x="Placement")
```

#### CGPA Distribution

```python
sns.histplot(data=df, x="CGPA", kde=True)
```

#### CGPA vs IQ

```python
sns.scatterplot(
    data=df,
    x="CGPA",
    y="IQ",
    hue="Placement"
)
```

#### Correlation Heatmap

```python
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)
```

---

## 🤖 Machine Learning Models

Since the target variable contains two classes, classification algorithms can be used.

### Recommended Algorithms

#### 1. Logistic Regression

A simple and effective baseline classification algorithm that estimates the probability of a student being placed.

#### 2. K-Nearest Neighbors (KNN)

Classifies a student based on the placement outcomes of similar students.

#### 3. Decision Tree Classifier

Creates decision rules based on student features such as CGPA, IQ, and profile score.

#### 4. Random Forest Classifier

Combines multiple decision trees to improve classification performance and robustness.

#### 5. Support Vector Machine (SVM)

Finds an optimal decision boundary between placed and not-placed students.

---

## 🧪 Train-Test Split

The dataset can be divided into training and testing subsets.

```python
from sklearn.model_selection import train_test_split

X = df[["CGPA", "IQ", "Profile_Score"]]
y = df["Placement"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

> Because the uploaded dataset is very small, model evaluation results may vary significantly depending on the train-test split. A larger dataset would provide more reliable performance estimates.

---

## 📏 Model Evaluation

Classification models can be evaluated using the following metrics.

### Accuracy

Measures the percentage of correctly classified students.

```text
Accuracy =
Correct Predictions / Total Predictions
```

Higher accuracy indicates better overall classification performance.

### Precision

Measures how many students predicted as placed were actually placed.

### Recall

Measures how many of the actually placed students were correctly identified.

### F1-Score

The harmonic mean of precision and recall.

### Confusion Matrix

A confusion matrix provides a detailed view of:

```text
                    Predicted
                  Not Placed   Placed
Actual Not Placed    TN          FP
Actual Placed       FN          TP
```

---

## 🏗️ Suggested Project Structure

```text
Placement-Prediction/
│
├── dataset/
│   └── placement.csv
│
├── notebooks/
│   └── placement_prediction.ipynb
│
├── src/
│   └── placement_prediction.py
│
├── models/
│   └── placement_model.pkl
│
├── README.md
│
└── requirements.txt
```

---

## 🚀 Implementation Steps

### Step 1 — Load Dataset

Load the placement dataset using Pandas.

### Step 2 — Data Inspection

Analyze:

* Dataset shape
* Column names
* Data types
* Missing values
* Duplicate records
* Class distribution

### Step 3 — Data Cleaning

Handle missing, duplicated, or incorrectly formatted records.

### Step 4 — Exploratory Data Analysis

Analyze the relationship between:

```text
CGPA ↔ Placement
IQ ↔ Placement
Profile Score ↔ Placement
```

### Step 5 — Feature and Target Selection

```python
X = df[["CGPA", "IQ", "Profile_Score"]]
y = df["Placement"]
```

### Step 6 — Encode Target

Convert `Placed` and `Not Placed` into numerical classes.

### Step 7 — Split the Dataset

Separate the data into training and testing sets.

### Step 8 — Train Classification Models

Train one or more classification algorithms.

### Step 9 — Evaluate Models

Compare models using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Step 10 — Select the Best Model

Select the model that provides the most suitable performance based on the evaluation metrics.

### Step 11 — Predict New Student Placement

Use the trained model to predict the placement status of a new student.

---

## 🔮 Prediction Example

A new student's information can be provided to the trained model.

Example:

```text
CGPA            : 8.5
IQ              : 120
Profile Score   : 80
```

The model may produce:

```text
Prediction: Placed
```

or:

```text
Prediction: Not Placed
```

The prediction depends entirely on the trained model and the data used for training.

---

## 📈 Expected Outcomes

The project is expected to:

* Predict student placement status.
* Identify relationships between student characteristics and placement.
* Compare multiple classification algorithms.
* Determine important factors affecting placement.
* Demonstrate the practical application of machine learning classification.
* Provide a foundation for a student placement prediction system.

---

## ⚠️ Dataset Limitation

The currently supplied CSV is **very small and appears to contain formatting inconsistencies**. In particular, the first record is being interpreted as a header and one record contains a concatenated value.

Before using the dataset for final model training, the CSV should be corrected into the intended structure:

```text
CGPA,IQ,Profile_Score,Placement
9.5,140,95,Placed
8.5,100,50,Not Placed
8.5,120,80,Placed
...
```

For a reliable machine learning project, a substantially larger dataset is recommended.

---

## 💡 Future Enhancements

The project can be improved by:

* Increasing the dataset size
* Adding more student attributes
* Performing feature engineering
* Applying cross-validation
* Hyperparameter tuning
* Comparing multiple classification algorithms
* Implementing feature importance analysis
* Creating an interactive Streamlit application
* Deploying the trained model
* Adding probability-based placement predictions
* Providing personalized recommendations for improving placement chances

---

## 🌐 Possible Application

The trained model can be integrated into a web application.

```text
Student
   │
   ▼
Enter Academic & Profile Details
   │
   ▼
Data Preprocessing
   │
   ▼
Trained Classification Model
   │
   ▼
Placement Prediction
   │
   ├───────────────┐
   ▼               ▼
Placed          Not Placed
```

A web application could allow students to enter their CGPA, IQ, and profile score and receive an estimated placement classification.

---

## 📚 Learning Outcomes

This project provides practical experience with:

* Supervised machine learning
* Binary classification
* Data preprocessing
* Exploratory data analysis
* Data visualization
* Feature selection
* Categorical encoding
* Train-test splitting
* Classification algorithms
* Model evaluation
* Confusion matrices
* Prediction
* Model comparison
* Machine learning project development

---

## 👨‍💻 Project Information

**Project Name:** Placement Prediction

**Project Type:** Machine Learning – Classification

**Domain:** Education / Career Analytics

**Target Variable:** `Placement`

**Classes:** `Placed`, `Not Placed`

**Programming Language:** Python

**Machine Learning Task:** Binary Classification

---

## 📄 License

This project is intended for **educational and academic purposes**. The dataset should be used according to the terms and conditions associated with its original source.

---

## ⭐ Conclusion

The **Placement Prediction** project demonstrates how machine learning can be applied to predict student placement outcomes using academic, aptitude, and profile-related information.

By analyzing factors such as **CGPA, IQ, and Profile Score**, classification algorithms can learn patterns from historical student data and classify new students as **Placed** or **Not Placed**.

The project provides a practical implementation of the machine learning lifecycle, from **data preprocessing and exploratory analysis to model training, evaluation, and prediction**.
