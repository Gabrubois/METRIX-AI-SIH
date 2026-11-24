from common import *
rec,feat=init(); res=controls(feat)
st.title("5 · Inspector Validation")
syn=(feat.data_source=="SYNTHETIC").all()
note("How well the groups match instruments that inspectors marked non-compliant.","Clustering never sees these labels. Afterwards, instruments in the High-risk cluster count as 'predicted non-compliant' and are compared with the inspector labels (an instrument is non-compliant if at least half its tests were).",
 "Precision = of those flagged High, how many were truly non-compliant. Recall = of all truly non-compliant, how many we caught. F1 = balance of the two. ARI/NMI = how closely groups match labels (0 = unrelated, 1 = identical). Silhouette = how well separated the groups are (−1 to 1).")
if syn: st.warning("These labels are SYNTHETIC. This validates the method, not real-world performance.")
M=pd.DataFrame({m:{k:res[m]["metrics"][k] for k in ("precision","recall","f1","ARI","NMI","silhouette")} for m in("euclidean","manhattan")}).round(3); st.dataframe(M)
c=st.columns(2)
for col,m in zip(c,("euclidean","manhattan")):
    x=res[m]["metrics"]; col.plotly_chart(px.imshow([[x["tn"],x["fp"]],[x["fn"],x["tp"]]],text_auto=True,x=["Predicted OK","Predicted High"],y=["Truly compliant","Truly non-compliant"],template=T,title=f"Confusion matrix – {m}"),use_container_width=True)
    col.caption(f"{x['tp']} correctly flagged, {x['fp']} flagged by mistake, {x['fn']} missed, {x['tn']} correctly left alone.")
e,ma=M["euclidean"],M["manhattan"]; w="euclidean" if (e.f1,e.ARI)>(ma.f1,ma.ARI) else "manhattan" if (ma.f1,ma.ARI)>(e.f1,e.ARI) else "neither (tie)"
st.success(f"Verdict on this data: **{w}** aligns better (F1 {e.f1} vs {ma.f1}; ARI {e.ARI} vs {ma.ARI}; decided by F1, then ARI). Try other k values in the sidebar: the winner can change.")
