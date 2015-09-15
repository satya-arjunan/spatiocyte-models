import numpy as np
import sys

filename = "hislog.Translocating.Neurite0.csv"
if(len(sys.argv) == 2):
  filename = sys.argv[1]

f = open(filename, 'r')
legendTitles = f.readline().strip().split(",")
logInterval = float(legendTitles[1])
speciesNames = []
speciesRadii = []
for i in range(len(legendTitles)-2):
  speciesNames.append(legendTitles[i+2])

startTime = 5

data = np.genfromtxt(filename, delimiter=',', skip_header=1)
mean = np.mean(data, axis=0, dtype=np.float64)
print mean
