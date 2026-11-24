from common import *
rec,feat=init()
st.write("Duplicates removed:",len(S.raw)-len(S.raw.drop_duplicates()))
st.write("Missing before / after cleaning",S.raw.isna().sum().sum(),rec.isna().sum().sum())
st.write("IQR outliers",outlier_counts(rec,["calibration_deviation","percentage_error","operating_hours"]))
st.write("Raw vs processed"); a,b=st.columns(2); a.dataframe(S.raw.head(8)); b.dataframe(rec.head(8))
st.write("Standardised features (StandardScaler, shared by both metrics)")
st.dataframe(((feat[FEATURES]-feat[FEATURES].mean())/feat[FEATURES].std()).head(8))
