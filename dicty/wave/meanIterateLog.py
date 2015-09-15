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

startTime = 5

data = np.genfromtxt(filename, delimiter=',', skip_header=int(startTime/logInterval)+1)
mean = np.mean(data, axis=0, dtype=np.float64)
cols = mean.shape[0]
v = mean[1:cols]
PTENvol = v[0]
PTEN = v[1]
PTENa = v[2]
PTENac = v[3]
PTENp2 = v[4]
PTENp2c = v[5]
PTENp3 = v[6]
PTENp3c = v[7]
PI3Kvol = v[8]
PI3K = v[9]
PI3Ka = v[10]
PI3Kac = v[11]
PI3Kp2 = v[12]
PI3Kp2c = v[13]
PI3Kp3 = v[14]
PI3Kp3c = v[15]
PIP2 = v[16]
PIP2c = v[17]
PIP3 = v[18]
PIP3c = v[19]

pten_mem = PTEN+PTENa+PTENac+PTENp2+PTENp2c+PTENp3+PTENp3c
print (PTENp2+PTENp2c)/pten_mem, (PTENa+PTENac+PTENp3+PTENp3c)/pten_mem, PTEN/pten_mem
print "PTEN_state1:", int(PTENp2+PTENp2c)
print "PTEN_state2:", int(PTENa+PTENac+PTENp3+PTENp3c)
print "PTEN_state3:", int(PTEN)
print "PTEN_membrane:", int(pten_mem)
print "PTENvol:", int(PTENvol), PTENvol/(pten_mem+PTENvol)
print "PTEN total:", int(pten_mem+PTENvol)
print "PTEN_a:", int(PTENa+PTENac)
print "PTEN_p2:", int(PTENp2+PTENp2c)
print "PTEN_p3:", int(PTENp3+PTENp3c)
print "PTENv:", int(PTEN)
print "PI3K_a:", int(PI3Ka+PI3Kac)
print "PI3K_p2:", int(PI3Kp2+PI3Kp2c)
print "PI3K_p3:", int(PI3Kp3+PI3Kp3c)
print "PI3Kv:", int(PI3K)
pi3k_mem = PI3K+PI3Ka+PI3Kac+PI3Kp2+PI3Kp2c+PI3Kp3+PI3Kp3c
print "PI3K_membrane:", int(pi3k_mem)
print "PI3Kvol:", int(PI3Kvol)
print "PI3K total:", int(pi3k_mem+PI3Kvol)
print "PIP2_free:", int(PIP2)
print "PIP3_free:", int(PIP3)
pip2 = PTENp2+PTENp2c+PI3Kp2+PI3Kp2c+PIP2+PIP2c
print "PIP2:", int(pip2)
pip3 = PTENp3+PTENp3c+PI3Kp3+PI3Kp3c+PIP3+PIP3c
print "PIP3:", int(pip3)
print "PIP_total:", pip3+pip2
print "PIP3/PIP2:", pip3/(pip2+pip3)

