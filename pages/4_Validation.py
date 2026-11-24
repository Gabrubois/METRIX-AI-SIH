from common import *
rec,feat=init(); res=controls(feat)
st.title("Inspector Validation")
headline(verdict(res)[1]); 
if (feat.data_source=="SYNTHETIC").all(): st.warning("Labels are synthetic: this validates the method, not real-world accuracy.")
note("How well the High-risk group matches instruments inspectors marked non-compliant.","Clustering never sees the labels. Afterwards 'High' cluster = predicted non-compliant, compared with the labels (non-compliant = at least half the tests failed). Winner decided by F1, then ARI.","Precision: of those flagged, how many were right. Recall: of all truly non-compliant, how many were found. F1: balance of both. ARI/NMI: match between groups and labels (0 unrelated, 1 identical). Silhouette: how separated the groups are.")
M=pd.DataFrame({m.title():{k:res[m]["metrics"][k] for k in ("precision","recall","f1","ARI","NMI","silhouette")} for m in("euclidean","manhattan")}).round(3)
st.plotly_chart(px.bar(M.reset_index().melt("index"),x="index",y="value",color="variable",barmode="group",template=T,labels={"index":"","value":"score","variable":"Metric"}),use_container_width=True)
st.dataframe(M.T)
with st.expander("Confusion matrices"):
    c=st.columns(2)
    for col,m in zip(c,("euclidean","manhattan")):
        x=res[m]["metrics"]; col.plotly_chart(px.imshow([[x["tn"],x["fp"]],[x["fn"],x["tp"]]],text_auto=True,x=["Predicted OK","Predicted High"],y=["Compliant","Non-compliant"],template=T,title=m.title()),use_container_width=True)
        col.caption(f"{x['tp']} caught · {x['fp']} false alarms · {x['fn']} missed · {x['tn']} correctly cleared")
