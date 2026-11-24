import numpy as np, pandas as pd
W={"mean_abs_deviation":.15,"max_abs_deviation":.10,"calibration_failure_freq":.25,"historical_failure_rate":.15,
   "violation_indicator":.10,"usage_intensity":.10,"maintenance_freq":.05,"days_since_calibration":.10}
def _norm(x): r=x.max()-x.min(); return (x-x.min())/r if r>0 else x*0
def risk_score(f): return sum(w*_norm(f[c]) for c,w in W.items())*100
def explain(f):
    Z=pd.DataFrame({c:_norm(f[c])*w for c,w in W.items()})
    return [", ".join(r.nlargest(3).index) for _,r in Z.iterrows()]
def cluster_risk_map(labels,score):
    """Documented mapping: clusters ranked by mean risk score; lowest->Low, highest->High, rest->Medium."""
    m=pd.Series(np.asarray(score)).groupby(np.asarray(labels)).mean().sort_values(); n={}
    for i,c in enumerate(m.index): n[c]="Low" if i==0 else ("High" if i==len(m)-1 else "Medium")
    return n

def contributions(f):
    """Points each feature adds to the 0-100 risk score (they sum exactly to risk_score)."""
    return pd.DataFrame({c:_norm(f[c])*w*100 for c,w in W.items()})
