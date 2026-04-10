# PHARMA-trialguard

Synthetic patient risk scoring & SHAP explainability proof-of-concept.

## Structure

- data/: source and output CSVs
- model/: training, scoring, explainability scripts
- dashboard/: static HTML + SHAP visuals

## Quickstart

1. pip install -r requirements.txt
2. python generate_data.py
3. python model/train_model.py
4. python model/predict.py
5. python model/shap_export.py
6. open dashboard/index.html
