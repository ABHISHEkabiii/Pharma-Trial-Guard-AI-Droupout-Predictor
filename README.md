<div align="center">

<!-- ✅ ANIMATED BANNER — capsule-render (live waves + twinkling) -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=PharmaTrialGuard&fontSize=52&fontColor=FFFFFF&fontAlignY=40&desc=AI-Powered%20Clinical%20Trial%20Dropout%20Prediction%20%26%20Explainability&descAlignY=62&descSize=15&descColor=00b4d8&animation=twinkling" width="100%"/>

<br/>

<!-- ✅ ANIMATED TYPING SVG — demolab (live typewriter effect) -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=00B4D8&background=00000000&center=true&vCenter=true&multiline=false&width=750&height=45&lines=Predicting+Patient+Dropout+Before+It+Happens...;XGBoost+%2B+SHAP+Explainability+Engine;Transparent+AI+for+Clinical+Research;Built+for+Pharma+%7C+Designed+for+Trust" alt="Typing SVG"/>

<br/><br/>

<!-- ✅ BADGES ROW 1 -->
<img src="https://img.shields.io/badge/Python-3.10+-00b4d8?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-Classifier-ff6b35?style=for-the-badge&logo=buffer&logoColor=white"/>
<img src="https://img.shields.io/badge/SHAP-Explainability-00d4a8?style=for-the-badge&logo=leaflet&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-ML-f7931e?style=for-the-badge&logo=scikit-learn&logoColor=white"/>

<br/>

<!-- ✅ BADGES ROW 2 -->
<img src="https://img.shields.io/badge/Status-Active-00d4a8?style=flat-square&logo=statuspage&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-00b4d8?style=flat-square"/>
<img src="https://img.shields.io/badge/Clinical%20AI-Pharma-ff3b3b?style=flat-square"/>
<img src="https://img.shields.io/badge/Dashboard-Interactive-ffb703?style=flat-square&logo=chartdotjs&logoColor=black"/>
<img src="https://img.shields.io/badge/Patients-400%20Synthetic-6c5ce7?style=flat-square"/>

<br/><br/>

<!-- ✅ ANIMATED SNAKE / CONTRIBUTION GRAPH VISUAL -->
<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%"/>

</div>

---

## 🧬 What is PharmaTrialGuard?

> **PharmaTrialGuard** is an end-to-end machine learning system that predicts patient dropout risk in clinical trials — before it costs the study millions of dollars and months of delay.

Clinical trial failures cost the pharmaceutical industry **$600B+ annually**, with patient dropout being a leading cause. TrialGuard uses a trained **XGBoost classifier** combined with **SHAP explainability** to not just flag at-risk patients, but *explain why* — giving trial managers actionable, transparent insight through a real-time interactive dashboard.

---

## 🎯 Problem → Solution

```
❌ BEFORE TrialGuard                         ✅ AFTER TrialGuard
─────────────────────────────────────        ──────────────────────────────────────
Dropout detected AFTER it happens      →     Risk scored BEFORE dropout occurs
No insight into WHY patients drop out  →     SHAP explains every prediction
Manual, reactive monitoring            →     Automated, proactive risk pipeline
Black-box model decisions              →     Full per-patient explainability
Static spreadsheets                    →     Live interactive clinical dashboard
```

---

## 📸 Dashboard Preview

<div align="center">

> ⚡ **Interactive dashboard running at `dashboard/index.html`**

**Dashboard Overview**
<img src="./assets/dashboard-overview.png" width="100%" alt="Dashboard Overview"/>

<br/>

**Patient Risk Table**
<img src="./assets/risk-table.png" width="100%" alt="Patient Risk Table"/>

<br/>

**SHAP Beeswarm Plot**
<img src="./assets/shap-beeswarm.png" width="100%" alt="SHAP Beeswarm Plot"/>

<br/>

**Feature Importance Chart**
<img src="./assets/feature-importance.png" width="100%" alt="Feature Importance Chart"/>

</div>

---

## 🏗️ Architecture

```
pharma-trialguard/
│
├── 📊 clinical_data.csv          ← 400 synthetic patients (age, distance, adherence, AEs)
│
├── 🐍 generate_data.py           ← Synthetic data generator with realistic dropout logic
│
├── model/
│   ├── 🧠 train_model.py         ← XGBoost classifier training + model serialisation
│   ├── 🔮 predict.py             ← Batch dropout probability scoring
│   ├── 🔍 shap_export.py         ← SHAP TreeExplainer → beeswarm + bar charts
│   └── 📦 xgboost_model.pkl      ← Serialised trained model
│
├── data/
│   ├── feature_importance.csv    ← Top feature weights
│   ├── predictions.csv           ← Scored patient output
│   └── shap_values.csv           ← Per-patient SHAP decomposition
│
└── dashboard/
    ├── 🖥️  index.html             ← Full interactive clinical dashboard (Chart.js)
    ├── shap_beeswarm.png         ← SHAP summary beeswarm plot
    └── shap_importance.png       ← Global feature importance bar chart
```

