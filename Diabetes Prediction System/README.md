# 🩸 DiabetesAI — Medical Intelligence Dashboard

An interactive **machine-learning based diabetes risk assessment dashboard** built with **Python, Streamlit, Pandas, NumPy, Plotly, and Scikit-Learn**.

The application provides a professional clinical-style interface for entering patient measurements, generating a diabetes-risk prediction using a **Decision Tree Classifier**, visualizing the result, maintaining prediction history, and exploring the training dataset.

> **Important:** This project is intended for **educational, portfolio, and analytical demonstration purposes only**. It is not a medical diagnostic system and must not be used as a substitute for evaluation by a qualified healthcare professional.

---

## 📌 Project Overview

DiabetesAI is designed as a decision-support style application that evaluates a patient's clinical measurements using a previously trained machine-learning classification model.

The dashboard includes:

- Patient assessment and diabetes-risk prediction
- Probability-based risk classification
- Interactive risk visualizations
- Patient metric comparison
- Prediction history logging
- Dataset exploration and basic EDA
- Model architecture and feature-order information
- Educational clinical insights
- Downloadable prediction reports

---

## ✨ Key Features

### 🔮 1. Prediction Engine

The Prediction Engine accepts **8 numerical patient features**:

| Feature | Description |
|---|---|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree score |
| Age | Patient age in years |

The application sends the values to the loaded machine-learning model and returns:

- Model classification
- Diabetes probability
- Assessed risk tier
- Classification confidence
- Risk probability gauge
- Normalized patient-metric visualization
- Contributory insights
- Downloadable CSV clinical summary

---

### 📊 2. Risk Classification

The application categorizes the calculated diabetes probability into four risk tiers:

| Probability | Risk Category |
|---:|---|
| `0–30%` | 🟢 Low Risk |
| `>30–60%` | 🟡 Moderate Risk |
| `>60–80%` | 🟠 High Risk |
| `>80–100%` | 🔴 Very High Risk |

The final prediction itself is returned by the classification model as:

- `0` → No diabetes classification
- `1` → Diabetes classification

---

### 📈 3. Interactive Visualizations

The dashboard uses **Plotly** to provide interactive visual analysis.

#### Risk Probability Meter
A radial gauge displays the predicted diabetes probability from 0% to 100%.

#### Relative Metric Spectrum
A radar-style chart compares selected patient measurements after normalization against predefined reference bounds.

---

### 🧠 4. Decision Context

The dashboard provides human-readable insights based on important patient measurements such as:

- Glucose
- BMI
- Age

These messages provide context around factors associated with the displayed risk assessment.

---

### 📜 5. Prediction History

Every executed prediction can be recorded in:

```text
prediction_history.csv
```

The history contains:

- Timestamp
- Patient features
- Prediction
- Probability
- Risk level

The history page displays the records in a structured table and supports CSV export.

---

### 🗂 6. Dataset Explorer

The Dataset Explorer provides basic training-data inspection, including:

- Total records
- Total features
- Positive instances
- Raw dataset sample
- Feature distribution visualization

The supplied dataset contains:

- **768 records**
- **8 input features**
- **1 target column**
- **500 Outcome = 0**
- **268 Outcome = 1**

Dataset columns:

```text
Pregnancies
Glucose
BloodPressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age
Outcome
```

---

### 🤖 7. Model Architecture

The application is configured to use a **Decision Tree Classifier**.

Model configuration displayed by the application:

| Parameter | Value |
|---|---|
| Algorithm | Decision Tree Classifier |
| Max Depth | 7 |
| Min Samples Leaf | 15 |
| Min Samples Split | 2 |
| Target Variable | Outcome |
| Feature Count | 8 |

The application loads the serialized model and feature ordering from:

```text
diabetes_model.pkl
diabetes_features.pkl
```

---

## 🏗️ Application Architecture

```text
                    ┌──────────────────────────┐
                    │       User Input         │
                    │  8 Clinical Measurements │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     Streamlit UI Layer   │
                    │ Validation + Form Inputs │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Decision Tree Model    │
                    │   diabetes_model.pkl     │
                    └────────────┬─────────────┘
                                 │
                     ┌───────────┴───────────┐
                     ▼                       ▼
              ┌──────────────┐       ┌──────────────┐
              │ Prediction   │       │ Probability  │
              │   0 / 1      │       │   0–100%     │
              └──────┬───────┘       └──────┬───────┘
                     │                       │
                     └───────────┬───────────┘
                                 ▼
                    ┌──────────────────────────┐
                    │      Risk Assessment     │
                    │ Low / Moderate / High /  │
                    │       Very High Risk     │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       ┌────────────┐     ┌────────────┐     ┌─────────────┐
       │ Plotly      │     │ Prediction │     │ CSV Report  │
       │ Visuals     │     │ History    │     │ Download    │
       └────────────┘     └────────────┘     └─────────────┘
```

---

## 🖥️ Dashboard Pages

The application contains the following navigation sections:

1. **🏠 Overview**
   - Project introduction
   - Core feature scope
   - High-level system information

2. **🔮 Prediction Engine**
   - Patient clinical inputs
   - Risk calculation
   - Classification result
   - Interactive visualizations
   - Clinical summary export

3. **📊 Analytics Hub**
   - Total assessments
   - Positive and negative classifications
   - Mean risk score
   - Historical classification charts
   - Risk-tier distribution

