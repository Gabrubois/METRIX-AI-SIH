import numpy as np
from sklearn.metrics import pairwise_distances
def euclidean_matrix(X):
    X=np.asarray(X,float); return np.sqrt(((X[:,None,:]-X[None,:,:])**2).sum(-1))
def manhattan_matrix(X):
    X=np.asarray(X,float); return np.abs(X[:,None,:]-X[None,:,:]).sum(-1)
def verify(X):
    return (np.allclose(euclidean_matrix(X),pairwise_distances(X,metric="euclidean")),
            np.allclose(manhattan_matrix(X),pairwise_distances(X,metric="manhattan")))
def nearest(D,i,n=5): o=np.argsort(D[i]); return [int(j) for j in o if j!=i][:n]
