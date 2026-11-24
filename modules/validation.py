import numpy as np
from sklearn.metrics import precision_score,recall_score,f1_score,confusion_matrix,adjusted_rand_score,normalized_mutual_info_score,silhouette_score
def validate(D,labels,risk_names,truth):
    pred=np.array([1 if risk_names[l]=="High" else 0 for l in labels]); t=np.asarray(truth)
    return dict(precision=precision_score(t,pred,zero_division=0),recall=recall_score(t,pred,zero_division=0),
      f1=f1_score(t,pred,zero_division=0),ARI=adjusted_rand_score(t,labels),NMI=normalized_mutual_info_score(t,labels),
      silhouette=silhouette_score(D,labels,metric="precomputed") if len(set(labels))>1 else float("nan"),
      tn=int(confusion_matrix(t,pred,labels=[0,1])[0,0]),fp=int(confusion_matrix(t,pred,labels=[0,1])[0,1]),
      fn=int(confusion_matrix(t,pred,labels=[0,1])[1,0]),tp=int(confusion_matrix(t,pred,labels=[0,1])[1,1]))
