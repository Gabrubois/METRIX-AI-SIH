from common import *
rec,feat=init()
st.title("1 · Data & Cleaning")
note("The raw test records and what cleaning did to them.","Duplicates dropped; missing numbers filled with the column median; deviation = measured − reference; % error = |deviation| ÷ |reference| × 100 (0 if reference is 0).","Check the numbers below: 'after' should show no missing values. The source line tells you if data is real or synthetic.")
st.write(f"**Source:** {S.src} · {S.raw.shape[0]} rows × {S.raw.shape[1]} columns")
c=st.columns(3); c[0].metric("Duplicates removed",len(S.raw)-len(S.raw.drop_duplicates())); c[1].metric("Missing before",int(S.raw.isna().sum().sum())); c[2].metric("Missing after",int(rec.isna().sum().sum()))
q=st.text_input("Search instrument ID"); cat=st.multiselect("Category",sorted(rec.instrument_category.unique())); v=rec
if q: v=v[v.instrument_id.str.contains(q,case=False)]
if cat: v=v[v.instrument_category.isin(cat)]
st.write(f"{len(v)} records"); st.dataframe(v.head(500),use_container_width=True)
st.write("**Outliers** (values far outside the typical range, using the IQR rule):"); st.dataframe(outlier_counts(rec,["calibration_deviation","percentage_error","operating_hours"]))
st.download_button("⬇ Download cleaned records",rec.to_csv(index=False),"records.csv")
st.caption("Real Kaggle data: see README for how to add it. Nothing was downloaded automatically.")
