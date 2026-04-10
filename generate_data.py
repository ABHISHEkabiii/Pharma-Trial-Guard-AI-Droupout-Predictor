import pandas as pd
import numpy as np

np.random.seed(42)

n = 400

data = pd.DataFrame({
    "patient_id": range(1, n+1),
    "age": np.random.randint(18, 80, n),
    "distance_to_site": np.random.randint(1, 100, n),
    "adverse_events": np.random.randint(0, 5, n),
    "visit_adherence": np.random.uniform(0.5, 1.0, n),
    "comorbidity_score": np.random.randint(0, 5, n)
})

# Dropout logic
data["dropout"] = (
    (data["adverse_events"] > 2) |
    (data["visit_adherence"] < 0.7) |
    (data["distance_to_site"] > 70)
).astype(int)

data.to_csv("clinical_data.csv", index=False)

print("Synthetic data generated.")