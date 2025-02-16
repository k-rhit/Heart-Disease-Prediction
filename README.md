# Heart-Disease-Prediction
Heart Disease Prediction Using Logistic Regression and Flask API

Problem Statement: Heart Disease Prediction
Heart disease is one of the leading causes of mortality worldwide. Early detection of heart disease can significantly improve treatment outcomes and reduce the risk of fatal complications. The objective of this project is to build a predictive model using Logistic Regression to classify whether a person is at risk of heart disease based on their medical and demographic attributes.

Dataset Overview: The dataset consists of various medical parameters and symptoms related to cardiovascular health.
The features include:
  1. Demographic Features:
     1.1 age: Age of the individual
     1.2 sex: Gender (0 = Female, 1 = Male)
  2. Clinical & Test Features:
     2.01 cp: Chest pain type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)
     2.02 trestbps: Resting blood pressure (in mm Hg)
     2.03 chol: Serum cholesterol level (in mg/dl)
     2.04 fbs: Fasting blood sugar (> 120 mg/dl, 1 = True, 0 = False)
     2.05 restecg: Resting electrocardiographic results (0 = Normal, 1 = ST-T Wave abnormality, 2 = Left Ventricular Hypertrophy)
     2.06 thalach: Maximum heart rate achieved
     2.07 exang: Exercise-induced angina (0 = No, 1 = Yes)
     2.08 oldpeak: ST depression induced by exercise relative to rest
     2.09 slope: Slope of the peak exercise ST segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)
     2.10 ca: Number of major vessels colored by fluoroscopy (0–4)
     2.11 thal: Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)
  3. Target Variable:
     3.1 target: Presence of heart disease (1 = Disease, 0 = No Disease)

Objectives:
1. Perform Exploratory Data Analysis (EDA) to understand the data distribution.
2. Conduct feature selection using assumption testing and correlation analysis.
3. Apply outlier handling using Z-score and standardization.
4. Train a Logistic Regression model to classify heart disease risk.
5. Evaluate the model using metrics like Confusion Matrix, Classification Report, ROC-AUC, F1 Score, and Log Loss.
6. Deploy the model as a Flask API with an interactive HTML interface to accept user inputs and display the prediction report.
