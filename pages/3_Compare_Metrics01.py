from common import *
from sklearn.metrics import adjusted_rand_score as ari
rec,feat=init(); res=controls(feat)
st.title("3 · Euclidean vs Manhattan")
note("The same instruments grouped twice: once using Euclidean distance, once using Manhattan distance.","Features are standardised (same scale), then distance = √Σ(a−b)² for Euclidean, Σ|a−b| for Manhattan. K-Medoids picks k real instruments (medoids) as group centres and assigns every instrument to its nearest one. Hierarchical clustering is an extra check.",
 "Cluster numbers (0,1,2) are just names, so cluster 0 under Euclidean is not the same as cluster 0 under Manhattan. Use the agreement score (ARI): 1 = identical groupings, near 0 = unrelated. Euclidean punishes one big difference more; Manhattan treats all differences evenly.")
eu,ma=res["euclidean"],res["manhattan"]; a=ari(eu["labels"],ma["labels"])
st.metric("Agreement between the two groupings (ARI)",f"{a:.2f}")
st.info(f"The two metrics give {'very similar' if a>.8 else 'moderately similar' if a>.5 else 'noticeably different'} groupings (ARI {a:.2f}). Hierarchical vs K-Medoids (Euclidean): ARI {ari(eu['labels'],res['hier']):.2f}.")
p=PCA(2).fit_transform(res["Z"]); c=st.columns(2)
for col,(m,r) in zip(c,(("Euclidean",eu),("Manhattan",ma))):
    t=r["table"].assign(PC1=p[:,0],PC2=p[:,1],cluster=r["labels"].astype(str))
    col.plotly_chart(px.scatter(t,x="PC1",y="PC2",color="cluster",hover_name="instrument_id",template=T,title=f"{m} groups (2-D picture)"),use_container_width=True)
    col.caption("Group sizes"); col.dataframe(r["table"].cluster.value_counts().sort_index().rename("instruments")); col.caption("Medoids (most representative instruments)"); col.dataframe(r["table"][r["table"].is_medoid][["instrument_id","cluster","risk_group"]])
st.caption("PCA squashes the features into 2-D only for drawing. It is not used for clustering.")
st.subheader("Find similar instruments")
iid=st.selectbox("Instrument",feat.instrument_id); i=int(feat.index[feat.instrument_id==iid][0]); n=st.slider("Neighbours",3,10,5)
ne,nm=nearest(eu["D"],i,n),nearest(ma["D"],i,n)
st.dataframe(pd.DataFrame({"Euclidean nearest":feat.instrument_id.iloc[ne].values,"Manhattan nearest":feat.instrument_id.iloc[nm].values}))
st.write(f"{len(set(ne)&set(nm))} of {n} neighbours are the same under both metrics.")
d=eu["table"].merge(ma["table"],on="instrument_id",suffixes=("_E","_M")); d=d[d.risk_group_E!=d.risk_group_M]
st.write(f"**{len(d)} instruments** get a different risk group depending on the metric:"); st.dataframe(d[["instrument_id","risk_group_E","risk_group_M","risk_score_E"]])
