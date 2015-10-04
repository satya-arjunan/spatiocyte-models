import numpy as np
import sys
import math

def get_mean(file, start_row, bins):
  data = np.loadtxt(file, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  #meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  #meanCols = [cols-1]#, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  meanCols = [cols-1, cols-2, cols-3, cols-4, cols-5]
  total = np.zeros(bins)
  for i in meanCols:
    total = np.add(total, data[0:rows, i:i+1].reshape(rows/bins, bins))
  return np.mean(total, axis=0)#.astype(int)


filename = "histogram.csv"
if(len(sys.argv) == 2):
  filename = sys.argv[1]

data = np.loadtxt(filename, delimiter=',', skiprows=1)
bins = 0
initTime = float(data[0][0])
for row in data:
  if(row[0] == initTime): 
    bins = bins+1
logInterval = data[bins][0]-initTime
startTime = 1
startRow = int(np.ceil((startTime-initTime)/logInterval))*bins
print "bins:", bins

print get_mean(filename, startRow, bins)
