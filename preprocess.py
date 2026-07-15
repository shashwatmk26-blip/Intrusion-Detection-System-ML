import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    # Remove difficulty column
    df = df.iloc[:, :-1]

    # Rename label column
    df.rename(columns={41: "label"}, inplace=True)

    encoder = LabelEncoder()

    # Encode categorical columns
    for col in df.select_dtypes(include=["object"]).columns:
        if col != "label":
            df[col] = encoder.fit_transform(df[col])

    return df