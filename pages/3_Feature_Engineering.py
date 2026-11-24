from common import *
rec,feat=init()
st.dataframe(feat.head(50),use_container_width=True); st.dataframe(feat[FEATURES].describe())
st.plotly_chart(px.imshow(feat[FEATURES].corr(),text_auto=".2f",template=T,color_continuous_scale="RdBu_r"),use_container_width=True)
f=st.selectbox("Distribution",FEATURES); st.plotly_chart(px.histogram(feat,x=f,color="instrument_category",template=T),use_container_width=True)
