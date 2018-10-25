import numpy as np

import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import sys

sv_data = sys.argv[1]

# Extracting feature data
indices = list(range(4, sv_data.shape[1]))
data = sv_data.values[:, indices]
 
targets = sv_data.values[:, 0]
X = data
# #############################################################################
# Compute DBSCAN
db = DBSCAN(min_samples=5, n_jobs=-1).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
d = {}
for label in set(labels):
	d[label] = []

one_indices = []

for i in range(len(labels)):
	if labels[i] in [3, 4, 7, 9]:
		one_indices.append(i)
	if int(targets[i]) == 1:
		d[labels[i]].append(1)
	else:
		d[labels[i]].append(0)
for label in set(labels):
	lab_len = len(d[label])
	d[label] = float(sum(d[label])) / float(len(d[label]))
	print "Cluster number: " + str(label) + ", Percent cancer: " + str(d[label]) + ", Number of samples: " + str(lab_len)
for elem in one_indices:
	print sv_data.values[elem]
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f"
#      % metrics.adjusted_rand_score(labels_true, labels))
#print("Adjusted Mutual Information: %0.3f"
#      % metrics.adjusted_mutual_info_score(labels_true, labels))
#print("Silhouette Coefficient: %0.3f"
#      % metrics.silhouette_score(X, labels))
