import pandas as pd
from config import DATA
def export_all(rec,feat,res):
    E=DATA/"exports"; P=DATA/"processed"
    rec.to_csv(P/"instrument_test_records.csv",index=False); feat.to_csv(P/"instrument_features.csv",index=False)
    for m in ("euclidean","manhattan"): res[m]["table"].to_csv(P/f"{m}_clusters.csv",index=False)
    feat[["instrument_id","confirmed_non_compliant","data_source"]].to_csv(P/"inspector_validation_records.csv",index=False)
    cmp=pd.DataFrame({m:res[m]["metrics"] for m in ("euclidean","manhattan")}).T; cmp.index.name="metric"
    cmp.to_csv(E/"metric_comparison.csv")
    a,b=res["euclidean"]["table"],res["manhattan"]["table"]
    a[["instrument_id","risk_score","risk_group","risk_reasons"]].merge(b[["instrument_id","risk_group"]],on="instrument_id",suffixes=("_euclidean","_manhattan")).to_csv(E/"risk_analysis_report.csv",index=False)
    a.merge(b[["instrument_id","cluster","risk_group"]],on="instrument_id",suffixes=("_euclidean","_manhattan")).to_csv(E/"final_results.csv",index=False)
    return cmp
