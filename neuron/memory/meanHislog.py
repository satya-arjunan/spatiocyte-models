import numpy as np
import sys
import math

filename = "hislog.Translocating.Neurite0.csv"
if(len(sys.argv) == 2):
  filename = sys.argv[1]

data = np.loadtxt(filename, delimiter=',', skiprows=1)
bins = 0
initTime = float(data[0][0])
for row in data:
  if(row[0] == initTime): 
    bins = bins+1
logInterval = data[bins][0]-initTime
startTime = 200
startRow = int(np.ceil((startTime-initTime)/logInterval))*bins
print startRow

data = np.loadtxt(filename, delimiter=",", skiprows=startRow+1)
rows,cols = data.shape
Kinesin = data[0:rows, cols-1:cols].reshape(rows/bins, bins)
MTKinesinATP = data[0:rows, cols-2:cols-1].reshape(rows/bins, bins)
MTKinesin = data[0:rows, cols-3:cols-2].reshape(rows/bins, bins)
total = np.add(Kinesin, MTKinesinATP)
total = np.add(total, MTKinesin)
print np.mean(total, axis=0, dtype=np.float64).astype(int)
#print "Kinesin", np.mean(Kinesin, axis=0, dtype=np.float64).astype(int)
#print "MTKinesin", np.mean(MTKinesin, axis=0, dtype=np.float64).astype(int)
#print "MTKinesinATP", np.mean(MTKinesinATP, axis=0, dtype=np.float64).astype(int)
