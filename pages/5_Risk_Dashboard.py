from common import *
rec,feat=init()
res=controls(feat)
m=st.radio("Metric",["euclidean","manhattan"],horizontal=True); t=res[m]["table"]
st.caption("Risk groups are analytical prioritisation aids, NOT legal declarations of non-compliance.")
g=st.multiselect("Risk group",["Low","Medium","High"],default=["High"]); q=st.text_input("Search ID")
v=t[t.risk_group.isin(g)]; v=v[v.instrument_id.str.contains(q,case=False)] if q else v
st.plotly_chart(px.pie(t,names="risk_group",template=T,color="risk_group",color_discrete_map={"Low":"#22d3ee","Medium":"#3b82f6","High":"#ef4444"}),use_container_width=True)
st.dataframe(v.sort_values("risk_score",ascending=False),use_container_width=True)
iid=st.selectbox("Profile",t.instrument_id); st.write(feat[feat.instrument_id==iid].T); st.write("Top drivers:",t[t.instrument_id==iid].risk_reasons.iloc[0])
