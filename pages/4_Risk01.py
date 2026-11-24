from common import *
rec,feat=init(); res=controls(feat)
st.title("4 · Verification Risk")
note("A 0–100 risk score for every instrument, and Low / Medium / High groups.","Score = weighted sum of 8 features, each rescaled 0–1 (weights on page 7). A cluster's risk level comes from the AVERAGE score of its members: lowest-scoring cluster = Low, highest = High, others = Medium. The cluster label alone is never assumed to mean risk.",
 "Pick an instrument below to see exactly how many points each feature added. These are prioritisation aids, NOT legal declarations of non-compliance.")
m=st.radio("Metric",["euclidean","manhattan"],horizontal=True); t=res[m]["table"]
st.write("Cluster → risk mapping:",{int(k):v for k,v in res[m]["risk_names"].items()}); st.write(t.groupby("risk_group").risk_score.agg(["count","mean"]).round(1).rename(columns={"count":"instruments","mean":"avg score"}))
g=st.multiselect("Show groups",["Low","Medium","High"],default=["High"]); q=st.text_input("Search ID"); v=t[t.risk_group.isin(g)]
if q: v=v[v.instrument_id.str.contains(q,case=False)]
st.plotly_chart(px.pie(t,names="risk_group",template=T,color="risk_group",color_discrete_map={"Low":"#22d3ee","Medium":"#3b82f6","High":"#ef4444"}),use_container_width=True)
st.dataframe(v.sort_values("risk_score",ascending=False),use_container_width=True)
st.subheader("Why is this instrument scored this way?")
iid=st.selectbox("Instrument",t.instrument_id); i=int(feat.index[feat.instrument_id==iid][0]); C=contributions(feat).iloc[i].sort_values(ascending=False)
st.plotly_chart(px.bar(C[::-1],orientation="h",template=T,labels={"value":"points added","index":"feature"}),use_container_width=True)
txt="; ".join(f"**{c}** = {feat[c].iloc[i]:.3g} (higher than {(feat[c]<=feat[c].iloc[i]).mean()*100:.0f}% of instruments) adds {C[c]:.1f} pts" for c in C.index[:3])
st.success(f"{iid}: score {C.sum():.1f}/100 → **{t.risk_group.iloc[i]}** risk group. Top reasons: {txt}.")
