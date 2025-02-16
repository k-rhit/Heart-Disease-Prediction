import pickle
import numpy as np
import pandas as pd

class HeartDisease():
    def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal	

    def load_model(self):
        with open("log_reg_heart.pkl", "rb") as f:
            self.model = pickle.load(f)
        with open("std_scaler_heart.pkl","rb") as f:
            self.scaler = pickle.load(f)

    def prediction(self):

        self.load_model()

        test_array = np.array([[self.age, self.sex, self.cp, self.trestbps, self.chol,
                                self.fbs, self.restecg, self.thalach, self.exang, self.oldpeak, 
                                self.slope, self.ca, self.thal]])
        
        print("Test Array: ", test_array)

        std_test_array = self.scaler.transform(test_array)

        disease_prediction = self.model.predict(std_test_array)

        return disease_prediction