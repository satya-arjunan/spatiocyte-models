import numpy as np
import sys

filename = "IterateLog.csv"
if(len(sys.argv) == 2):
  filename = sys.argv[1]

f = open(filename, 'r')
legendTitles = f.readline().strip().split(",")
logInterval = float(legendTitles[0].split("=")[1])
len_x = float(legendTitles[1].split("=")[1])
len_y = float(legendTitles[2].split("=")[1])
len_z = float(legendTitles[3].split("=")[1])
voxelRadius = float(legendTitles[4].split("=")[1])
scale = voxelRadius*2
speciesNames = []
speciesRadii = []
for i in range(len(legendTitles)-5):
  speciesNames.append(legendTitles[i+5].split("=")[0])
  speciesRadii.append(float(legendTitles[i+5].split("=")[1]))
print speciesNames

startTime = 5

data = np.genfromtxt(filename, delimiter=',', skip_header=int(startTime/logInterval)+1)
mean = np.mean(data, axis=0, dtype=np.float64)
cols = mean.shape[0]
v = mean[1:cols]
print v
p_mem = float(v[0]+v[1]+v[2]+v[3]+v[4])
print (v[0]+v[1])/p_mem, (v[2]+v[3])/p_mem, v[4]/p_mem

