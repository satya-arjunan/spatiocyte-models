import glob
import numpy as np

filenames = glob.glob("HistogramCooperativity_7*.csv")
print filenames

bins = 3

for i in range(len(filenames)):
  f = filenames[i].split("_")
  K1 = float(f[1])
  K6 = float(f[2])
  K7 = float(f[3])
  K8 = float(f[4].strip(".csv"))
  data = np.loadtxt(filenames[i], skiprows=1, delimiter=",")
  rows,cols = data.shape
  simple = data[0:rows, cols-1:cols].reshape(rows/bins, bins)
  rows,cols = simple.shape
  ave = np.mean(simple[rows-100:rows], axis=0)
  if(ave[0] < ave[2]):
    print ave[2]/ave[0], ave
  
