import numpy as np
import matplotlib.pyplot as plt
import glob

labelFontSize = 18
tickFontSize = 18
legendFontSize = 18
lineFontSize = 18
lines = ['-', '-', '-', '-']
colors = ['r', 'g', 'b', 'y', 'c', 'k']
legendTitles = ['7um Neurite 1', '7um Neurite 2', '7um Neurite 3', '7um Neurite 4']

def get_bins(file, start_time, end_time):
  data = np.loadtxt(file, delimiter=',', skiprows=1)
  bins = 0
  initTime = float(data[0][0])
  for row in data:
    if(row[0] == initTime):
      bins = bins+1
  logInterval = data[bins][0]-initTime
  start_row = int(np.ceil((start_time-initTime)/logInterval))*bins
  drows = int((end_time-start_time)/logInterval*bins)
  return bins, start_row, drows

def initialize(start_time, end_time, bin_no):
  filenames = sorted(glob.glob("histogram_*.csv"))
  fig, ax = plt.subplots()
  for file in filenames:
    bins, start_row, drows = get_bins(file, start_time, end_time)
    data = np.loadtxt(file, delimiter=",", skiprows=start_row+1)
    rows,cols = data.shape
    xcol = 0 #time
    ycols = [cols-5, cols-4, cols-3, cols-2, cols-1]
    x = np.divide(data[0:drows, xcol:xcol+1].reshape(drows/bins, bins), 3600.0)
    y = np.zeros((drows/bins, 1))
    for i in ycols:
      tmp = data[0:drows, i:i+1].reshape(drows/bins, bins)[:, bin_no-1:bin_no]
      y = np.add(y, tmp)
    ax.plot(x, y)
  plt.show()

initialize(1000, 1000+3600*10, -1)
