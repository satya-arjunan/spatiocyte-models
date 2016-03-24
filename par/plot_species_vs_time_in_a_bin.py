import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import csv

fontsize = 15 

def plot_figure(data, row_labels, col_labels, labels, start_time, end_time, bin_id):
  logInterval = row_labels[1]-row_labels[0]
  timePoints = (end_time-start_time)/logInterval
  dim, rows, cols = data.shape
  fig, ax = plt.subplots()
  for i in range(dim):
    x = data[i:i+1, 0:timePoints, bin_id][0]
    z = np.arange(len(x))*logInterval
    ax.plot(z, x, label=labels[i], linewidth=1.5)
  ax.grid(color='b', linestyle='--')
  leg = plt.legend(loc=0, labelspacing=0.2, handletextpad=0.2, fancybox=True)
  for t in leg.get_texts():
    t.set_fontsize(fontsize)   
  frame = leg.get_frame()
  frame.set_linewidth(None)
  frame.set_facecolor('0.95')
  frame.set_edgecolor('0.75')
  plt.ylabel("Density in Bin #%d (a.u.)" %bin_id, fontsize=fontsize)
  plt.xlabel('Time (s)', fontsize=fontsize)
  plt.xticks(fontsize=fontsize)
  plt.yticks(fontsize=fontsize)
  plt.show()

def get_headers(filename):
  f = open(filename, 'rb')
  reader = csv.reader(f)
  headers = reader.next()[2:]
  for i in range(len(headers)):
    headers[i] = headers[i].split(']')[0].strip('[')
    headers[i] = headers[i].split(':')[1] #remove path of species
  return headers

def initialize(startTime):
  filename = "original.csv"
  headers = get_headers(filename)
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
  return filename, start_row, row_labels, col_labels, headers

def get_data(filename, start_row, row_labels, col_labels, headers, species):
  data = np.loadtxt(filename, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  bins = len(col_labels)
  dataset = np.empty([len(species), rows/bins, bins])
  labels = []
  for i in range(len(species)):
    dataset[i] = data[0:rows, species[i]+2:species[i]+3].reshape(rows/bins,
        bins)
    labels.append(headers[species[i]])
  abs_val = np.amax(dataset)
  return dataset, abs_val, labels

start_time = 0
end_time = 2000
bin_id = 23
species = [1, 2]
filename, start_row, row_labels, col_labels, headers = initialize(start_time)
data, abs_val, labels = get_data(filename, start_row, row_labels, col_labels, headers, species)
plot_figure(data, row_labels, col_labels, labels, start_time, end_time, bin_id)
