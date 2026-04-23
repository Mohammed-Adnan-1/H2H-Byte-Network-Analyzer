from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

def train_anomaly_model(data):
    model.fit(data)

def detect_anomaly(data_point):
    prediction = model.predict([data_point])
    return "Anomaly" if prediction[0] == -1 else "Normal"