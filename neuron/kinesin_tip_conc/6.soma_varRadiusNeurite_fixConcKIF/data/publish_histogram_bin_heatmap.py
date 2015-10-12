import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np

fontsize = 20

def get_bins(file, start_time):
  data = np.loadtxt(file, delimiter=',', skiprows=1)
  bins = 0
  initTime = float(data[0][0])
  for row in data:
    if(row[0] == initTime):
      bins = bins+1
  logInterval = data[bins][0]-initTime
  start_row = int(np.ceil((start_time-initTime)/logInterval))*bins
  return bins, start_row

def get_mean(file, start_time):
  bins, start_row = get_bins(file, start_time)
  data = np.loadtxt(file, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  #meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  #meanCols = [cols-1]#, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  meanCols = [cols-1]# cols-2, cols-3, cols-4, cols-5]
  total = np.zeros(bins)
  for i in meanCols:
    total = np.add(total, data[0:rows, i:i+1].reshape(rows/bins, bins))
  return np.mean(total, axis=0)#.astype(int)

def load_data(file):
  loaddata = np.loadtxt(file, delimiter=",", dtype=str)
  rows, cols = loaddata.shape
  bins = 1
  nrows = (rows-1)/bins
  abs_val = loaddata[0][0]
  data = loaddata[1:rows, 1:cols].astype(float).reshape(bins, nrows, cols-1)
  row_labels = loaddata[1:nrows+1, 0:1].reshape(nrows)
  col_labels = loaddata[0:1, 1:cols+1].reshape(cols-1)
  return data, row_labels, col_labels, abs_val

def save_data(file, data, row_labels, col_labels, abs_val):
  bins, rows, cols = data.shape
  nrows = bins*rows
  data = data.reshape((nrows, cols))
  savedata = np.zeros((nrows+1, cols+1)).astype(str)
  savedata[0][0] = abs_val
  if(bins != 1):
    savedata[nrows][0] = bins
  savedata[1:nrows+1, 1:cols+1] = data.astype(str)
  savedata[1:rows+1, 0:1] = row_labels.reshape(savedata[1:rows+1, 0:1].shape)
  savedata[0:1, 1:cols+1] = col_labels.reshape(savedata[0:1, 1:cols+1].shape)
  np.savetxt(file, savedata, delimiter=",", fmt="%s")

def show_values_binary(pc, minus, fmt="%s", **kw):
  from itertools import izip
  pc.update_scalarmappable()
  ax = pc.get_axes()
  for p, color, value in izip(pc.get_paths(), pc.get_facecolors(),
      pc.get_array()):
    x, y = p.vertices[:-2, :].mean(0)
    if np.all(color[:3] > 0.5):
      color = (0.0, 0.0, 0.0)
    else:
      color = (1.0, 1.0, 1.0)
    if (value == minus):
      value = '-'
      #value = r'${-}$'
      #value = r'$\textendash$'
    else:
      value = '+'
    ax.text(x, y, fmt % value, ha="center", va="center", color=color, **kw)

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
    if fmt=="%d":
      value = int(round(value))
    ax.text(x, y, fmt % value, ha="center", va="center", color=color, **kw)
  #for y in range(row_matrix.shape[0]):
  #  for x in range(row_matrix.shape[1]):
  #    plt.text(x + 0.5, y + 0.5, '%.2f' % row_matrix[y, x],
  #        horizontalalignment='center', verticalalignment='center', rotation=0)

def plot_headers(row_labels, col_labels, fig, ax):
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
  #V0 = row_matrix[0:rows, 0:1]
  if(rcols > 1):
    V1 = row_matrix[0:rows, 1:2]

  rows, ccols = col_matrix.shape
  V2 = col_matrix[0:rows, 0:1]
  V2 = np.transpose(V2)
  if(ccols > 1):
    V3 = np.add(col_matrix[0:rows, 1:2], 1.0)
    V3 = np.transpose(V3)

  #cax = divider.append_axes("left", size="20%", pad=0.05)
  #rect [left, bottom, width, height]
  #ax1 = fig.add_axes([0.80, 0.05, 0.05, 0.8])
  #cmap = mpl.cm.YlOrRd
  #cmap = mpl.cm.YlOrBr
  #cmap = mpl.cm.Reds
  #cmap = mpl.cm.Oranges
  bar_width = 0.05
  bar_height = 0.04
  padding = 0
  #ax1 = fig.add_axes(cax)
  box = ax.get_position()

  #cmap = mpl.cm.YlGn
  cmap = mpl.cm.YlOrBr
  ax1 = fig.add_axes([box.x1, box.y0, bar_width, box.height])
  heatmap = ax1.pcolor(V1, cmap=cmap, edgecolors='k')
  #ax1.set_axis_off()
  ax1.xaxis.tick_top()
  ax1.invert_yaxis()
  #put major ticks at the middle of each cell
  ax1.set_xticks(np.arange(row_matrix.shape[1]) + 0.5, minor=False)
  #ax1.set_xticklabels(['Ratchet'])
  ax1.set_xticklabels([])
  ax1.set_yticklabels([])
  ax1.set_ylabel('Plus-end biased walk', fontsize=fontsize)
  ax1.yaxis.set_label_position('right')
  #major_ticks = np.arange(0, 37, 6)
  #ax1.set_yticks(major_ticks)
  show_values_binary(heatmap, minus=0, size=fontsize)
  plt.axis("tight")

  if(rcols > 1):
    cmap = mpl.cm.YlOrBr
    ax0 = fig.add_axes([box.x0-(bar_width+padding), box.y0, bar_width,
      box.height])
    heatmap = ax0.pcolor(V0, cmap=cmap, edgecolors='k')
    ax0.xaxis.tick_top()
    ax0.invert_yaxis()
    ax0.set_xticks(np.arange(row_matrix.shape[1]) + 0.5, minor=False)
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])
    ax0.set_ylabel('% radius expansion of neurite #4',
        fontsize=fontsize)
    #major_ticks = np.arange(0, 37, 6)
    #ax0.set_yticks(major_ticks)
    show_values(heatmap, fmt="%d", size=fontsize)
    plt.axis("tight")

  cmap = mpl.cm.YlOrBr
  ax2 = fig.add_axes([box.x0, box.y0+box.height+padding, box.width,
    bar_height])
  heatmap = ax2.pcolor(V2, cmap=cmap, edgecolors='k')
  ax2.set_yticks(np.arange(col_matrix.shape[1]) + 0.5, minor=False)
  #ax2.set_yticklabels(['p'])
  ax2.set_yticklabels([])
  ax2.set_xticklabels([])
  ax2.set_xlabel("Kinesin-MT binding probability", fontsize=fontsize)
  ax2.xaxis.set_label_position('top')
  #ax2.set_xticks(major_ticks)
  show_values(heatmap, fmt="%.2f", size=fontsize)
  plt.axis("tight")

  if(ccols > 1):
    cmap = mpl.cm.YlOrBr
    ax3 = fig.add_axes([box.x0, box.y0-bar_height, box.width, bar_height])
    heatmap = ax3.pcolor(V3, cmap=cmap, edgecolors='k')
    ax3.set_yticks(np.arange(col_matrix.shape[1]) + 0.5, minor=False)
    ax3.set_yticklabels([])
    ax3.set_xticklabels([])
    ax3.set_xlabel("Neurite #", fontsize=fontsize)
    ax3.xaxis.set_label_position('bottom')
    #ax3.set_xticks(major_ticks)
    show_values(heatmap, fmt="%d", size=fontsize)
    plt.axis("tight")

