from common import *
rec,feat=init(); res=controls(feat)
st.title("🎯 Cluster Optimizer"); st.caption("Sweeps k for both metrics; use it to justify your choice of k.")
kmax=st.slider("Max k",3,8,6)
if st.button("Run sweep") or "sweep" in S:
    if "sweep" not in S or st.session_state.get("sweep_kmax")!=kmax:
        rows=[]; bar=st.progress(0.0)
        for i,k in enumerate(range(2,kmax+1)):
            r=run_analysis(feat,S.cols,k,3)
            for m in ("euclidean","manhattan"):
                x=r[m]["metrics"]; rows.append(dict(k=k,metric=m,silhouette=x["silhouette"],F1=x["f1"],ARI=x["ARI"],NMI=x["NMI"],cost=x["cost"]))
            bar.progress((i+1)/(kmax-1))
        S.sweep=pd.DataFrame(rows); S.sweep_kmax=kmax
    sw=S.sweep; c=st.columns(2)
    for i,y in enumerate(["silhouette","F1","ARI","NMI"]): c[i%2].plotly_chart(px.line(sw,x="k",y=y,color="metric",markers=True,template=T,title=y),use_container_width=True)
    st.dataframe(sw); b=sw.loc[sw.silhouette.idxmax()]; st.success(f"Best silhouette: {b.metric}, k={int(b.k)}")
    st.download_button("⬇ Sweep CSV",sw.to_csv(index=False),"k_sweep.csv")
