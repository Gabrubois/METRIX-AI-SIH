from common import *
rec,feat=init()
res=controls(feat)
st.warning("Labels are SYNTHETIC unless real inspector data was uploaded. Labels were never used for clustering." if (feat.data_source=="SYNTHETIC").all() else "Validation against uploaded inspector labels.")
st.write("Non-compliant instruments:",int(feat.confirmed_non_compliant.sum()),"of",len(feat))
met=pd.DataFrame({m:res[m]["metrics"] for m in("euclidean","manhattan")}); st.dataframe(met)
for m in("euclidean","manhattan"):
    x=res[m]["metrics"]; st.plotly_chart(px.imshow([[x["tn"],x["fp"]],[x["fn"],x["tp"]]],text_auto=True,x=["Pred compliant","Pred high-risk"],y=["Compliant","Non-compliant"],template=T,title=f"Confusion – {m}"),use_container_width=True)
    st.write("Cluster→risk mapping:",res[m]["risk_names"])
best=max(("euclidean","manhattan"),key=lambda m:res[m]["metrics"]["f1"]); st.success(f"Higher F1 on this data: {best}. ARI/NMI/silhouette shown above; interpret together.")
