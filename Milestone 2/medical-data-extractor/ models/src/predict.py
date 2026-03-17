import joblib
import numpy as np

model = joblib.load("models/health_model.pkl")

def predict_condition(input_data):
    """
    input_data = [hemoglobin, glucose, cholesterol, platelets]
    """
    data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(data)[0]
    return prediction
