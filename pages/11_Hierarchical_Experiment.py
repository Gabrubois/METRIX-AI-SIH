from common import *
import plotly.figure_factory as ff
from sklearn.metrics import adjusted_rand_score as ari
rec,feat=init(); res=controls(feat)
st.title("🌳 Hierarchical Clustering Experiment"); st.caption("Experimental comparison to K-Medoids (average linkage on the same distance matrices).")
k=S.k; rows=[]
for m in ("euclidean","manhattan"):
    h=hierarchical(res[m]["D"],k); rows.append(dict(metric=m,ARI_vs_KMedoids=ari(h,res[m]["labels"]),ARI_vs_inspector=ari(h,feat.confirmed_non_compliant),cluster_sizes=str(np.bincount(h).tolist())))
st.dataframe(pd.DataFrame(rows))
n=st.slider("Instruments in dendrogram",20,80,40); m=st.radio("Metric",["euclidean","manhattan"],horizontal=True)
from scipy.cluster.hierarchy import linkage; from scipy.spatial.distance import squareform
fig=ff.create_dendrogram(res["Z"][:n],labels=feat.instrument_id.iloc[:n].tolist(),linkagefun=lambda x:linkage(squareform(res[m]["D"][:n,:n],checks=False),"average"))
fig.update_layout(template=T,height=500); st.plotly_chart(fig,use_container_width=True)