def plot_colorbar(fig, ax, heatmap):
  box = ax.get_position()
  padding = 0.01
  bar_height = 0.04
  cax = fig.add_axes([box.x0, box.y0-bar_height*2-padding, box.width,
    bar_height])
  #rect [left, bottom, width, height]
  cbar = plt.colorbar(heatmap, cax=cax, orientation='horizontal')
  cbar.ax.get_xaxis().set_ticks([])
  vmin, vmax = cbar.get_clim()
  major_ticks = np.arange(vmin, vmax+1, (vmax-vmin)/4.0).astype(int)
  for j, lab in enumerate(major_ticks):
    color = np.array(heatmap.get_cmap()(major_ticks[j]/vmax))
    if (color[0] > 0.5 and color[1] > 0.5 and color [2] > 0.5):
      color = (0.0, 0.0, 0.0)
    else:
      color = (1.0, 1.0, 1.0)
    pos = (2*j)/8.0
    ha = 'center'
    if(j == 0):
      pos = (2*j + 0.02)/8.0
      ha = 'left'
      #lab = '%d (%d)' %(lab, int(float(abs_val)))
    elif(j == len(major_ticks)-1):
      pos = (2*j - 0.02)/8.0
      ha = 'right'
    cbar.ax.text(pos, .5, lab, ha=ha, va='center', color=color, size=fontsize)
  #cbar.ax.get_xaxis().labelpad = 15
  #cbar.ax.set_xlabel('%% higher than the lowest kinesin concentration (%d) at tip' %int(float(abs_val)))
  label = '% of max cytosolic kinesin concentration at neurite tip'
  cbar.ax.set_xlabel(label, size=fontsize)

