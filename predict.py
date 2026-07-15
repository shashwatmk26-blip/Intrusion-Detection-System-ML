import pandas as pd
import joblib

from preprocess import preprocess

df = pd.read_csv("dataset/KDDTrain+.txt", header=None)

df = preprocess(df)

model = joblib.load("model/ids_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

sample = df.drop("label", axis=1).iloc[[0]]

prediction = model.predict(sample)

print("Prediction :", label_encoder.inverse_transform(prediction)[0])

prob = model.predict_proba(sample)

print("Confidence :", max(prob[0]) * 100)