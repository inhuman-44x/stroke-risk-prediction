### Stroke Risk Prediction
A machine learning project for predicting stroke risk using patient demographic and clinical data.

This project demonstrates an end-to-end workflow including exploratory data analysis, preprocessing, model training, evaluation, and risk stratification. The goal is to build a predictive model that can estimate the probability of stroke and categorize patients into clinically meaningful risk tiers.

### Project Overview
Stroke is a major global health problem and early identification of high-risk individuals is important for prevention and clinical decision-making. Machine learning models can help identify patterns in patient data that may indicate elevated stroke risk.

This project builds a predictive logistic regression model using healthcare data containing demographic and clinical features such as age, average glucose level, hypertension, heart disease, BMI, and smoking status.

The workflow includes:

Exploratory Data Analysis (EDA)

Data preprocessing and feature engineering

Training a logistic regression model

Model evaluation using multiple metrics

Calibration analysis

Threshold optimization

Risk tier classification (Low, Moderate, High)

### Live Demo
A web application for stroke risk prediction is available at:
👉 [Stroke Risk Predictor](https://inhuman44-stroke-risk-app.hf.space/)

Enter a patient's demographic and clinical details to receive a predicted stroke risk probability and risk tier classification (Low, Moderate, or High).

### Dataset
The project uses the Stroke Prediction Dataset originally available on Kaggle (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).

### Evaluation Metrics
Because stroke datasets are highly imbalanced, model performance is evaluated using:

- ROC-AUC

- Precision-Recall AUC

- Calibration analysis

### Threshold Optimization
Instead of using the default 0.5 threshold, the model probabilities are converted into risk categories using optimized cutoffs that better capture the clinical cost of missing a true stroke case. Thresholds are selected by analyzing the Precision-Recall curve:

- The moderate risk cutoff is set at the probability threshold that achieves ≥80% recall, ensuring the majority of true stroke cases are flagged, even at the cost of some additional false positives.
- The high risk cutoff is set at the threshold where precision reaches ≥30%, identifying the subset of patients where the model's positive predictions are most reliable.

This approach prioritizes sensitivity in a domain where false negatives (missed strokes) carry greater clinical consequence than false positives.

### Risk Tier Classification
Predicted probabilities are mapped to three clinically meaningful risk tiers based on the optimized thresholds above:

| Risk Tier | Probability Range | Monitoring | Lifestyle Guidance | Clinical Action |
|-----------|------------------|------------|-------------------|-----------------|
| 🟢 **Low** | Below moderate cutoff | Routine annual review | Maintain healthy diet, exercise, and avoid smoking | No immediate intervention required |
| 🟡 **Moderate** | Moderate to high cutoff | Follow-up every 3–6 months | Address modifiable risk factors (weight, glucose, smoking) | Consider referral for risk factor management |
| 🔴 **High** | Above high cutoff | Frequent monitoring | Urgent lifestyle modification advised | Prompt clinical referral recommended |

### Results

The model was evaluated using 5-fold cross-validation on the training set and final held-out test set performance.

**Cross-Validation (Training Set)**

| Metric | Score | Std Dev |
|--------|-------|---------|
| ROC-AUC | 0.853 | ± 0.027 |
| PR-AUC | 0.230 | ± 0.045 |
| Brier Score | 0.042 | ± 0.001 |

**Hold-Out Test Set**

| Metric | Score |
|--------|-------|
| ROC-AUC | 0.837 |
| PR-AUC | 0.219 |
| Brier Score | 0.042 |

The close alignment between cross-validation and test set scores indicates the model generalises well without significant overfitting. The low Brier Score (0.042) reflects well-calibrated probability estimates, which is important for meaningful risk tier assignment. The relatively modest PR-AUC (0.219) is expected given the significant class imbalance in stroke datasets, and underscores why threshold optimisation was applied rather than relying on default classification cutoffs.

### Limitations

- **Cross-sectional data:** The dataset reflects a single snapshot of patient demographic and clinical information. The absence of longitudinal or time-to-event data means the model cannot capture how risk evolves over time or estimate when a stroke is likely to occur.

- **Class imbalance:** Stroke is a relatively rare event in the dataset, which limits the model's ability to learn robust patterns for the positive class. Threshold optimisation and imbalance-aware evaluation metrics were applied to mitigate this, but predictive performance on stroke cases remains constrained.

- **Generalisation:** The model was trained on a single dataset of unknown provenance and may not generalise to patient populations with different demographic profiles, healthcare settings, or data collection practices.

- **Feature scope:** The model relies on a limited set of demographic and clinical features. Potentially important predictors such as medication history, family history, imaging data, or biomarkers are not included.

> ⚠️ **Disclaimer:** Risk tiers are intended to support clinical decision-making, not replace it. This project is intended for educational and research purposes only. The model should not be used to guide clinical decisions without further validation on prospective, representative patient data.

### Future Work

The current model serves as a proof-of-concept for stroke risk stratification using static clinical data. The long-term vision for this project is to develop a lightweight, deployable model capable of real-time stroke risk prediction embedded in wearable devices.

**Planned directions include:**

- **Longitudinal data integration:** Incorporating time-series biodata (e.g. heart rate variability, blood pressure trends, activity levels) to capture how risk evolves over time and move beyond the limitations of cross-sectional snapshots.

- **Prospective clinical validation:** Validating the model on prospective, real-world patient cohorts across diverse demographics and healthcare settings to ensure generalisation before any clinical use.

- **Wearable deployment:** Optimising the model for edge deployment on low-power wearable hardware, enabling continuous, on-device inference without reliance on cloud connectivity.

- **Real-time early warning system:** Developing an alert mechanism that detects meaningful deviations in a patient's everyday biodata and surfaces timely warning signals to both the patient and their healthcare provider.

- **Patient-specific baseline modelling:** Building personalised risk profiles so that alerts are triggered relative to an individual's normal patterns rather than population-level thresholds, reducing false alarm fatigue.
