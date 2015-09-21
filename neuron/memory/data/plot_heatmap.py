import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np

def get_mean(file, start_row, bins):
  data = np.loadtxt(file, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  #meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  meanCols = [cols-1]#, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  total = np.zeros(cols)
  for i in meanCols:
    total = np.add(total, data[0:rows, i:i+1].reshape(rows/bins, bins))
  return np.mean(total, axis=0)#.astype(int)

def load_data(file):
  loaddata = np.loadtxt(file, delimiter=",", dtype=str)
  rows, cols = loaddata.shape
  data = loaddata[1:rows, 1:cols].astype(float)
  row_labels = loaddata[1:rows+1, 0:1].reshape(rows-1)
  col_labels = loaddata[0:1, 1:cols+1].reshape(cols-1)
  return data, row_labels, col_labels

def save_data(file, data, row_labels, col_labels):
  rows, cols = data.shape
  savedata = np.zeros((rows+1, cols+1)).astype(str)
  savedata[1:rows+1, 1:cols+1] = data.astype(str)
  savedata[1:rows+1, 0:1] = row_labels.reshape(savedata[1:rows+1, 0:1].shape)
  savedata[0:1, 1:cols+1] = col_labels.reshape(savedata[0:1, 1:cols+1].shape)
  np.savetxt(file, savedata, delimiter=",", fmt="%s")

def show_values(pc, fmt="%.2f", **kw):
  from itertools import izip
  pc.update_scalarmappable()
  ax = pc.get_axes()
  for p, color, value in izip(pc.get_paths(), pc.get_facecolors(), pc.get_array()):
    x, y = p.vertices[:-2, :].mean(0)
    if np.all(color[:3] > 0.5):
      color = (0.0, 0.0, 0.0)
    else:
      color = (1.0, 1.0, 1.0)
    ax.text(x, y, fmt % value, ha="center", va="center", color=color, **kw)
  #for y in range(row_matrix.shape[0]):
  #  for x in range(row_matrix.shape[1]):
  #    plt.text(x + 0.5, y + 0.5, '%.2f' % row_matrix[y, x],
  #        horizontalalignment='center', verticalalignment='center', rotation=0)

def plot_colorbars(row_labels, col_labels, fig, ax):
  vmin = float('inf')
  vmax = -1.0
  vdelta = float('inf')
  vals = []
  col_matrix = np.zeros((len(col_labels), len(col_labels[0].split(" "))))
  for i in range(len(col_labels)):
    labels = col_labels[i].split(" ")
    for j in range(len(labels)):
      vals.append(float(labels[j]))
      col_matrix[i, j] = float(labels[j])
  row_matrix = np.zeros((len(row_labels), len(row_labels[0].split(" "))))
  for i in range(len(row_labels)):
    labels = row_labels[i].split(" ")
    for j in range(len(labels)):
      vals.append(float(labels[j]))
      row_matrix[i, j] = float(labels[j])
  vals = np.array(vals)
  vmax = np.amax(vals)
  vmin = np.amin(vals)
  for i in range(len(vals)-1):
    if (vals[i+1] > vals[i] and vals[i+1] - vals[i] < vdelta):
      vdelta = vals[i+1]-vals[i]
  print col_matrix.shape
  print row_matrix.shape

  box = ax.get_position()
  #cax = divider.append_axes("left", size="20%", pad=0.05)
  #rect [left, bottom, width, height]
  #ax1 = fig.add_axes([0.80, 0.05, 0.05, 0.8])
  #cmap = mpl.cm.YlOrRd
  #cmap = mpl.cm.YlOrBr
  #cmap = mpl.cm.Reds
  #cmap = mpl.cm.Oranges
  #cmap = mpl.cm.OrRd
  cmap = mpl.cm.YlGn
  bar_width = 0.04
  bar_space = 0
  i = 0
  #ax1 = fig.add_axes(cax)
  ax1 = fig.add_axes([box.x0-(bar_width+bar_space), box.y0, bar_width,
    box.height])
  heatmap = ax1.pcolor(row_matrix, cmap=cmap, vmin=vmin, vmax=vmax*1.5,
      edgecolors='k')
  #for y in range(row_matrix.shape[0]):
  #  for x in range(row_matrix.shape[1]):
  #    plt.text(x + 0.5, y + 0.5, '%.2f' % row_matrix[y, x],
  #        horizontalalignment='center', verticalalignment='center', rotation=0)
  ax1.set_axis_off()
  ax1.invert_yaxis()
  show_values(heatmap)
  plt.axis("tight")


  col_matrix = np.transpose(col_matrix)
  ax2 = fig.add_axes([box.x0, box.y0+box.height+bar_space, box.width,
    bar_width*1.5])
  heatmap = ax2.pcolor(col_matrix, cmap=cmap, vmin=vmin, vmax=vmax*1.5,
      edgecolors='k')
  #for y in range(col_matrix.shape[0]):
  #  for x in range(col_matrix.shape[1]):
  #    plt.text(x + 0.5, y + 0.5, '%.2f' % col_matrix[y, x],
  #        horizontalalignment='center', verticalalignment='center', rotation=90)
  ax2.set_axis_off()
  ax2.invert_yaxis()
  show_values(heatmap)
  plt.axis("tight")

def plot_figure(data, row_labels, col_labels):
  rows, cols = data.shape
  fig, ax = plt.subplots()
  #heatmap = ax.pcolormesh(data, cmap=plt.cm.YlOrBr, alpha=0.8)
  heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=0.8)
  #heatmap = ax.pcolormesh(data)
  #heatmap = ax.pcolor(data)
  # put the major ticks at the middle of each cell
  #ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
  #ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
  plt.gca().set_xlim((0, cols))
  plt.gca().set_ylim((0, rows))
  #annotate
  #for y in range(data.shape[0]):
  #  for x in range(data.shape[1]):
  #    plt.text(x + 0.5, y + 0.5, '%d' % int(data[y, x]),
  #        horizontalalignment='center', verticalalignment='center', rotation=90)
  show_values(heatmap, fmt="%d")
  #divider = make_axes_locatable(ax)
  #cax = divider.append_axes("right", size="5%", pad=0.05)
  #cbar = plt.colorbar(heatmap, cax)
  cbar = plt.colorbar(heatmap)
  ax.set_axis_off()
  # want a more natural, table-like display
  ax.invert_yaxis()
  #ax.xaxis.tick_top()
  #ax.set_xticklabels(col_labels, minor=False)
  #ax.set_yticklabels(row_labels, minor=False)
  plt.xticks(rotation=90)
  #ax.grid(False)
  ## Turn off all the ticks
  #ax = plt.gca()
  #for t in ax.xaxis.get_major_ticks():
  #    t.tick1On = False
  #    t.tick2On = False
  #for t in ax.yaxis.get_major_ticks():
  #    t.tick1On = False
  #    t.tick2On = False
  plot_colorbars(row_labels, col_labels, fig, ax)
  print ax.get_position()
  plt.show()

