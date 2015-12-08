import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

fontsize = 20

def plot_figure(data, row_labels, col_labels, start_time, end_time):
  bin_id = 4
  logInterval = row_labels[1]-row_labels[0]
  timePoints = (end_time-start_time)/logInterval
  dim, rows, cols = data.shape
  x = data[0:1, 0:timePoints, bin_id][0]
  x = np.add(x, data[2:3, 0:timePoints, bin_id][0])
  max_x = np.amax(x)
  x = x/max_x
  y = data[1:2, 0:timePoints, bin_id][0]
  max_y = np.amax(y)
  y = y/max_y
  z = np.arange(len(x))*logInterval
  print z
  fig, ax = plt.subplots()
  ax.plot(z, x, 'g')
  ax.plot(z, y, 'r')
  plt.show()

def initialize(startTime):
  filename = "original.csv"
  data = np.loadtxt(filename, delimiter=',', skiprows=1)
  bins = 0
  initTime = float(data[0][0])
  for row in data:
    if(row[0] == initTime):
      bins = bins+1
  if (initTime < 1e-7):
    initTime = 0
  logInterval = data[bins][0]-initTime
  binInterval = float(np.loadtxt(filename, delimiter=',', dtype=str)[0][1])
  start_row = int(np.ceil((startTime-initTime)/logInterval))*bins
  rows = (len(data)-start_row)/bins
  row_labels = np.empty([rows])
  col_labels = np.empty([bins])
  for i in range(rows):
    row_labels[i] = startTime+i*logInterval
  for i in range(bins):
    col_labels[i] = i*binInterval
  return filename, start_row, row_labels, col_labels

def get_data(filename, start_row, row_labels, col_labels):
  data = np.loadtxt(filename, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  #meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  #meanCols = [cols-1]#, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  #meanCols = [cols-1]# cols-2, cols-3, cols-4, cols-5]
  meanCols = [cols-2, cols-1, cols-4]# cols-2, cols-3, cols-4, cols-5]
  bins = len(col_labels)
  dataset = np.empty([len(meanCols), rows/bins, bins])
  for i in range(len(meanCols)):
    dataset[i] = data[0:rows, meanCols[i]:meanCols[i]+1].reshape(rows/bins,
        bins)
  abs_val = np.amax(dataset)
  return dataset, abs_val

start_time = 0
end_time = 2000
filename, start_row, row_labels, col_labels = initialize(start_time)
data, abs_val = get_data(filename, start_row, row_labels, col_labels)
plot_figure(data, row_labels, col_labels, start_time, end_time)