4. **📜 Prediction History**
   - Stored assessment records
   - Historical registry
   - CSV export

5. **🗂 Dataset Explorer**
   - Dataset statistics
   - Raw data sample
   - Feature distribution charts

6. **🤖 Model Architecture**
   - Algorithm details
   - Hyperparameter configuration
   - Feature ordering

7. **📚 Clinical Insights**
   - Educational information about major diabetes-related measurements

8. **ℹ️ About**
   - Project and technology information

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application and ML integration |
| Streamlit | Interactive web dashboard |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-Learn | Machine-learning model |
| Plotly Express | Interactive charts |
| Plotly Graph Objects | Gauge and radar-style visualizations |
| Pickle | Loading serialized ML model artifacts |
| CSS / HTML | Dashboard styling and theme |

---

## 📁 Project Structure

A typical project directory can be organized as:

```text
DiabetesAI/
│
├── app.py
├── diabetes.csv
├── diabetes_model.pkl
├── diabetes_features.pkl
├── prediction_history.csv
├── README.md
│
└── assets/
    └── (optional project assets)
```

### File descriptions

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `diabetes.csv` | Diabetes dataset used for dataset exploration |
| `diabetes_model.pkl` | Serialized Decision Tree model |
| `diabetes_features.pkl` | Stored feature ordering used by the model |
| `prediction_history.csv` | Historical prediction records |
| `README.md` | Project documentation |

`prediction_history.csv` is automatically created by the application when it does not already exist.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd DiabetesAI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install streamlit pandas numpy scikit-learn plotly
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

After startup, open the local Streamlit address shown in the terminal, typically:

```text
http://localhost:8501
```

---

## 🔐 Required Model Files

Before running the application, make sure these files are available in the same working directory as `app.py`:

```text
diabetes_model.pkl
diabetes_features.pkl
```

The application loads them during startup.

If either file is missing or cannot be loaded, the application displays a critical model-loading error and stops execution.

---

## 🧪 Dataset

The supplied diabetes dataset contains **768 patient records** and **9 columns**:

- 8 predictive features
- 1 target variable (`Outcome`)

### Target Variable

```text
Outcome = 0
Outcome = 1
```

Dataset distribution:

```text
Outcome 0 → 500 records
Outcome 1 → 268 records
```

The dataset is used by the Dataset Explorer for analysis and inspection.

---

## 📄 Prediction Report

After an assessment, the application generates a downloadable CSV summary containing information such as:

```text
Patient Classification
Diabetes Probability
Assessed Risk Category
Glucose
Blood Pressure
BMI
Insulin
Age
Pedigree Function
Assessment Timestamp
```

The generated filename follows the pattern:

```text
DiabetesAI_Report_YYYYMMDD_HHMMSS.csv
```

---

## 📊 Example Workflow

```text
Launch Application
       │
       ▼
Open Prediction Engine
       │
       ▼
Enter Patient Measurements
       │
       ▼
Click "Execute Risk Analysis"
       │
       ▼
Decision Tree Prediction
       │
       ├──────────────► Classification
       │
       ├──────────────► Diabetes Probability
       │
       ├──────────────► Risk Category
       │
       └──────────────► Confidence
       │
       ▼
View Interactive Charts
       │
       ▼
Download Clinical Summary
       │
       ▼
Prediction Stored in History
```

---

## 🎯 Project Objectives

The main objectives of DiabetesAI are:

- Build a user-friendly machine-learning dashboard for diabetes risk assessment.
- Demonstrate integration of a trained classification model with Streamlit.
- Visualize model outputs using interactive charts.
- Maintain a local prediction history.
- Provide basic exploratory dataset analysis.
- Demonstrate how machine learning can be integrated into a healthcare-oriented decision-support interface.
- Present model information and feature inputs in a professional dashboard.

---

## 🔮 Future Enhancements

Possible improvements include:

- Model comparison using Random Forest, Logistic Regression, XGBoost, and other classifiers
- Cross-validation and model-performance reporting
- ROC-AUC, precision, recall, F1-score, and confusion-matrix analysis
- SHAP-based feature explanations
- More advanced patient trend analytics
- Database-backed prediction history
- User authentication and role-based access
- PDF report generation
- Cloud deployment
- API-based model serving
- Model monitoring and drift detection
- Improved clinical validation workflows

---

## ⚠️ Medical Disclaimer

**DiabetesAI is an educational and portfolio project.**

The predictions generated by this software are based on a machine-learning model and should **not** be interpreted as a clinical diagnosis, medical recommendation, or treatment decision.

Do not use this application to make decisions about medication, treatment, or personal medical care.

For real-world medical concerns, consult a qualified healthcare professional.

---

## 👨‍💻 Project Information

**Project Name:** DiabetesAI — Medical Intelligence Dashboard

**Application Type:** Machine Learning + Healthcare Analytics Dashboard

**Primary Framework:** Streamlit

**Machine Learning Algorithm:** Decision Tree Classifier

**Input Features:** 8

**Target:** `Outcome`

---

## 📜 License

This project can be used for educational and portfolio purposes. Add an appropriate open-source license, such as MIT, to the repository if you intend to distribute the project publicly.

---

## ⭐ Acknowledgement

This project demonstrates the integration of:

```text
Machine Learning
        +
Healthcare Analytics
        +
Data Visualization
        +
Interactive Web Application
```

to create a practical educational prototype for diabetes risk assessment.
