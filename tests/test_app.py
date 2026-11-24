import sys,pathlib,glob; R=pathlib.Path(__file__).parents[1]; sys.path.insert(0,str(R))
import numpy as np,pandas as pd,pytest
from streamlit.testing.v1 import AppTest
PAGES=[str(R/"app.py")]+sorted(glob.glob(str(R/"pages/*.py")))
def run(p): return AppTest.from_file(p,default_timeout=180).run()
def btn(at,label): return next(b for b in at.sidebar.button if label in b.label)
@pytest.mark.parametrize("p",PAGES)
def test_page_loads(p): assert not run(p).exception
@pytest.mark.parametrize("k",[2,5,6])
def test_change_k_and_rerun(k):
    at=run(str(R/"pages/2_Compare_Metrics.py")); at.sidebar.slider[0].set_value(k); btn(at,"Run analysis").click().run()
    assert not at.exception and len(set(at.session_state["res"]["euclidean"]["labels"]))==k
def test_feature_subset_and_empty():
    at=run(str(R/"pages/3_Risk.py")); at.sidebar.multiselect[0].set_value(["mean_abs_deviation","maintenance_freq"]); btn(at,"Run analysis").click().run(); assert not at.exception
    at.sidebar.multiselect[0].set_value([]); at.run(); assert not at.exception and at.sidebar.error
def test_messy_upload():
    from modules.data_loader import generate_synthetic
    d=generate_synthetic(40,3); d.loc[3:8,"operating_hours"]=np.nan; d=pd.concat([d,d.head(5)]); d.loc[1,"reference_value"]=0
    at=AppTest.from_file(str(R/"pages/4_Validation.py"),default_timeout=180); at.session_state["raw"]=d; at.session_state["src"]="test"; at.run(); assert not at.exception
def test_reports_files_nonempty():
    at=run(str(R/"pages/5_Reports.py")); assert not at.exception
    for f in ["processed/instrument_features.csv","processed/euclidean_clusters.csv","processed/manhattan_clusters.csv","exports/metric_comparison.csv","exports/risk_analysis_report.csv","exports/final_results.csv"]:
        assert pd.read_csv(R/"data"/f).shape[0]>0