def plot_figure(data, row_labels, col_labels, abs_val):
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
  show_values(heatmap, fmt="%d", size=fontsize)
  #divider = make_axes_locatable(ax)
  #cax = divider.append_axes("right", size="5%", pad=0.05)
  #plot_colorbar(fig, ax, heatmap)
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
  plot_headers(row_labels, col_labels, fig, ax)
  plt.show()

def initialize():
  filenames = glob.glob("histogram_*.csv")
  #filenames = glob.glob("histogram_9_55_1.00_n0.csv")
  filename = filenames[0]
  name = filename.split("_")
  neurite = name[-1].split(".")[0].split("n")[-1]
  name = name[1:-1]
  name.append(neurite)
  labels = []
  for i in name:
    labels.append(([float(i)]))
  for file in filenames:
    vals = file.split("_")
    neurite = vals[-1].split(".")[0].split("n")[-1]
    vals = vals[1:-1]
    vals.append(neurite)
    for i in range(len(vals)):
      if float(vals[i]) not in labels[i]:
        labels[i].append(float(vals[i]))
  for i in range(len(labels)):
    labels[i].sort()
  return filenames, labels

def get_data(filenames, labels, start_time):
  row_head_size = len(labels)-len(labels)/2
  rows = len(labels[0])
  cols = len(labels[row_head_size])
  for i in range(row_head_size-1):
    rows = rows*len(labels[i+1])
  for i in range(row_head_size, len(labels)-1):
    cols = cols*len(labels[i+1])
  data = np.zeros((1, rows, cols))
  row_labels = np.zeros(rows).astype(str)
  col_labels = np.zeros(cols).astype(str)
  for file in filenames:
    vals = np.asarray(file.split("_"))
    neurite = vals[-1].split(".")[0].split("n")[-1]
    vals = (vals[1:-1]).astype(float)
    vals = np.append(vals, float(neurite))
    row = labels[0].index(vals[0])+1
    for i in range(row_head_size-1):
      row = row+(labels[i+1].index(vals[i+1]))*len(labels[i])
    col = labels[row_head_size].index(vals[row_head_size])+1
    for i in range(row_head_size, len(labels)-1):
      col = col+(labels[i+1].index(vals[i+1]))*len(labels[i])
    row_labels[row-1] = "%.4e %.4e" %(vals[0], vals[1])
    col_labels[col-1] = "%.4e %.4e" %(vals[2], vals[3])
    data[0:1, row-1:row, col-1:col] = get_mean(file, start_time)[-1]
  abs_val = np.amax(data)
  data = np.divide(data, abs_val/100.0)
  return data, row_labels, col_labels, abs_val

file = "saved_histogram_data.csv"
load = 0
start_time = 200
if(load):
  data, row_labels, col_labels, abs_val = load_data(file)
else:
  filenames, labels = initialize()
  data, row_labels, col_labels, abs_val = get_data(filenames, labels,
      start_time)
  save_data(file, data, row_labels, col_labels, abs_val)
plot_figure(data[0], row_labels, col_labels, abs_val)
