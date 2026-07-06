# A Comprehensive Measure of Well-Being
## Human Development Index (HDI) Prediction using Machine Learning and Flask

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## 📌 Project Overview

The **Human Development Index (HDI) Predictor** is a Machine Learning web application that predicts the Human Development Index of a country using socioeconomic indicators.

The project combines **Data Analysis**, **Machine Learning**, and **Flask Web Development** to build an end-to-end prediction system.

Users enter important development indicators such as:

- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) Per Capita

The application predicts the **HDI Score** and classifies it into one of the following categories:

- Very High
- High
- Medium
- Low

---

# Objectives

- Understand the Human Development Index dataset.
- Perform Exploratory Data Analysis (EDA).
- Visualize important relationships among features.
- Build a Machine Learning prediction model.
- Evaluate model performance.
- Deploy the model using Flask.
- Develop a user-friendly web interface.

---

# Features

- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis
- Data Visualization
- Feature Engineering
- Linear Regression Model
- Model Evaluation
- HDI Score Prediction
- HDI Category Classification
- Flask Web Application
- Pickle Model Serialization

---

# Project Architecture

```
User
 │
 ▼
Flask Web Interface
 │
 ▼
Input Validation
 │
 ▼
Machine Learning Model
 │
 ▼
HDI Prediction
 │
 ▼
HDI Category
 │
 ▼
Display Results
```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-Learn | Machine Learning |
| Flask | Web Framework |
| HTML | Frontend |
| CSS | Styling |
| Bootstrap | Responsive UI |
| Pickle | Model Serialization |

---

# Folder Structure

```
HDI-Predictor/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── HDI.csv
│
├── model/
│   └── hdi.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── images/
```

---

# Dataset Features

| Feature | Description |
|----------|-------------|
| Country | Country Name |
| Life Expectancy | Average Life Expectancy |
| Expected Years of Schooling | Expected Education Years |
| Mean Years of Schooling | Average Education Years |
| GNI Per Capita | Gross National Income |
| HDI | Human Development Index |

---

# Machine Learning Workflow

### 1. Data Collection

- Load HDI Dataset
- Explore Dataset

### 2. Data Preprocessing

- Handle Missing Values
- Mean Imputation
- Label Encoding
- Feature Selection
- Train-Test Split

### 3. Exploratory Data Analysis

Visualizations include:

- Distribution Plots
- Scatter Plots
- Strip Plots
- Heatmaps
- Correlation Matrix
- Pair Plots

### 4. Model Building

Algorithm Used:

- Linear Regression

### 5. Model Evaluation

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### 6. Model Serialization

The trained model is saved using Pickle.

```
model/hdi.pkl
```

### 7. Flask Deployment

The trained model is loaded into the Flask application for prediction.

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HDI-Predictor.git
```

Move into the project directory

```bash
cd human-development-index-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open the browser

```
http://127.0.0.1:5000/
```

---

# User Inputs

The application accepts:

- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- GNI Per Capita

---

# Output

The application displays:

- Predicted HDI Score
- HDI Category

Example:

```
Predicted HDI Score

0.912

Category

Very High Human Development
```

---

# Screenshots

Include screenshots of:

- Home Page
- Input Form
- Prediction Result
- Data Visualization
- Heatmap
- Scatter Plot
- Model Evaluation

---

# Future Enhancements

- Add Random Forest Regression
- Add XGBoost Regressor
- Improve Prediction Accuracy
- Deploy on Render
- Deploy on Railway
- Deploy on AWS
- Add Interactive Charts
- Add Country Comparison Dashboard
- Use Latest UNDP Dataset

---

# Learning Outcomes

After completing this project, you will understand:

- Data Analysis
- Exploratory Data Analysis
- Machine Learning Workflow
- Regression Algorithms
- Model Evaluation
- Flask Development
- Model Deployment
- End-to-End AI Project Development

---

# Requirements

```
Flask
numpy
pandas
matplotlib
seaborn
scikit-learn
pickle-mixin
```

Install using

```bash
pip install -r requirements.txt
```

---

# Author

Shaik Nazeer Ahmad

AI & Machine Learning Student

---

# License

This project is created for educational and learning purposes.

---

## ⭐ If you found this project useful, don't forget to star the repository!
