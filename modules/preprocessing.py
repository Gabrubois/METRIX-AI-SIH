import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
def clean(df):
    d=df.drop_duplicates().copy()
    for c in ["verification_date","last_calibration_date"]: d[c]=pd.to_datetime(d[c],errors="coerce")
    num=d.select_dtypes("number").columns
    d[num]=d[num].apply(lambda s:s.fillna(s.median()))
    for c in d.select_dtypes(exclude="number"): d[c]=d[c].fillna("Unknown")
    d["calibration_deviation"]=d["measured_value"]-d["reference_value"]
    ref=d["reference_value"].abs()
    d["percentage_error"]=(d["calibration_deviation"].abs()/ref.replace(0,np.nan)*100).fillna(0)
    return d
def outlier_counts(df,cols):
    o={}
    for c in cols:
        q1,q3=df[c].quantile([.25,.75]); i=q3-q1; o[c]=int(((df[c]<q1-1.5*i)|(df[c]>q3+1.5*i)).sum())
    return pd.Series(o,name="iqr_outliers")
def scale(X): s=StandardScaler(); return s.fit_transform(X),s
