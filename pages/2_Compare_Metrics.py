from common import *
from sklearn.metrics import adjusted_rand_score as ari
rec,feat=init(); res=controls(feat); eu,ma=res["euclidean"],res["manhattan"]; a=ari(eu["labels"],ma["labels"])
st.title("Euclidean vs Manhattan")
headline(f"The two metrics produce {'very similar' if a>.8 else 'moderately similar' if a>.5 else 'noticeably different'} groupings (agreement ARI = {a:.2f}, where 1 means identical).")
note("The same instruments grouped twice, once per distance metric.","Features are standardised, then distance = √Σ(a−b)² (Euclidean) or Σ|a−b| (Manhattan). K-Medoids picks k real instruments as centres and assigns every instrument to the nearest.","Cluster numbers are only names, so compare the shapes and the agreement score. Euclidean punishes one big difference more; Manhattan counts all differences evenly. PCA only flattens the picture to 2-D; it is not used for clustering.")
p=PCA(2).fit_transform(res["Z"]); c=st.columns(2)
for col,(m,r) in zip(c,(("Euclidean",eu),("Manhattan",ma))):
    col.plotly_chart(px.scatter(r["table"].assign(PC1=p[:,0],PC2=p[:,1],group=r["labels"].astype(str)),x="PC1",y="PC2",color="group",hover_name="instrument_id",template=T,title=m),use_container_width=True)
sz=pd.DataFrame({"Euclidean":eu["table"].cluster.value_counts().sort_index(),"Manhattan":ma["table"].cluster.value_counts().sort_index()}); sz.index.name="group"
st.write("**Group sizes**"); st.dataframe(sz.T)
with st.expander("Find similar instruments"):
    iid=st.selectbox("Instrument",feat.instrument_id); i=int(feat.index[feat.instrument_id==iid][0]); n=5
    ne,nm=nearest(eu["D"],i,n),nearest(ma["D"],i,n)
    st.dataframe(pd.DataFrame({"Euclidean nearest":feat.instrument_id.iloc[ne].values,"Manhattan nearest":feat.instrument_id.iloc[nm].values}))
    st.write(f"{len(set(ne)&set(nm))} of {n} neighbours are shared.")
with st.expander("Instruments that change risk group between metrics"):
    d=eu["table"].merge(ma["table"],on="instrument_id",suffixes=("_E","_M")); d=d[d.risk_group_E!=d.risk_group_M]
    st.write(f"{len(d)} instruments"); st.dataframe(d[["instrument_id","risk_group_E","risk_group_M"]],height=250)
with st.expander("Extra check: hierarchical clustering"):
    st.write(f"Agreement with K-Medoids (Euclidean): ARI {ari(eu['labels'],res['hier']):.2f}")
