import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np

def get_mean(file):
  data = np.loadtxt(file, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  return data[rows-1, cols-2]-data[rows-1, cols-1]

def load_data(file):
  loaddata = np.loadtxt(file, delimiter=",", dtype=str)
  rows, cols = loaddata.shape
  abs_min = loaddata[0][0]
  data = loaddata[1:rows, 1:cols].astype(float)
  row_labels = loaddata[1:rows+1, 0:1].reshape(rows-1)
  col_labels = loaddata[0:1, 1:cols+1].reshape(cols-1)
  return data, row_labels, col_labels, abs_min

def save_data(file, data, row_labels, col_labels, abs_min):
  rows, cols = data.shape
  savedata = np.zeros((rows+1, cols+1)).astype(str)
  savedata[0][0] = abs_min
  savedata[1:rows+1, 1:cols+1] = data.astype(str)
  savedata[1:rows+1, 0:1] = row_labels.reshape(savedata[1:rows+1, 0:1].shape)
  savedata[0:1, 1:cols+1] = col_labels.reshape(savedata[0:1, 1:cols+1].shape)
  np.savetxt(file, savedata, delimiter=",", fmt="%s")

def show_values(pc, fmt="%.1e", **kw):
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
  vdelta = float('inf')
  for i in range(len(vals)-1):
    if (vals[i+1] > vals[i] and vals[i+1] - vals[i] < vdelta):
      vdelta = vals[i+1]-vals[i]

  rows, rcols = row_matrix.shape
  V0 = row_matrix[0:rows, 0:1]
  if(rcols > 1):
    V1 = row_matrix[0:rows, 1:2]

  rows, ccols = col_matrix.shape
  V2 = col_matrix[0:rows, 0:1]
  V2 = np.transpose(V2)
  if(ccols > 1):
    V3 = col_matrix[0:rows, 1:2]
    V3 = np.transpose(V3)

  #cax = divider.append_axes("left", size="20%", pad=0.05)
  #rect [left, bottom, width, height]
  #ax1 = fig.add_axes([0.80, 0.05, 0.05, 0.8])
  #cmap = mpl.cm.YlOrRd
  #cmap = mpl.cm.YlOrBr
  #cmap = mpl.cm.Reds
  #cmap = mpl.cm.Oranges
  #cmap = mpl.cm.OrRd
  cmap = mpl.cm.YlGn
  bar_width = 0.03
  padding = 0
  #ax1 = fig.add_axes(cax)
  box = ax.get_position()

  ax1 = fig.add_axes([box.x0-(bar_width+padding), box.y0, bar_width,
    box.height])
  heatmap = ax1.pcolor(V1, cmap=cmap, edgecolors='k')
  #ax1.set_axis_off()
  ax1.xaxis.tick_top()
  ax1.invert_yaxis()
  #put major ticks at the middle of each cell
  ax1.set_xticks(np.arange(row_matrix.shape[1]) + 0.5, minor=False)
  ax1.set_xticklabels(['ratchet'])
  ax1.set_yticklabels([])
  major_ticks = np.arange(0, 37, 6)
  ax1.set_yticks(major_ticks)
  show_values(heatmap, fmt="%d")
  plt.axis("tight")

  if(rcols > 1):
    ax0 = fig.add_axes([box.x0-(bar_width*2+padding), box.y0, bar_width,
      box.height])
    heatmap = ax0.pcolor(V0, cmap=cmap, edgecolors='k')
    ax0.xaxis.tick_top()
    ax0.invert_yaxis()
    ax0.set_xticks(np.arange(row_matrix.shape[1]) + 0.5, minor=False)
    ax0.set_xticklabels(['space'])
    ax0.set_yticklabels([])
    major_ticks = np.arange(0, 37, 6)
    ax0.set_yticks(major_ticks)
    show_values(heatmap, fmt="%.1e")
    plt.axis("tight")

  ax2 = fig.add_axes([box.x0, box.y0+box.height+padding, box.width,
    bar_width*1.5])
  heatmap = ax2.pcolor(V2, cmap=cmap, edgecolors='k')
  ax2.set_yticks(np.arange(col_matrix.shape[1]) + 0.5, minor=False)
  ax2.set_yticklabels(['p'])
  ax2.set_xticklabels([])
  ax2.set_xticks(major_ticks)
  show_values(heatmap, fmt="%.2f")
  plt.axis("tight")

  if(ccols > 1):
    ax3 = fig.add_axes([box.x0, box.y0+box.height*2+padding, box.width,
      bar_width*1.5])
    heatmap = ax2.pcolor(V3, cmap=cmap, edgecolors='k')
    ax3.set_yticks(np.arange(col_matrix.shape[1]) + 0.5, minor=False)
    ax3.set_yticklabels(['V2'])
    ax3.set_xticklabels([])
    ax3.set_xticks(major_ticks)
    show_values(heatmap, fmt="%.2f")
    plt.axis("tight")

def plot_figure(data, row_labels, col_labels, abs_min):
  rows, cols = data.shape
  fig, ax = plt.subplots()
  #heatmap = ax.pcolormesh(data, cmap=plt.cm.YlOrBr, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.hot)
  #heatmap = ax.pcolor(data, cmap=plt.cm.afmhot, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.gist_heat, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.gist_heat, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.Oranges, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=0.8)
  heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
  #heatmap = ax.pcolor(data)
  # put the major ticks at the middle of each cell
  #ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
  #ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
  plt.gca().set_xlim((0, cols))
  plt.gca().set_ylim((0, rows))
  show_values(heatmap, fmt="%d")
  #divider = make_axes_locatable(ax)
  #cax = divider.append_axes("right", size="5%", pad=0.05)
  #cbar = plt.colorbar(heatmap, cax)
  box = ax.get_position()
  padding = 0.005
  bar_width = 0.03
  #cax = fig.add_axes([box.x0+box.width+padding, box.y0, bar_width, box.height])
  cax = fig.add_axes([box.x0, box.y0-bar_width-padding, box.width, bar_width])
  #rect [left, bottom, width, height]
  cbar = plt.colorbar(heatmap, cax=cax, orientation='horizontal')
  cbar.ax.get_xaxis().set_ticks([])
  vmin, vmax = cbar.get_clim()
  major_ticks = np.arange(vmin, vmax+1, (vmax-vmin)/4.0).astype(int)
  for j, lab in enumerate(major_ticks):
    color = np.array(heatmap.get_cmap()(major_ticks[j]/vmax))
    if np.all(color[:3] > 0.5):
      color = (0.0, 0.0, 0.0)
    else:
      color = (1.0, 1.0, 1.0)
    pos = (2*j)/8.0
    ha = 'center'
    if(j == 0):
      pos = (2*j + 0.02)/8.0
      ha = 'left'
      lab = '%d (%d)' %(lab, int(float(abs_min)))
    elif(j == len(major_ticks)-1):
      pos = (2*j - 0.02)/8.0
      ha = 'right'
    cbar.ax.text(pos, .5, lab, ha=ha, va='center', color=color)
  #cbar.ax.get_xaxis().labelpad = 15
  #cbar.ax.set_xlabel('%% higher than the lowest kinesin concentration (%d) at tip' %int(float(abs_min)))
  ax.set_axis_off()
  #ax.set_aspect("equal")
  # want a more natural, table-like display
  ax.set_yticklabels([])
  ax.set_xticklabels([])
  for tic in ax.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
  for tic in ax.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
  ax.invert_yaxis()
  #ax.xaxis.tick_top()
  plt.xticks(rotation=90)
  plot_colorbars(row_labels, col_labels, fig, ax)
  plt.show()


def initialize():
  filenames = glob.glob("collision_*.csv")
  #filenames = glob.glob("his_1e-01_5e-02_1e-01_5e-02_n0.csv")
  filename = filenames[0]
  startTime = 1
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
  for file in filenames:
    vals = np.asarray(file.split("_"))
    vals = (vals[1:len(vals)-1]).astype(float)
    row = labels[0].index(vals[0])+1
    for i in range(row_head_size-1):
      row = row+(labels[i+1].index(vals[i+1]))*len(labels[i])
    col = labels[row_head_size].index(vals[row_head_size])+1
    for i in range(row_head_size, len(labels)-1):
      col = col+(labels[i+1].index(vals[i+1]))*len(labels[i])
    row_labels[row-1] = "%.2e %.2e" %(vals[0], vals[1])
    col_labels[col-1] = "%.2e" %(vals[2])
    mean = get_mean(file)
    data[row-1][col-1] = mean
  #convert to percentage of lowest value
  #abs_min = max(np.amin(data), 1.0)
  abs_min = np.amin(data)
  #data = np.divide(np.subtract(data, abs_min), abs_min/100.0)
  return data, row_labels, col_labels, abs_min

file = "saved_data.csv"
load = 1
if(load):
  data, row_labels, col_labels, abs_min = load_data(file)
else:
  filenames, labels, start_row, bins = initialize()
  data, row_labels, col_labels, abs_min = get_data(filenames, labels, start_row, bins)
  save_data(file, data, row_labels, col_labels, abs_min)
plot_figure(data, row_labels, col_labels, abs_min)

