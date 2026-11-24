from common import *
rec,feat=init()
st.title("2 · Features")
note("One row per instrument, built from all its test records. These 10 numbers are what the clustering uses.","Each feature is computed from the records with the simple formulas in the table.","In the heatmap, red/blue = features that move together. Highly correlated features carry similar information.")
F=pd.DataFrame([("mean_abs_deviation","average of |measured − reference|","typical size of error"),("max_abs_deviation","largest |measured − reference|","worst single error"),
("mean_pct_error","average % error","error relative to the reading"),("calibration_failure_freq","share of tests where |deviation| > permissible error","how often it fails"),
("days_since_calibration","days from last calibration to test","calibration age"),("verification_interval","days between tests","testing regularity"),
("usage_intensity","operating hours ÷ usage frequency","how heavily it is used"),("maintenance_freq","maintenance count","upkeep"),
("historical_failure_rate","previous failures ÷ number of tests","past failure tendency"),("violation_indicator","1 if any test exceeded permissible error","ever out of tolerance")],columns=["feature","formula","meaning"])
st.dataframe(F,use_container_width=True); st.dataframe(feat.drop(columns=["data_source"]).head(50),use_container_width=True)
st.dataframe(feat[FEATURES].describe())
st.plotly_chart(px.imshow(feat[FEATURES].corr(),text_auto=".2f",template=T,color_continuous_scale="RdBu_r",title="Correlation between features"),use_container_width=True)
f=st.selectbox("Distribution of",FEATURES); st.plotly_chart(px.histogram(feat,x=f,color="instrument_category",template=T),use_container_width=True)
