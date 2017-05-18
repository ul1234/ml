import matplotlib
import matplotlib.pyplot as plt
import kNN
from numpy import *
#reload(kNN)

datingDataMat, datingDataLabels = kNN.file2matrix('datingTestSet2.txt')

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15*array(datingDataLabels), 15*array(datingDataLabels))
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], c=15*array(datingDataLabels))
plt.show()
