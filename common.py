import io, numpy as np, pandas as pd, streamlit as st, plotly.express as px, plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from config import DATA, FEATURES, ROOT
from modules.data_loader import generate_synthetic, load_csv, validate_columns, save_synthetic
from modules.preprocessing import clean, outlier_counts
from modules.feature_engineering import build_features
from modules.distance_metrics import verify, nearest, euclidean_matrix, manhattan_matrix
from modules.clustering import run_analysis, hierarchical
from modules.risk_segmentation import risk_score, explain, contributions, W
from modules.report_generator import export_all
S=st.session_state; T="plotly_dark"
def card(t,v): st.markdown(f"<div class='glass'><div>{t}</div><div class='big'>{v}</div></div>",unsafe_allow_html=True)
def init():
    st.set_page_config("METRIX AI",page_icon="⚖️",layout="wide")
    st.markdown(f"<style>{(ROOT/'assets/styles.css').read_text()}</style>",unsafe_allow_html=True)
    st.sidebar.markdown("## ⚖️ METRIX AI"); st.sidebar.caption("Intelligent Instrument Verification & Risk Analytics")
    if "raw" not in S:
        p=DATA/"synthetic/synthetic_instrument_records.csv"
        S.raw=pd.read_csv(p) if p.exists() else save_synthetic(); S.src="SYNTHETIC demo data"
    with st.sidebar.expander("📁 Data source"):
        up=st.file_uploader("Upload CSV",type="csv")
        if up is not None and S.get("upname")!=up.name:
            df=load_csv(up); miss=validate_columns(df)
            if miss: st.error(f"Missing columns: {miss}")
            else: S.raw=df; S.src=f"Uploaded: {up.name}"; S.upname=up.name; S.pop("res",None)
        st.download_button("⬇ Template CSV (required columns)",generate_synthetic(3,1).to_csv(index=False),"template.csv")
        if st.button("Use synthetic demo data"): S.raw=save_synthetic(); S.src="SYNTHETIC demo data"; S.pop("res",None)
        if st.button("🔄 Reset analysis"): S.clear(); st.rerun()
    st.sidebar.caption(f"Data: {S.src}")
    rec=clean(S.raw); return rec,build_features(rec)
def controls(feat):
    with st.sidebar.expander("⚙️ Analysis settings",expanded=True):
        cols=st.multiselect("Features used",FEATURES,default=FEATURES); k=st.slider("Number of groups (k)",2,6,3)
        if not cols: st.error("Select at least one feature."); st.stop()
        if len(feat)<=k+1: st.error("Too few instruments for this k. Lower k."); st.stop()
        if st.button("▶ Run analysis") or "res" not in S:
            with st.spinner("Computing..."): S.res=run_analysis(feat,cols,k); S.k=k; S.cols=cols
    return S.res
def headline(t): st.markdown(f"<div class='headline'>{t}</div>",unsafe_allow_html=True)
def verdict(res):
    e,m=res["euclidean"]["metrics"],res["manhattan"]["metrics"]
    w="Euclidean" if (e["f1"],e["ARI"])>(m["f1"],m["ARI"]) else "Manhattan" if (m["f1"],m["ARI"])>(e["f1"],e["ARI"]) else "Neither (tie)"
    return w,f"{w} matches inspector findings better (F1 {e['f1']:.2f} Euclidean vs {m['f1']:.2f} Manhattan; ARI {e['ARI']:.2f} vs {m['ARI']:.2f})."
def note(what,how,read):
    with st.expander("ℹ️ Explain this page"):
        st.markdown(f"**What it shows:** {what}\n\n**How it is calculated:** {how}\n\n**How to read it:** {read}")
