from common import *
rec,feat=init()
res=controls(feat)
st.write("Implementation matches scikit-learn (Euclid, Manhattan):",verify(res["Z"][:50]))
a,b=st.columns(2)
for col,m in zip((a,b),("euclidean","manhattan")):
    with col:
        st.subheader(m.title()); t=res[m]["table"]; st.write(t.cluster.value_counts().sort_index().rename("size"))
        st.write("Medoids",t[t.is_medoid][["instrument_id","cluster","risk_group"]])
        st.plotly_chart(px.imshow(res[m]["D"][:60,:60],template=T,title="Distance matrix (first 60)"),use_container_width=True)
from sklearn.metrics import adjusted_rand_score as ari
st.metric("Agreement between metrics (ARI)",round(ari(res["euclidean"]["labels"],res["manhattan"]["labels"]),3))
st.metric("Hierarchical (Euclid) vs K-Medoids Euclid ARI",round(ari(res["euclidean"]["labels"],res["hier"]),3))
dd=pd.DataFrame({"Euclidean":res["euclidean"]["D"][np.triu_indices(len(feat),1)][:20000],"Manhattan":res["manhattan"]["D"][np.triu_indices(len(feat),1)][:20000]})
st.plotly_chart(px.histogram(dd.melt(),x="value",color="variable",barmode="overlay",template=T),use_container_width=True)
iid=st.selectbox("Instrument",feat.instrument_id); i=int(feat.index[feat.instrument_id==iid][0]); n=st.slider("Neighbours",3,10,5)
ne,nm=nearest(res["euclidean"]["D"],i,n),nearest(res["manhattan"]["D"],i,n)
st.dataframe(pd.DataFrame({"Euclidean NN":feat.instrument_id.iloc[ne].values,"Manhattan NN":feat.instrument_id.iloc[nm].values}))
st.write("Neighbour overlap:",len(set(ne)&set(nm)),"/",n)
diff=res["euclidean"]["table"].merge(res["manhattan"]["table"],on="instrument_id",suffixes=("_E","_M"))
st.write("Instruments whose risk group differs:",int((diff.risk_group_E!=diff.risk_group_M).sum())); 
st.dataframe(diff[diff.risk_group_E!=diff.risk_group_M][["instrument_id","risk_group_E","risk_group_M"]])
