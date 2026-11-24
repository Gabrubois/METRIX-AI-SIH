from common import *
rec,feat=init(); res=controls(feat)
st.title("🧪 What-If Simulator"); st.caption("Edit an instrument's features and see which group it falls into under both metrics.")
iid=st.selectbox("Base instrument",feat.instrument_id); base=feat[feat.instrument_id==iid].iloc[0]
new={}; cols=st.columns(3)
for i,c in enumerate(S.cols):
    lo,hi=float(feat[c].min()),float(feat[c].max()); new[c]=cols[i%3].slider(c,lo,hi,float(np.clip(base[c],lo,hi)),(hi-lo)/100 or 0.01)
sc=StandardScaler().fit(feat[S.cols]); z=sc.transform(pd.DataFrame([new]))[0]; Z=res["Z"]
tmp=feat.copy(); tmp.loc[len(tmp)]=tmp.iloc[0]; 
for c,v in new.items(): tmp.loc[tmp.index[-1],c]=v
sc_new=risk_score(tmp).iloc[-1]; out=[]
for m,fn in (("euclidean",lambda a,b:np.sqrt(((a-b)**2).sum(1))),("manhattan",lambda a,b:np.abs(a-b).sum(1))):
    med=res[m]["medoids"]; d=fn(Z[med],z); c=int(np.argmin(d)); lab=res[m]["table"].cluster.iloc[med[c]]
    out.append(dict(metric=m,assigned_cluster=int(lab),risk_group=res[m]["risk_names"][lab],distance_to_medoid=round(float(d[c]),3)))
st.metric("Recomputed risk score (0-100)",f"{sc_new:.1f}",f"{sc_new-risk_score(feat).iloc[feat.index[feat.instrument_id==iid][0]]:+.1f} vs original"); st.dataframe(pd.DataFrame(out))
