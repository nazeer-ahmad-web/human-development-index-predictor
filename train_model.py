import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/HDR.csv")

print("=" * 50)
print("DATA CLEANING")
print("=" * 50)

# Keep only required columns
df = df[
    [
        "Country",
        "Human Development Index (HDI) ",
        "Life expectancy at birth YEARS",
        "Expected years of schooling YEARS",
        "Mean years of schooling YEARS",
        "Gross national income (GNI) per capita USD"
    ]
]

print("\nSelected Columns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nSample GNI Values:")
print(df["Gross national income (GNI) per capita USD"].head(10))

# Convert GNI column to numeric
df["Gross national income (GNI) per capita USD"] = (
    df["Gross national income (GNI) per capita USD"]
    .str.replace(",", "", regex=False)
    .astype(float)
)

print("\nData Types After Conversion:")
print(df.dtypes)

# Create HDI Category
def categorize_hdi(hdi):
    if hdi >= 0.800:
        return "Very High"
    elif hdi >= 0.700:
        return "High"
    elif hdi >= 0.550:
        return "Medium"
    else:
        return "Low"

# Apply the function
df["HDI_Category"] = df["Human Development Index (HDI) "].apply(categorize_hdi)

print("\nHDI Categories Created Successfully!")

print(df[["Country", "Human Development Index (HDI) ", "HDI_Category"]].head(10))

# ==============================
# Prepare Features and Target
# ==============================

X = df[
    [
        "Life expectancy at birth YEARS",
        "Expected years of schooling YEARS",
        "Mean years of schooling YEARS",
        "Gross national income (GNI) per capita USD"
    ]
]

y = df["HDI_Category"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# ==============================
# Train-Test Split
# ==============================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

# ==============================
# Train Random Forest Model
# ==============================

from sklearn.ensemble import RandomForestClassifier

# Create the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

print("\n Random Forest Model Trained Successfully!")

# ==============================
# Model Evaluation
# ==============================

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Make predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==============================
# Save the Trained Model
# ==============================

import joblib

# Save the model
joblib.dump(model, "model/model.pkl")

print("\n Model saved successfully as model/model.pkl")