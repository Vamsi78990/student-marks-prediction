
import pandas as pd
import os


# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "student_data.csv"
)


# Input features
FEATURE_COLUMNS = [
    "StudyHours",
    "Attendance",
    "PreviousMarks",
    "SleepHours",
    "SocialMediaHours"
]

# Target column
TARGET_COLUMN = "FinalMarks"


def load_dataset():
    """Load student dataset."""

    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully!")

    return df


def preprocess_data(df):
    """Clean dataset and separate features and target."""

    # Check required columns
    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Select required columns
    df = df[required_columns].copy()

    # Handle missing values
    df = df.dropna()

    # Separate input features
    X = df[FEATURE_COLUMNS]

    # Separate target
    y = df[TARGET_COLUMN]

    print("Preprocessing completed!")

    print("Features Shape:", X.shape)

    print("Target Shape:", y.shape)

    return X, y


if __name__ == "__main__":

    df = load_dataset()

    X, y = preprocess_data(df)

    print("\nInput Features:")
    print(X.head())

    print("\nTarget Values:")
    print(y.head())

