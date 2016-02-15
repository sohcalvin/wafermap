import pandas as pd
import numpy as np

from common.data_utility import loadData

dataOneLinePerMap = loadData()


tmp = [i[1] for i in dataOneLinePerMap]
X = pd.DataFrame(tmp)
Y = np.array([i[0] for i in dataOneLinePerMap])

from sklearn.cluster import KMeans
num_clusters = 2
km = KMeans(n_clusters=num_clusters)
km.fit(X)
print(km.n_clusters)

clusters = km.labels_.tolist()
print("Length of cluster variable= {0}".format(len(clusters)))

data = { 'pattern': Y, 'cluster': clusters}
frame = pd.DataFrame(data, index = [Y] , columns = ['pattern', 'cluster'])

print(frame)