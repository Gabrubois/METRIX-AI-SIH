from common import *
rec,feat=init()
st.title("How It Works")
st.markdown("""**Euclidean:** √Σ(xᵢ−yᵢ)² · **Manhattan:** Σ|xᵢ−yᵢ| (both coded in NumPy, tested against scikit-learn)  
**K-Medoids:** choose k instruments as centres → assign everyone to the nearest → re-pick each centre as the most central member → repeat until stable.  
**Standardisation:** all features rescaled to the same range so none dominates.  
**Risk weights:**""")
st.dataframe(pd.DataFrame({"feature":list(W),"weight":list(W.values())}),hide_index=True)
st.markdown("**Cluster → risk:** by average member score (lowest Low, highest High). **Validation:** labels used only after clustering. **Limits:** demo data is synthetic; weights are assumptions; results depend on k and features.")
