# 🌍 Human Development Index (HDI) Prediction System

A Machine Learning based web application that predicts the **Human Development Index (HDI) category** of a country using key socio-economic indicators such as **Life Expectancy**, **Education**, and **Gross National Income (GNI)**.

---

# 📌 Project Overview

The Human Development Index (HDI) is a statistical measure developed by the **United Nations Development Programme (UNDP)** to evaluate a country's overall development.

This project uses a **Random Forest Classifier** to predict the HDI category of a country based on four important indicators.

The application is deployed using the **Flask** web framework with a modern and user-friendly interface.

---

# 🎯 Problem Statement

The Human Development Index (HDI) measures development using three major dimensions:

- ❤️ Health (Life Expectancy)
- 🎓 Education (Expected & Mean Years of Schooling)
- 💰 Standard of Living (Gross National Income Per Capita)

This project predicts whether a country belongs to one of the following HDI categories:

- 🌍 Very High
- 🟢 High
- 🟡 Medium
- 🔴 Low

---

# 🚀 Features

- Predict Human Development Index (HDI) category
- Machine Learning based prediction
- Flask Web Application
- Modern Dashboard User Interface
- Real-time Prediction
- Easy-to-use Input Form
- Responsive Design

---

# 🛠 Technologies Used

## Programming Language
- Python

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Web Framework
- Flask

## Frontend
- HTML5
- CSS3
- Tailwind CSS

## Development Tools
- VS Code
- Git
- GitHub

---

# 📊 Dataset

The project uses the **Human Development Report (HDR)** dataset.

### Important Features

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) Per Capita

Target Variable:

- HDI Category

---

# 🤖 Machine Learning Model

Algorithm Used:

**Random Forest Classifier**

### Why Random Forest?

- High Accuracy
- Handles Classification Problems Efficiently
- Reduces Overfitting
- Works Well with Structured Data
- Easy to Train

---

# 🌐 Web Application Workflow

1. User enters:
   - Life Expectancy
   - Expected Years of Schooling
   - Mean Years of Schooling
   - GNI Per Capita

2. Flask receives the input.

3. The trained Machine Learning model predicts the HDI category.

4. The prediction is displayed on the result page.

---

# 📁 Project Structure

```
HDI_Prediction_Project
│
├── dataset
│   └── HDR.csv
│
├── model
│   └── model.pkl
│
├── notebooks
│
├── screenshots
│
├── static
│   └── style.css
│
├── templates
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HDI_Prediction_Project.git
```

Move into the project folder

```bash
cd HDI_Prediction_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📷 Screenshots

## Home Page

(Add screenshot here)

---

## Prediction Result

(Add screenshot here)

---

# 🎯 Sample Prediction

### Input

Life Expectancy : 82

Expected Years of Schooling : 18

Mean Years of Schooling : 13

GNI Per Capita : 65000

### Output

```
Very High Human Development
```

---

# 📈 Future Enhancements

- Confidence Score
- Interactive Charts
- Country Comparison Dashboard
- Data Visualization
- Cloud Deployment
- API Integration

---

# 👩‍💻 Developer

**Rabiya Tahseen**

B.Tech Computer Science Engineering

Machine Learning Project

---

# 🙏 Acknowledgements

- United Nations Development Programme (UNDP)
- Human Development Report Dataset
- Scikit-learn
- Flask
- Python Community

---

# 📜 License

This project is developed for **educational and academic purposes only**.