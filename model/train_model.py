import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle

data = pd.read_csv("clinical_data.csv")

X = data.drop(["dropout", "patient_id"], axis=1)
y = data["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved.")