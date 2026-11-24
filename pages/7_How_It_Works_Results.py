from common import *
rec,feat=init()
st.title("7 · How It Works")
st.markdown("""
**Euclidean distance:** √Σ(xᵢ − yᵢ)² — straight-line distance; one large difference counts extra.  
**Manhattan distance:** Σ|xᵢ − yᵢ| — adds up differences; every feature counts in proportion.  
Both are written from scratch in NumPy and checked against scikit-learn in the tests.

**K-Medoids:** pick k instruments as centres → assign each instrument to the nearest centre → re-pick each centre as the member closest to its group → repeat until stable. It runs on the full distance matrix, so the metric really changes the result.

**Standardisation:** every feature is rescaled (mean 0, spread 1) so large-valued features do not dominate. Same scaling for both metrics.

**Risk score weights:**""")
st.dataframe(pd.DataFrame({"feature":list(W),"weight":list(W.values())}))
st.markdown("""**Cluster → risk mapping:** clusters ranked by average risk score; lowest = Low, highest = High, rest = Medium.  
**Validation:** inspector labels are used only after clustering, never to build it.  
**Limits:** demo data is synthetic; weights are expert-style assumptions, not legal rules; results depend on k and chosen features.""")