---

## ⚙️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
|  **ML Model** | XGBoost | Gradient-boosted dropout classifier |
|  **Explainability** | SHAP TreeExplainer | Per-patient prediction decomposition |
|  **Feature Engineering** | scikit-learn | Train/test split, preprocessing |
|  **Data** | pandas + NumPy | Synthetic patient data generation |
|  **Dashboard** | Chart.js + PapaParse | Real-time interactive risk visualisation |
|  **Serialisation** | joblib + pickle | Model persistence |
|  **UI Design** | Vanilla HTML/CSS/JS | Zero-dependency, deployable anywhere |

</div>

---

## 🔬 Features in Detail

### 🧠 Machine Learning Pipeline

- **XGBoost Classifier** trained on 5 clinical features: `age`, `distance_to_site`, `adverse_events`, `visit_adherence`, `comorbidity_score`
- **Dropout logic**: patients flagged if `adverse_events > 2` OR `visit_adherence < 0.7` OR `distance_to_site > 70`
- 80/20 train-test split with `predict_proba` for continuous risk scoring (0–100%)
- Model serialised and reloadable for production inference

### 🔍 SHAP Explainability

- **SHAP TreeExplainer** generates per-patient feature contribution scores
- **Beeswarm plot** → shows feature impact distribution across all patients
- **Bar chart** → global feature importance ranking
- Every prediction is *decomposable*: know exactly which feature drove each patient's risk score

### 🖥️ Interactive Dashboard

- **Patient risk table** with colour-coded risk tiers (High 🔴 / Medium 🟡 / Low 🟢)
- **Live XGBoost inference** — run the model directly in the browser
- **SHAP visualisations** embedded and zoomable
- **Sidebar filters** by risk threshold and patient segment
- Fully dark-mode, responsive clinical UI built with `Bebas Neue` + `DM Mono` typography

---

## 🚀 Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/your-username/pharma-trialguard.git
cd pharma-trialguard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate synthetic patient data
python generate_data.py

# 4. Train the XGBoost model
python model/train_model.py

# 5. Score all patients
python model/predict.py

# 6. Export SHAP explainability plots
python model/shap_export.py

# 7. Open the dashboard
open dashboard/index.html
```

---

## 📦 Requirements

```txt
pandas
xgboost
scikit-learn
joblib
shap
matplotlib
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📊 Model Features

| Feature | Type | Clinical Meaning |
|---------|------|-----------------|
| `age` | Integer (18–80) | Patient age — older patients may have higher dropout |
| `distance_to_site` | Integer (1–100 km) | Travel burden → key dropout driver |
| `adverse_events` | Integer (0–4) | Reported adverse events count |
| `visit_adherence` | Float (0.5–1.0) | Ratio of attended vs scheduled visits |
| `comorbidity_score` | Integer (0–4) | Count of comorbid conditions |

**Target variable:** `dropout` (binary: 1 = dropped out, 0 = completed)

---

## 🧩 How Dropout is Defined

```python
data["dropout"] = (
    (data["adverse_events"] > 2)      |   # Too many adverse events
    (data["visit_adherence"] < 0.7)   |   # Poor visit adherence
    (data["distance_to_site"] > 70)       # Too far from trial site
).astype(int)
```

This multi-factor rule captures the three most clinically validated predictors of trial dropout.

---

## 🌐 Real-World Impact

```
💊  Clinical Trial Phase II/III average cost:  $20M–$100M
📉  ~30% of trials fail due to patient dropout
⏱️  Each dropout causes 3–6 months delay on average
🎯  TrialGuard identifies high-risk patients early → enables proactive retention
✅  Explainable AI → compliant with ICH E6 GCP transparency requirements
```

---

## 🛣️ Roadmap

-  🏥 Real EHR integration (FHIR / HL7 API connector)
- (-) 📡 REST API wrapper for trial management systems (Medidata / Veeva)
- [-] 🔄 Longitudinal risk tracking (patient risk over trial timeline)
- [ ] 📱 Mobile alert system for site coordinators
- [ ] 🧬 Extend features: genetic markers, PRO scores, wearable signals
- [ ] 🐳 Docker + cloud deployment (AWS/GCP ready)
- [ ] 🔒 HIPAA-compliant data handling layer

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

<!-- ✅ ANIMATED FOOTER WAVE -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer" width="100%"/>

<p>
  <sub>Built by Abhishek for the future of clinical AI · <strong>PharmaTrialGuard</strong> · Keeping patients in trials, research on track</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Made%20with-Python-00b4d8?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Powered%20by-XGBoost%20%2B%20SHAP-ff6b35?style=flat-square"/>
  <img src="https://img.shields.io/badge/For-Clinical%20AI%20Innovation-00d4a8?style=flat-square"/>
</p>

</div>
