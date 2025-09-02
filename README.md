# Instagram Fake vs. Genuine Account Detector – Starter Kit

This starter kit guides you through a complete, end‑to‑end project: EDA, a baseline ML model, optional SQL analysis, and ideas for a Tableau dashboard.

## 0) Prerequisites
- Python 3.9+ installed
- (Optional) JupyterLab/Notebook if you prefer notebooks
- (Optional) Tableau Public / Power BI for dashboards

## 1) Set up the environment
```bash
cd instagram_fake_genuine_project
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

## 2) Get the dataset
From the PDF you uploaded, download **train.csv** and **test.csv** (same schema) and place them into:
```
instagram_fake_genuine_project/data/
```
Expected files:
```
data/train.csv
data/test.csv
```

## 3) Run the baseline script
```bash
python src/train_model.py
```
This will:
- Load the data from `data/train.csv` and `data/test.csv`
- Train a RandomForestClassifier
- Print metrics (accuracy/precision/recall/F1)
- Show a confusion matrix and a feature-importance bar chart

## 4) Use the notebook (optional)
Open the notebook and run cells top to bottom:
```
notebooks/Instagram_Fake_vs_Genuine.ipynb
```

## 5) SQL analysis (optional)
- Schema + EDA queries are in `sql/instagram_accounts.sql` and `sql/eda_queries.sql`.
- You can import the CSVs to your DB (e.g., PostgreSQL) and run the queries for analyst-style insights.

## 6) Dashboards (optional)
See `dashboards/tableau_guide.md` for suggested charts to build in Tableau/Power BI.

## 7) Next steps / enhancements
- Add hyperparameter tuning (GridSearchCV/RandomizedSearchCV)
- Try GradientBoosting/XGBoost/LightGBM
- Calibrate thresholds to trade off precision/recall
- Add k-fold cross-validation and learning curves
- Log experiments (MLflow) and export a pickle model

---

Last generated: 2025-09-02
