# METRIX AI – SIH26036
Euclidean vs Manhattan K-Medoids grouping of weighing/measuring instrument verification records, validated against inspector labels.

## Run (Windows / VS Code)
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python -m pytest tests        (optional, 18 tests)
    streamlit run app.py
Tested with Python 3.12, Streamlit 1.67, pandas 3.0, scikit-learn 1.9.

## Pages
Home · Data & Features · Compare Metrics · Risk · Validation · Reports · How It Works.
Sidebar: upload CSV, template CSV, reset, choose features and k, run analysis.

## Data honesty
- Default data is SYNTHETIC (data/synthetic); its inspector labels are simulated. Results show the method works, not real-world accuracy.
- Kaggle data was NOT downloaded in the build environment. For real data: create a Kaggle account, put `kaggle.json` in `%USERPROFILE%\.kaggle\`,
  accept competition rules, download, keep the original in `data/raw/kaggle_source_data.csv` unmodified, convert to the 17 columns in the sidebar **Template CSV**, then upload it.
  Industrial-sensor data is not weighing-scale calibration data; do not present it as such.
- Inspector labels are never used for clustering, only for validation afterwards.
- Cluster→risk mapping: clusters ranked by mean risk score; lowest = Low, highest = High, rest = Medium. "High" = predicted non-compliant.


## Windows note: duplicate page URL error
This archive contains exactly one Validation page: `pages/4_Validation.py`. It does not contain `pages/5_Validation.py`. If Streamlit still reports both files, you are likely running an older extracted project folder. Extract this ZIP into a NEW folder (or delete the old `p` folder first), then run `streamlit run app.py` from the new `p` folder. Do not merge the new files into an old folder, because stale page files can remain.
