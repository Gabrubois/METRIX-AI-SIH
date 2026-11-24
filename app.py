from common import *
rec,feat=init(); res=controls(feat)
st.markdown("<div class='hero'>METRIX AI</div>",unsafe_allow_html=True)
st.subheader("Intelligent Instrument Verification & Risk Analytics"); st.caption("SIH26036 · Euclidean vs Manhattan distance for grouping weighing & measuring instruments")
for col,(a,b) in zip(st.columns(4),[("Test records",len(rec)),("Instruments",len(feat)),("High-risk group",int((res['euclidean']['table'].risk_group=='High').sum())),("Inspector-flagged",int(feat.confirmed_non_compliant.sum()))]):
    with col: card(a,b)
st.write("")
headline("Result: "+verdict(res)[1]+(" (synthetic demo data)" if (feat.data_source=="SYNTHETIC").all() else ""))
c=st.columns(3)
for col,(t,d) in zip(c,[("1 · Describe","Turn each instrument's test records into 10 calibration & usage features."),("2 · Group","Cluster instruments with Euclidean and Manhattan distance (K-Medoids) and compare."),("3 · Validate","Check the groups against inspector-confirmed non-compliant cases.")]):
    col.markdown(f"<div class='glass'><b>{t}</b><br>{d}</div>",unsafe_allow_html=True)
st.caption("Use the sidebar pages in order: Data & Features → Compare Metrics → Risk → Validation → Reports. 'How It Works' explains every formula.")