def initialize():
  filenames = glob.glob("his_*.csv")
  #filenames = glob.glob("his_1e-01_5e-02_1e-01_5e-02_n0.csv")
  filename = filenames[0]
  startTime = 400
  data = np.loadtxt(filename, delimiter=',', skiprows=1)
  bins = 0
  initTime = float(data[0][0])
  for row in data:
    if(row[0] == initTime):
      bins = bins+1
  logInterval = data[bins][0]-initTime
  start_row = int(np.ceil((startTime-initTime)/logInterval))*bins
  name = filename.split("_")
  name = name[1:len(name)-1]
  labels = []
  for i in name:
    labels.append(([float(i)]))
  for file in filenames:
    vals = file.split("_")
    vals = vals[1:len(vals)-1]
    for i in range(len(vals)):
      if float(vals[i]) not in labels[i]:
        labels[i].append(float(vals[i]))
  for i in range(len(labels)):
    labels[i].sort()
  return filenames, labels, start_row, bins

def get_data(filenames, labels, start_row, bins):
  row_head_size = len(labels)-len(labels)/2
  rows = len(labels[0])
  cols = len(labels[row_head_size])
  for i in range(row_head_size-1):
    rows = rows*len(labels[i+1])
  for i in range(row_head_size, len(labels)-1):
    cols = cols*len(labels[i+1])
  data = np.zeros((rows, cols))
  row_labels = np.zeros(rows).astype(str)
  col_labels = np.zeros(cols).astype(str)
  min_mean = float('inf')
  for file in filenames:
    vals = np.asarray(file.split("_"))
    vals = (vals[1:len(vals)-1]).astype(float)
    row = labels[0].index(vals[0])+1
    for i in range(row_head_size-1):
      row = row+(labels[i+1].index(vals[i+1]))*len(labels[i])
    col = labels[row_head_size].index(vals[row_head_size])+1
    for i in range(row_head_size, len(labels)-1):
      col = col+(labels[i+1].index(vals[i+1]))*len(labels[i])
    row_labels[row-1] = "%.2f %.2f" %(vals[0], vals[1])
    col_labels[col-1] = "%.2f %.2f" %(vals[2], vals[3])
    mean = get_mean(file, start_row, bins)[bins-1]
    data[row-1][col-1] = mean
    if mean < min_mean:
      min_mean = mean

  #convert to percentage of lowest value
  data = np.divide(np.subtract(data, min_mean), min_mean/100.0)
  return data, row_labels, col_labels

file = "saved_data.csv"
data, row_labels, col_labels = load_data(file)
#filenames, labels, start_row, bins = initialize()
#data, row_labels, col_labels = get_data(filenames, labels, start_row, bins)
#save_data(file, data, row_labels, col_labels)
plot_figure(data, row_labels, col_labels)
