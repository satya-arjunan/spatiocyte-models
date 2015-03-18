import glob
import numpy as np

filenames = glob.glob("HistogramCooperativity_*.csv")
#filenames = glob.glob("HistogramCooperativity_7.500000e-06_1.000000e+00_5.000000e-04_1.000000e+03.csv")

bins = 3
end_rows = 50
max_diff = 1
max_file = ""

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
  simple = simple[rows-end_rows:rows] #only get the last 50 rows
  ave = np.mean(simple, axis=0) #average along the column
  if(ave[2] > 10 and ave[2] > ave[0] and ave[2]-ave[0] > 15):
    if(ave[2]-ave[0] > max_diff):
      print "\n"
      print filenames[i],ave[2]-ave[0], ave
      print simple[40:50]

  
