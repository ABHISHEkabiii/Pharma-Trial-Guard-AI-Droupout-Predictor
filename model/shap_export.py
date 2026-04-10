import shap
import pandas as pd
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load model and data from project root (run from pharma-trialguard/)
model = pickle.load(open("model.pkl", "rb"))
data = pd.read_csv("clinical_data.csv")

X = data.drop(["dropout", "patient_id"], axis=1)

# Generate SHAP values
explainer = shap.Explainer(model)
shap_values = explainer(X)

# Save SHAP values CSV
shap_df = pd.DataFrame(shap_values.values, columns=X.columns)
shap_df.to_csv("shap_values.csv", index=False)

# Save beeswarm plot
shap.summary_plot(shap_values, X, show=False)
plt.tight_layout()
plt.savefig("dashboard/shap_beeswarm.png", dpi=150, bbox_inches='tight')
plt.clf()

# Save feature importance bar plot
shap.summary_plot(shap_values, X, plot_type='bar', show=False)
plt.tight_layout()
plt.savefig("dashboard/shap_importance.png", dpi=150, bbox_inches='tight')
plt.clf()

print("SHAP values exported.")