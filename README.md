# Heart-Disease-Prediction
Heart Disease Prediction Using Logistic Regression and Flask API

Problem Statement: Heart Disease Prediction
Heart disease is one of the leading causes of mortality worldwide. Early detection of heart disease can significantly improve treatment outcomes and reduce the risk of fatal complications. The objective of this project is to build a predictive model using Logistic Regression to classify whether a person is at risk of heart disease based on their medical and demographic attributes.

Dataset Overview:
The dataset consists of various medical parameters and symptoms related to cardiovascular health. The features include:

Demographic Features:
age: Age of the individual
sex: Gender (0 = Female, 1 = Male)

Clinical & Test Features:
cp: Chest pain type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)
trestbps: Resting blood pressure (in mm Hg)
chol: Serum cholesterol level (in mg/dl)
fbs: Fasting blood sugar (> 120 mg/dl, 1 = True, 0 = False)
restecg: Resting electrocardiographic results (0 = Normal, 1 = ST-T Wave abnormality, 2 = Left Ventricular Hypertrophy)
thalach: Maximum heart rate achieved
exang: Exercise-induced angina (0 = No, 1 = Yes)
oldpeak: ST depression induced by exercise relative to rest
slope: Slope of the peak exercise ST segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)
ca: Number of major vessels colored by fluoroscopy (0–4)
thal: Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)
Target Variable:
target: Presence of heart disease (1 = Disease, 0 = No Disease)

Objective:
Perform Exploratory Data Analysis (EDA) to understand the data distribution.
Conduct feature selection using assumption testing and correlation analysis.
Apply outlier handling using Z-score and standardization.
Train a Logistic Regression model to classify heart disease risk.
Evaluate the model using metrics like Confusion Matrix, Classification Report, ROC-AUC, F1 Score, and Log Loss.
Deploy the model as a Flask API with an interactive HTML interface to accept user inputs and display the prediction report.
