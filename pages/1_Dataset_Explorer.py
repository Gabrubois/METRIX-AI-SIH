from common import *
rec,feat=init()
st.write(f"**Source:** {S.src} · shape {S.raw.shape}")
q=st.text_input("Search instrument ID"); cat=st.multiselect("Category",sorted(S.raw.instrument_category.unique()))
v=S.raw
if q: v=v[v.instrument_id.str.contains(q,case=False)]
if cat: v=v[v.instrument_category.isin(cat)]
st.write(f"{len(v)} records"); st.dataframe(v.head(500),use_container_width=True)
st.bar_chart(S.raw.instrument_type.value_counts()); st.write("Missing values",S.raw.isna().sum()[lambda s:s>0])
st.download_button("⬇ Download dataset",S.raw.to_csv(index=False),"dataset.csv")
st.caption("Kaggle: place original CSV in data/raw/kaggle_source_data.csv and upload it (see README). Not downloaded here.")
