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
p_mem = float(v[0]+v[1]+v[2]+v[3]+v[4]+v[5]+v[6])
print (v[0]+v[1]+v[2]+v[3])/p_mem, (v[4]+v[5])/p_mem, v[6]/p_mem
print "PTEN_state1:", int(v[0]+v[1]+v[2]+v[3])
print "PTEN_state2:", int(v[4]+v[5])
print "PTEN_state3:", int(v[6])
print "PTEN_membrane:", int(v[0]+v[1]+v[2]+v[3]+v[4]+v[5]+v[6])
print "PTENvol:", int(v[7])
print "PTEN_p2:", int(v[0]+v[2])
print "PTEN_p3:", int(v[1]+v[3])
print "PI3K_p2:", int(v[10]+v[11])
print "PI3Kv:", int(v[8])
print "PI3K_membrane:", int(v[8]+v[10]+v[11])
print "PI3Kvol:", int(v[9])
print "PIP3_free:", int(v[12]+v[14])
print "PIP2_free:", int(v[13]+v[15])
print "PIP3:", int(v[1]+v[3]+v[12]+v[14])
print "PIP2:", int(v[0]+v[2]+v[13]+v[15])
print "PIP_total:", int(v[1]+v[3]+v[12]+v[14])+int(v[0]+v[2]+v[13]+v[15])
print "PIP3/PIP2:", (v[1]+v[3]+v[12]+v[14])/(v[0]+v[2]+v[13]+v[15])

