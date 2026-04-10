import os, textwrap
base = r'c:\Users\tirup\Downloads\gsk-trialguard'
structure = {
    'data': {
        'patients.csv': 'patient_id,age,gender,smoker,comorbidity\n1,65,M,1,0\n',
        'predictions.csv': 'patient_id,risk_score,tier\n1,0.72,high\n',
        'shap_values.csv': 'patient_id,feature,shap_value\n1,age,0.12\n',
        'feature_importance.csv': 'feature,importance\nage,0.45\n'
    },
    'model': {
        'train_model.py': textwrap.dedent('''
            import pandas as pd
            from xgboost import XGBClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import roc_auc_score
            import joblib

            df = pd.read_csv('../data/patients.csv')
            X = df[['age']]
            y = (df['age'] > 60).astype(int)
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
            model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
            model.fit(X_train, y_train)
            preds = model.predict_proba(X_test)[:, 1]
            print('AUC:', roc_auc_score(y_test, preds))
            joblib.dump(model, 'xgboost_model.pkl')
            joblib.dump({'features': list(X.columns)}, 'metadata.pkl')
        '''),
        'predict.py': textwrap.dedent('''
            import pandas as pd
            import joblib

            model = joblib.load('xgboost_model.pkl')
            data = pd.read_csv('../data/patients.csv')
            X = data[['age']]
            data['risk_score'] = model.predict_proba(X)[:, 1]
            data['tier'] = pd.cut(data['risk_score'], bins=[-1, 0.33, 0.66, 1], labels=['low','medium','high'])
            data.to_csv('../data/predictions.csv', index=False)
            print('predictions saved to data/predictions.csv')
        '''),
        'shap_export.py': textwrap.dedent('''
            import pandas as pd
            import shap, joblib
            import matplotlib.pyplot as plt

            model = joblib.load('xgboost_model.pkl')
            data = pd.read_csv('../data/patients.csv')
            X = data[['age']]
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X)
            shap_df = pd.DataFrame(shap_values, columns=X.columns)
            shap_df.to_csv('../data/shap_values.csv', index=False)
            shap.summary_plot(shap_values, X, show=False)
            plt.savefig('../dashboard/shap_beeswarm.png')
            shap.summary_plot(shap_values, X, plot_type='bar', show=False)
            plt.savefig('../dashboard/shap_importance.png')
        ''')
    },
    'dashboard': {
        'index.html': '<!DOCTYPE html><html><body><h1>TrialGuard Dashboard</h1></body></html>',
        'shap_beeswarm.png': '',
        'shap_importance.png': ''
    },
    'generate_data.py': textwrap.dedent('''
        import pandas as pd
        df = pd.DataFrame({'patient_id':[1,2,3],'age':[65,45,72],'gender':['M','F','M'],'smoker':[1,0,1],'comorbidity':[0,1,1]})
        df.to_csv('data/patients.csv', index=False)
        print('data/patients.csv generated')
    '''),
    'requirements.txt': 'pandas\nxgboost\nscikit-learn\njoblib\nshap\nmatplotlib\n',
    'README.md': '# gsk-trialguard\n\nSynthetic trial patient risk scoring demo.'
}

for folder, files in structure.items():
    if folder in ['generate_data.py', 'requirements.txt', 'README.md']:
        path = os.path.join(base, folder)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(files)
        continue
    dirpath = os.path.join(base, folder)
    os.makedirs(dirpath, exist_ok=True)
    for name, content in files.items():
        path = os.path.join(dirpath, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
print('scaffold created')
