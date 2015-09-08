import numpy as np
import sys

filename = sys.argv[1]

f = open(filename, 'r')
legendTitles = f.readline().strip().split(",")
speciesNames = []
for i in range(len(legendTitles)-2):
  speciesNames.append(legendTitles[i+2])
print speciesNames

data = np.genfromtxt(filename, delimiter=',', skip_header=1)
mean = np.mean(data, axis=0, dtype=np.float64)
cols = mean.shape[0]
v = mean[2:cols]
print v
print "1st order rate:", v[cols-2-1]*v[cols-2-2]
