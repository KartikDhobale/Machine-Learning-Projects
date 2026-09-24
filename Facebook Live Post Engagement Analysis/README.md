# Facebook Live Post Engagement Analysis

## Project Name

**Facebook Live Post Engagement Analysis**

## Project Overview

This project analyzes a dataset of Facebook Live posts to understand user engagement and identify patterns in how different types of posts perform.

The analysis focuses on engagement metrics such as reactions, comments, and shares. Using Python and Exploratory Data Analysis (EDA), the project cleans the dataset, examines relationships between variables, and presents insights through visualizations.

The goal is to understand which post characteristics are associated with higher engagement and to demonstrate a practical end-to-end data analytics workflow.

## Objectives

- Understand the structure and characteristics of the Facebook Live dataset.
- Clean and prepare the data for analysis.
- Analyze Facebook post engagement using available reaction, comment, and share metrics.
- Compare engagement across different post types.
- Identify relationships and patterns among engagement variables.
- Create meaningful visualizations.
- Extract useful business and social-media insights from the data.

## Dataset

The project uses the uploaded `Live.csv` dataset.

### Dataset Size

- **Rows:** 7,050
- **Columns:** 16

### Main Columns

The dataset contains the following columns:

- `status_id`
- `status_type`
- `status_published`
- `num_reactions`
- `num_comments`
- `num_shares`
- `num_likes`
- `num_loves`
- `num_wows`
- `num_hahas`
- `num_sads`
- `num_angrys`
- `Column1`
- `Column2`
- `Column3`
- `Column4`

### Engagement Columns

The dataset includes these engagement-related fields:

- Engagement fields are available in the dataset; inspect the notebook for the exact metrics used.

### Missing Values

The dataset contains missing values in the following columns:

- `Column1`: 7,050
- `Column2`: 7,050
- `Column3`: 7,050
- `Column4`: 7,050

## Technologies Used

- **Python**
- **Pandas** – data loading and manipulation
- **NumPy** – numerical operations
- **Matplotlib** – data visualization
- **Seaborn** – statistical visualization
- **Jupyter Notebook / Google Colab** – development and analysis

## Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Visualization
   ↓
Engagement Analysis
   ↓
Key Insights
   ↓
Conclusion
```

## Data Analysis Performed

### 1. Data Loading

The `Live.csv` dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv("Live.csv")
```

### 2. Data Understanding

Basic dataset information is examined using:

```python
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
```

This helps understand the number of records, data types, numerical ranges, and missing values.

### 3. Data Cleaning

The data-preprocessing stage may include:

- Removing unnecessary columns.
- Checking duplicate records.
- Handling missing values.
- Correcting data types where required.
- Preparing categorical variables for analysis.
- Checking for unusual or extreme values.

Example:

```python
df = df.drop_duplicates()
```

### 4. Exploratory Data Analysis

EDA is performed to answer questions such as:

- Which types of Facebook posts receive more engagement?
- Which posts receive more comments?
- Which posts are shared more frequently?
- How do different reaction types vary?
- Which engagement metrics are strongly related?
- Are there noticeable patterns between post characteristics and engagement?

### 5. Visualization

Visualizations can include:

- Bar charts
- Count plots
- Histograms
- Box plots
- Scatter plots
- Correlation heatmaps
- Comparison charts

Example:

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(data=df, x="status_type")
plt.title("Distribution of Facebook Post Types")
plt.xticks(rotation=45)
plt.show()
```

## Key Analysis Areas

### Post Type Analysis

The project compares engagement across different Facebook post types. This helps identify whether certain content categories receive more interaction.

### Reaction Analysis

Different reaction metrics are analyzed to understand how users respond to posts.

### Comment Analysis

Comments are used as an indicator of active audience interaction and discussion.

### Share Analysis

Shares help measure how frequently users redistribute or spread posts.

### Correlation Analysis

Correlation analysis is used to examine relationships between numerical engagement metrics.

Example:

```python
correlation = df.corr(numeric_only=True)

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between Engagement Metrics")
plt.show()
```

## Sample Questions Answered

The analysis can answer questions such as:

1. What is the most common type of Facebook post?
2. Which post type receives the highest number of reactions?
3. Which post type generates the most comments?
4. Which post type receives the most shares?
5. Which reaction is most frequently recorded?
6. What is the relationship between reactions, comments, and shares?
7. Are there outliers in engagement?
8. Which content types appear to generate stronger audience interaction?

## Project Structure

```text
Facebook-Live-Post-Engagement-Analysis/
│
├── Live.csv
├── Facebook_Live_Engagement_Analysis.ipynb
├── README.md
└── images/
    └── visualizations/
```

> The notebook filename can be changed to match the actual notebook used in the project.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Facebook-Live-Post-Engagement-Analysis
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open the Analysis Notebook

Open:

```text
Facebook_Live_Engagement_Analysis.ipynb
```

Make sure `Live.csv` is located in the same project directory as the notebook.

## Expected Outcome

After completing the analysis, the project provides:

- A cleaned and analyzed Facebook Live dataset.
- Visual representation of engagement patterns.
- Comparison of different post types.
- Analysis of reactions, comments, and shares.
- Correlation analysis between engagement metrics.
- Data-driven insights about Facebook post engagement.

## Key Insights

The final insights should be based on the results generated in the notebook rather than assumptions about the dataset.

Typical insights to document include:

- The distribution of different post types.
- The post type with the highest engagement according to the selected metric.
- The most common reaction category.
- The relationship between comments, shares, and reactions.
- Important outliers or unusual engagement records.
- Content patterns that may be useful for social-media analysis.

## Business Applications

The analysis can be useful for:

- Social-media performance analysis.
- Content strategy development.
- Audience engagement research.
- Marketing analytics.
- Identifying high-engagement content.
- Data-driven social-media decision making.

## Future Scope

The project can be extended by:

- Building an interactive Power BI or Tableau dashboard.
- Creating an engagement score.
- Performing time-series analysis if reliable date/time fields are available.
- Applying machine-learning models to predict engagement.
- Performing customer/audience segmentation.
- Automating data collection from social-media sources.
- Deploying the analysis as an interactive web dashboard using Streamlit.

## Conclusion

The **Facebook Live Post Engagement Analysis** project demonstrates a complete data analytics workflow, starting from raw CSV data and progressing through data cleaning, exploratory analysis, visualization, and insight generation.

The project provides practical experience with Python, Pandas, data visualization, exploratory data analysis, and interpretation of social-media engagement data.

## Author

**Kartik Rajendra Dhobale**

**Department:** Artificial Intelligence and Data Science

---

## License

This project is intended for educational and academic purposes.
