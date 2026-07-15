import pandas as pd
import joblib

from preprocess import preprocess

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("dataset/KDDTrain+.txt", header=None)

df = preprocess(df)

label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["label"])

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred, zero_division=0))

joblib.dump(model, "model/ids_model.pkl")
joblib.dump(label_encoder, "model/label_encoder.pkl")

print("Model Saved Successfully!")