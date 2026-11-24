import numpy as np, pandas as pd
from scipy.cluster.hierarchy import linkage,fcluster
from scipy.spatial.distance import squareform
from modules.distance_metrics import euclidean_matrix,manhattan_matrix
from modules.risk_segmentation import risk_score,explain,cluster_risk_map
from modules.validation import validate
from modules.preprocessing import scale
def kmedoids(D,k,seed=0,iters=100):
    """PAM-style K-Medoids on a PRECOMPUTED distance matrix, so the metric drives the result."""
    r=np.random.default_rng(seed); n=len(D); m=[int(r.integers(n))]
    while len(m)<k:
        d=D[:,m].min(1)**2; m.append(int(r.choice(n,p=d/d.sum())) if d.sum()>0 else int(r.integers(n)))
    m=np.array(m)
    for _ in range(iters):
        lab=D[:,m].argmin(1); new=m.copy()
        for c in range(k):
            idx=np.where(lab==c)[0]
            if len(idx): new[c]=idx[D[np.ix_(idx,idx)].sum(1).argmin()]
        if np.array_equal(new,m): break
        m=new
    lab=D[:,m].argmin(1); return lab,m,float(D[np.arange(n),m[lab]].sum())
def best_of(D,k,n_init=10): return min((kmedoids(D,k,s) for s in range(n_init)),key=lambda x:x[2])
def hierarchical(D,k): return fcluster(linkage(squareform(D,checks=False),"average"),k,"maxclust")-1
def run_analysis(feat,cols,k=3,n_init=10):
    Z,_=scale(feat[cols]); score=risk_score(feat).values; reasons=explain(feat); res={}
    for name,fn in (("euclidean",euclidean_matrix),("manhattan",manhattan_matrix)):
        D=fn(Z); lab,med,cost=best_of(D,k,n_init); rn=cluster_risk_map(lab,score)
        t=feat[["instrument_id","instrument_category","instrument_type","data_source"]].copy()
        t["cluster"]=lab; t["is_medoid"]=False; t.iloc[med,t.columns.get_loc("is_medoid")]=True
        t["risk_score"]=score; t["risk_group"]=[rn[l] for l in lab]; t["risk_reasons"]=reasons
        met=validate(D,lab,rn,feat.confirmed_non_compliant); met["cost"]=cost
        res[name]=dict(D=D,labels=lab,medoids=med,table=t,metrics=met,risk_names=rn)
    res["hier"]=hierarchical(res["euclidean"]["D"],k); res["Z"]=Z; return res
