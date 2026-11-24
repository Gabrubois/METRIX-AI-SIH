from common import *
rec,feat=init()
st.title("Data & Features")
headline(f"{len(rec)} test records from {len(feat)} instruments were cleaned and summarised into 10 features per instrument.")
c=st.columns(4); c[0].metric("Duplicates removed",len(S.raw)-len(S.raw.drop_duplicates())); c[1].metric("Missing values (raw)",int(S.raw.isna().sum().sum())); c[2].metric("Missing (clean)",int(rec.isna().sum().sum())); c[3].metric("Instrument types",rec.instrument_type.nunique())
note("The cleaned data and the features the clustering uses.","Duplicates dropped, gaps filled with the median, deviation = measured − reference, % error = |deviation| ÷ |reference| × 100. Features are averages/maxima/rates per instrument.","The heatmap shows which features move together (red = together, blue = opposite).")
f=st.selectbox("Look at one feature",FEATURES); a,b=st.columns(2)
a.plotly_chart(px.histogram(feat,x=f,color="instrument_category",template=T,title=f"Spread of {f}"),use_container_width=True)
b.plotly_chart(px.imshow(feat[FEATURES].corr(),template=T,color_continuous_scale="RdBu_r",title="How features relate"),use_container_width=True)
with st.expander("Feature definitions"):
    st.table(pd.DataFrame([("mean_abs_deviation","average |measured − reference|"),("max_abs_deviation","largest |measured − reference|"),("mean_pct_error","average % error"),("calibration_failure_freq","share of tests above permissible error"),("days_since_calibration","days since last calibration"),("verification_interval","days between tests"),("usage_intensity","operating hours ÷ usage frequency"),("maintenance_freq","maintenance count"),("historical_failure_rate","past failures ÷ tests"),("violation_indicator","1 if ever above permissible error")],columns=["feature","meaning"]))
with st.expander("Browse the data tables"):
    q=st.text_input("Search instrument ID"); v=feat[feat.instrument_id.str.contains(q,case=False)] if q else feat
    st.dataframe(v.drop(columns=["data_source"]).round(3),use_container_width=True,height=300)
    st.download_button("⬇ Download features",feat.to_csv(index=False),"features.csv")
