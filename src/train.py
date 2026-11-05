
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "student_data.csv"
)

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "students_model.pkl"
)


# Create models folder if it does not exist
os.makedirs(MODEL_DIR, exist_ok=True)


# Load dataset
print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)


# Input features
X = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousMarks",
        "SleepHours",
        "SocialMediaHours"
    ]
]


# Target variable
y = df["FinalMarks"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Machine Learning Pipeline
model = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression())
    ]
)


# Train model
print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# Predictions
y_pred = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


print("\n----- MODEL EVALUATION -----")

print("MAE:", round(mae, 2))

print("MSE:", round(mse, 2))

print("RMSE:", round(rmse, 2))

print("R2 Score:", round(r2, 2))


# Save trained model
joblib.dump(model, MODEL_PATH)


print("\nModel saved successfully!")

print("Model Location:", MODEL_PATH)

print("Model File Size:", os.path.getsize(MODEL_PATH), "bytes")

