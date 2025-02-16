from flask import Flask, render_template, jsonify, request, redirect, url_for
from utils import HeartDisease

app = Flask(__name__)

feature_labels = {
    "age": "Age",
    "sex": "Sex",
    "cp": "Chest Pain Type",
    "trestbps": "Resting Blood Pressure",
    "chol": "Cholesterol Level",
    "fbs": "Fasting Blood Sugar",
    "restecg": "Resting ECG Results",
    "thalach": "Maximum Heart Rate Achieved",
    "exang": "Exercise Induced Angina",
    "oldpeak": "ST Depression Induced by Exercise",
    "slope": "Slope of the Peak Exercise ST Segment",
    "ca": "Number of Major Vessels Colored by Fluoroscopy",
    "thal": "Thalassemia Type"
}

value_labels = {
    "sex": {"0": "Female", "1": "Male"},
    "fbs": {"0": "No", "1": "Yes"},
    "exang": {"0": "No", "1": "Yes"},
    "slope": {"0": "Upsloping", "1": "Flat", "2": "Downsloping"},
    "thal": {"1": "Normal", "2": "Fixed Defect", "3": "Reversible Defect"},
    "cp": {"0": "Typical Angina", "1": "Atypical Angina", "2": "Non-anginal Pain", "3": "Asymptomatic"},
    "restecg": {"0": "Normal", "1": "ST-T Wave Abnormality", "2": "Left Ventricular Hypertrophy"}
}

@app.route('/')
def index():
    return render_template('heart_index.html')

@app.route('/heart_disease', methods=['POST'])
def predict_heart_disease():
     try:
        data = request.form
        print("Data: ",data)
        age = eval(data['age'])
        sex = eval(data['sex'])
        cp = eval(data['cp'])
        trestbps = eval(data['trestbps'])
        chol = eval(data['chol'])
        fbs = eval(data['fbs'])
        restecg = eval(data['restecg'])
        thalach = eval(data['thalach'])
        exang = eval(data['exang'])
        oldpeak = eval(data['oldpeak'])
        slope = eval(data['slope'])
        ca = eval(data['ca'])
        thal = eval(data['thal'])
    
        predict_disease = HeartDisease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        predict = predict_disease.prediction()
        if predict == 1: disease = 'Positive'
        else: disease = 'Negative'

        input_dict = {}
        for key, value in request.form.items():
            read_key = feature_labels.get(key, key)
            read_value = value_labels[key].get(value, value) if key in value_labels else value
            input_dict[read_key] = read_value

        return redirect(url_for('report', prediction=disease, **input_dict))
     
     except Exception as e:
        return render_template("heart_index.html", prediction_text=f'Error: {str(e)}')

@app.route('/report')
def report():
    input_data = {key: request.args.get(key) for key in request.args if key != 'prediction'}
    prediction_text = request.args.get('prediction', 'Error in prediction')
    return render_template("heart_report.html", input_data=input_data, prediction_text=f'{prediction_text}')

app.run(debug = True)