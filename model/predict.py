import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

data = pd.read_csv("clinical_data.csv")

X = data.drop(["dropout", "patient_id"], axis=1)

data["prediction"] = model.predict_proba(X)[:,1]

data.to_csv("predictions.csv", index=False)

print("Predictions saved.")