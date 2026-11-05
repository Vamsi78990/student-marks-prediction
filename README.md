🎓 Student Marks Prediction Dashboard
📌 Project Overview
The Student Marks Prediction Dashboard is a Machine Learning project designed to predict students' final marks based on their academic and lifestyle factors.

This project uses Linear Regression to predict student performance and Streamlit to build an interactive web dashboard.

🎯 Objectives
Predict students' final marks using Machine Learning.
Analyze the relationship between study hours and academic performance.
Understand the impact of attendance and previous marks.
Develop an interactive dashboard for student performance prediction.
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Joblib
📊 Dataset Description
The dataset contains 100 student records.

Feature	Description
StudyHours	Daily study hours
Attendance	Attendance percentage
PreviousMarks	Previous academic marks
SleepHours	Daily sleep hours
SocialMediaHours	Daily social media usage
FinalMarks	Student's final marks
🤖 Machine Learning Algorithm
Linear Regression

Linear Regression is used to predict continuous numerical values based on input features.

Model Evaluation
Metric	Score
MAE	3.92
MSE	26.14
RMSE	5.11
R² Score	0.95
The model achieved an R² score of 0.95 on the test dataset.

Note: These results are based on a synthetic dataset. Performance on real student data may differ.

📁 Project Structure
studentmarks/
│
├── dataset/
│   ├── create_dataset.py
│   └── student_data.csv
│
├── models/
│   └── students_model.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── app.py
│
├── requirements.txt
│
└── README.md
⚙️ Installation
Step 1: Clone the Repository
git clone https://github.com/your-username/student-marks-prediction-dashboard.git
Step 2: Navigate to Project Directory
cd student-marks-prediction-dashboard
Step 3: Create Virtual Environment
python -m venv .venv
Step 4: Activate Virtual Environment
Windows:

.venv\Scripts\activate
Step 5: Install Dependencies
python -m pip install -r requirements.txt
🚀 Running the Project
Step 1: Train the Machine Learning Model
python src/train.py
Step 2: Launch the Streamlit Dashboard
python -m streamlit run src/app.py
Step 3: Open in Browser
http://localhost:8501
💻 Dashboard Features
Interactive student input fields
Study hours input
Attendance percentage input
Previous marks input
Sleep hours input
Social media usage input
Final marks prediction
Real-time prediction display
🔮 Future Enhancements
Student performance visualization
Pass/Fail prediction
Student risk analysis
Advanced Machine Learning algorithms
Database integration
Online dashboard deployment
👨‍💻 Author
B.Tech Computer Science and Engineering – Data Science

📜 License
This project is developed for educational and academic purposes.

