from model import build_model
import pandas as pd

df = pd.read_csv("dataset/wifi_data.csv")

X = df.drop("issue", axis=1)
y = df["issue"]

model = build_model()
model.fit(X, y)

import joblib
joblib.dump(model, "wifi_model.pkl")