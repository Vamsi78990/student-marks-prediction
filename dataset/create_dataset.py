
import pandas as pd
import numpy as np
import os

# 1. Generate random data
np.random.seed(42)

n = 100

data = {
    "StudyHours": np.random.uniform(1, 10, n),
    "Attendance": np.random.uniform(50, 100, n),
    "PreviousMarks": np.random.uniform(35, 95, n),
    "SleepHours": np.random.uniform(4, 9, n),
    "SocialMediaHours": np.random.uniform(0, 6, n)
}

# 2. Convert data into DataFrame
df = pd.DataFrame(data)

# 3. Calculate Final Marks
df["FinalMarks"] = (
    8 * df["StudyHours"]
    + 0.22 * df["Attendance"]
    + 0.30 * df["PreviousMarks"]
    + 1.2 * df["SleepHours"]
    - 2 * df["SocialMediaHours"]
    + np.random.normal(0, 4, n)
)

# 4. Keep marks between 0 and 100
df["FinalMarks"] = df["FinalMarks"].clip(0, 100)

# 5. Connect Python code to CSV file path
folder_path = os.path.dirname(__file__)

file_path = os.path.join(folder_path, "student_data.csv")

# 6. Save DataFrame into CSV file
df.to_csv(file_path, index=False)

# 7. Display output
print("CSV file created successfully!")
print("File path:", file_path)
print(df.head())