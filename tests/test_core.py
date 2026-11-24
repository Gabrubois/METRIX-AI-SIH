import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).parents[1]))
import numpy as np
from modules.data_loader import generate_synthetic,validate_columns
from modules.preprocessing import clean
from modules.feature_engineering import build_features
from modules.distance_metrics import euclidean_matrix,manhattan_matrix,verify
from modules.clustering import run_analysis
from config import FEATURES
def test_distances():
    a=np.array([[0,0],[3,4]]); assert euclidean_matrix(a)[0,1]==5 and manhattan_matrix(a)[0,1]==7
    assert all(verify(np.random.rand(20,4)))
def test_zero_reference():
    d=generate_synthetic(5,2); d.loc[0,"reference_value"]=0; d.loc[0,"measured_value"]=0.0
    c=clean(d); assert c.percentage_error.notna().all() and c.percentage_error.iloc[0]==0
def test_missing_and_columns():
    d=generate_synthetic(5,2); assert validate_columns(d)==[]; d.loc[1,"operating_hours"]=np.nan
    assert clean(d).operating_hours.notna().all()
def test_pipeline():
    f=build_features(clean(generate_synthetic(60,4))); r=run_analysis(f,FEATURES,3,3)
    for m in("euclidean","manhattan"): assert len(set(r[m]["labels"]))==3 and 0<=r[m]["metrics"]["f1"]<=1

def test_contributions_sum_to_score():
    from modules.risk_segmentation import contributions,risk_score
    f=build_features(clean(generate_synthetic(40,4))); assert np.allclose(contributions(f).sum(axis=1),risk_score(f))
