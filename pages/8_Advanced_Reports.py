from common import *
rec,feat=init()
res=controls(feat)
cmp=export_all(rec,feat,res); st.success("Fresh CSVs written to data/ and available below.")
for lab,pth in [("Processed records","processed/instrument_test_records.csv"),("Engineered features","processed/instrument_features.csv"),("Euclidean clusters","processed/euclidean_clusters.csv"),("Manhattan clusters","processed/manhattan_clusters.csv"),("Inspector validation records","processed/inspector_validation_records.csv"),("Metric comparison","exports/metric_comparison.csv"),("Risk analysis report","exports/risk_analysis_report.csv"),("Final results","exports/final_results.csv")]:
    st.download_button(f"⬇ {lab}",(DATA/pth).read_bytes(),pth.split("/")[-1],key=pth)
st.dataframe(cmp)

import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
def make_pdf():
    b=io.BytesIO()
    with PdfPages(b) as pdf:
        f=plt.figure(figsize=(8.3,11.7)); f.text(.07,.95,"METRIX AI – Verification Risk Report",fontsize=16,weight="bold")
        f.text(.07,.91,f"Data source: {S.src}",fontsize=9); f.text(.07,.89,"Risk groups are analytical aids, not legal declarations of non-compliance.",fontsize=8)
        y=.84
        for m in ("euclidean","manhattan"):
            x=res[m]["metrics"]; f.text(.07,y,m.title(),weight="bold"); y-=.03
            for kk in ("precision","recall","f1","ARI","NMI","silhouette"): f.text(.09,y,f"{kk}: {x[kk]:.3f}",fontsize=9); y-=.022
            y-=.02
        pdf.savefig(f); plt.close(f)
        f,ax=plt.subplots(1,2,figsize=(11,4))
        for a,m in zip(ax,("euclidean","manhattan")): res[m]["table"].risk_group.value_counts().reindex(["Low","Medium","High"]).fillna(0).plot.bar(ax=a,title=m.title())
        pdf.savefig(f); plt.close(f)
    return b.getvalue()
st.download_button("📄 Download complete analysis PDF",make_pdf(),"metrix_report.pdf","application/pdf")
