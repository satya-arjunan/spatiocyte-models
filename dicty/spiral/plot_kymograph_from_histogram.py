import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

fontsize = 20
cdict1 = {'red':   ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0))
        }
cdict2 = {'red':   ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0)),

         'blue':  ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0))
        }
cdict3 = {'red':   ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0)),

         'blue':  ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0))
        }

red_black = LinearSegmentedColormap('RedBlack', cdict1)
plt.register_cmap(cmap=red_black)
green_black = LinearSegmentedColormap('GreenBlack', cdict2)
plt.register_cmap(cmap=green_black)
white_black = LinearSegmentedColormap('WhiteBlack', cdict3)
plt.register_cmap(cmap=white_black)

def get_mean(file, start_row, bins):
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
  bins = int(loaddata[rows-1][0])
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

def plot_colorbars(row_labels, col_labels, fig, ax):
  V1 = row_labels.reshape(len(row_labels), 1)
  V2 = col_labels.reshape(len(col_labels), 1)

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
  #ax1.set_xticklabels(['Ratchet'])
  ax1.set_xticklabels([])
  ax1.set_yticklabels([])
  ax1.set_ylabel('Plus-end biased walk', fontsize=fontsize)
  ax1.yaxis.set_label_position('right')
  #major_ticks = np.arange(0, 37, 6)
  #ax1.set_yticks(major_ticks)
  #show_values_binary(heatmap, minus=0, size=fontsize)
  plt.axis("tight")

  cmap = mpl.cm.YlOrBr
  ax2 = fig.add_axes([box.x0, box.y0+box.height+padding, box.width,
    bar_height])
  heatmap = ax2.pcolor(V2, cmap=cmap, edgecolors='k')
  #ax2.set_yticklabels(['p'])
  ax2.set_yticklabels([])
  ax2.set_xticklabels([])
  ax2.set_xlabel("Kinesin-MT binding probability", fontsize=fontsize)
  ax2.xaxis.set_label_position('top')
  #ax2.set_xticks(major_ticks)
  #show_values(heatmap, fmt="%.2f", size=fontsize)
  plt.axis("tight")

def plot_legend(heatmap, fig, ax):
  box = ax.get_position()
  padding = 0.005
  bar_width = 0.04
  #cax = fig.add_axes([box.x0+box.width+padding, box.y0, bar_width, box.height])
  cax = fig.add_axes([box.x0, box.y0-bar_width-padding, box.width, bar_width])
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
  label = '%% of max cytosolic kinesin concentration at bin #%d' %plot_bin
  cbar.ax.set_xlabel(label, size=fontsize)

def plot_figure(data, row_labels, col_labels, abs_val, plot_bin):
  rows, cols = data.shape
  fig, ax = plt.subplots()
  #heatmap = ax.pcolormesh(data, cmap=plt.cm.YlOrBr, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.hot)
  #heatmap = ax.pcolor(data, cmap=plt.cm.afmhot, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.gist_heat, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.gist_heat, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.Oranges, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=0.8)
  #heatmap = ax.pcolor(data, cmap=plt.cm.Blues, vmax=abs_val*0.7)
  #heatmap = ax.pcolor(data, cmap=red_black, vmax=abs_val*0.7)
  #heatmap = ax.pcolor(data, cmap=green_black, vmax=abs_val*0.7)
  heatmap = ax.pcolor(data, cmap=white_black, vmax=abs_val*0.7)
  #heatmap = ax.pcolor(data)
  # put the major ticks at the middle of each cell
  #ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
  #ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
  plt.gca().set_xlim((0, cols))
  plt.gca().set_ylim((0, rows))
  #plot_legend(heatmap, fig, ax)

  #show_values(heatmap, fmt="%d", size=fontsize)
  #divider = make_axes_locatable(ax)
  #cax = divider.append_axes("right", size="5%", pad=0.05)
  #cbar = plt.colorbar(heatmap, cax)
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
  #plot_colorbars(row_labels, col_labels, fig, ax)
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
  meanCols = [cols-2]# cols-2, cols-3, cols-4, cols-5]
  bins = len(col_labels)
  dataset = np.empty([len(meanCols), rows/bins, bins])
  for i in range(len(meanCols)):
    dataset[i] = data[0:rows, meanCols[i]:meanCols[i]+1].reshape(rows/bins,
        bins)
  abs_val = np.amax(dataset)
  return dataset, abs_val

file = "saved_histogram_data.csv"
load = 0
plot_bin = 0
start_time = 0
if(load):
  data, row_labels, col_labels, abs_val = load_data(file)
else:
  filename, start_row, row_labels, col_labels = initialize(start_time)
  data, abs_val = get_data(filename, start_row, row_labels, col_labels)
  save_data(file, data, row_labels, col_labels, abs_val)
plot_figure(data[plot_bin], row_labels, col_labels, abs_val, plot_bin)
