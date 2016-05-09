import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import csv

fontsize = 15 
mpl.rcParams.update({'font.size': fontsize})
mpl.rcParams['figure.figsize'] = 10, 3

def plot_figure(data, row_labels, col_labels, labels, start_time, end_time, bin_id):
  colors = ['#0077FF', '#FF0000', '#00BB00', 'magenta']
  logInterval = row_labels[1]-row_labels[0]
  timePoints = (end_time-start_time)/logInterval
  dim, rows, cols = data.shape
  fig, ax = plt.subplots()
  for i in range(dim):
    x = data[i:i+1, 0:timePoints, bin_id][0]
    z = np.arange(len(x))*logInterval
    ax.plot(z, x, label='Rod '+str(int(labels[i])+1), color=colors[i],
        linewidth=4)
  #ax.grid(color='b', linestyle='--')
  #leg = plt.legend(loc=0, labelspacing=0.2, handletextpad=0.2, fancybox=True)
  #for t in leg.get_texts():
  #  t.set_fontsize(fontsize)   
  #frame = leg.get_frame()
  #frame.set_linewidth(None)
  #frame.set_facecolor('0.95')
  #frame.set_edgecolor('0.75')
  ax.yaxis.tick_right()
  plt.yticks(rotation=90)
  ax.yaxis.set_label_position("right")
  #plt.ylabel("Density in Bin #%d (a.u.)" %bin_id, fontsize=fontsize)
  #plt.xlabel('Time (s)', fontsize=fontsize)
  ax.get_xaxis().set_visible(False)
  plt.xticks(fontsize=fontsize)
  plt.yticks(fontsize=fontsize)
  plt.savefig('3rods_long_species_vs_time.pdf', bbox_inches='tight')
  plt.show()

def get_headers(filename):
  f = open(filename, 'rb')
  reader = csv.reader(f)
  headers = reader.next()[2:]
  for i in range(len(headers)):
    headers[i] = headers[i].split(']')[0].strip('[')
    headers[i] = headers[i].split(':')[1] #remove path of species
  return headers

def initialize(startTime, filename, n):
  filename = filename + str(n) + ".csv"
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
  return start_row, row_labels, col_labels, headers, logInterval

def get_data(filename, start_row, row_labels, col_labels, headers, species,
    rods):
  f = filename + str(rods[0]) + ".csv"
  data = np.loadtxt(f, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  bins = len(col_labels)
  dataset = np.zeros([len(rods), rows/bins, bins])
  labels = []
  abs_val = 0
  for i in range(len(species)):
    print headers[species[i]]
  for r in range(len(rods)):
    labels.append(str(rods[r]))
    f = filename + str(rods[r]) + ".csv"
    data = np.loadtxt(f, delimiter=",", skiprows=start_row+1)
    #sum the vals of all selected species
    for i in range(len(species)):
      dataset[r] = np.add(dataset[r], data[0:rows, 
        species[i]+2:species[i]+3].reshape(rows/bins, bins))
    max_val = np.amax(data[0:rows,
        species[i]+2:species[i]+3].reshape(rows/bins, bins))
    print max_val
    abs_val = max(abs_val, max_val)
  return dataset, abs_val, labels

start_time = 0
end_time = 2000
bin_id = 19
species = [3]
rods = [0, 1, 2]
filename = "histogram_0_55_1.00_n"
start_row, row_labels, col_labels, headers, logInterval = initialize(0, filename, rods[0])
data, abs_val, labels = get_data(filename, start_row, row_labels, col_labels, headers, species, rods)
plot_figure(data, row_labels, col_labels, labels, start_time, end_time, bin_id)
