import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
import csv
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

fontsize = 15
mpl.rcParams.update({'font.size': fontsize})
mpl.rcParams['figure.figsize'] = 5, 10

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
  heatmap = ax1.imshow(V1, cmap=cmap, edgecolors='k')
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
  heatmap = ax2.imshow(V2, cmap=cmap, edgecolors='k')
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

def plot_figure(data, row_labels, col_labels, abs_val, plot_bin, labels, time, logInterval):
  colors = ['#0077FF', '#FF0000', '#00FF00', 'magenta']
  cmaps = []
  for i in colors:
    cmaps.append(mpl.colors.LinearSegmentedColormap.from_list('m1',['black',i]))
  dim, rows, cols = data.shape
  vmax = np.amax(data)
  vmin = np.amin(data)
  fig, ax = plt.subplots()
  c = np.zeros([rows, cols, 4])
  for i in range(dim):
    c = np.add(c, cmaps[i]((data[i]-vmin)/(vmax-vmin)))
  c = np.clip(c, 0, 1)
  pc = ax.imshow(c, aspect='auto', interpolation='none')
  #ax.set_title(labels[0])
  fig.text(0.5, 0.04, 'Bin # along rod length', ha='center',
      fontsize=fontsize)
  fig.text(0.0, 0.5, 'Time (s)', va='center', rotation='vertical',
      fontsize=fontsize)
  #ax.add_patch(Rectangle((0.5, time/logInterval), cols-1, 10, edgecolor='w',
  #  facecolor='none'))
  #ax.add_patch(Rectangle((bin_id, 0.5/logInterval), 1, rows-0.5/logInterval,
  #  edgecolor='w', facecolor='none'))
  #plt.savefig('kymo.png', bbox_inches='tight')
  plt.savefig('3rods_different_lengths_small_diff_kymo.pdf')
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
    abs_val = np.amax(dataset)
  return dataset, abs_val, labels

start_time = 0
end_time = 2000
bin_id = 23
time = 280
species = [3]
rods = [0, 1, 2]
filename = "histogram_0_55_1.00_n"
start_row, row_labels, col_labels, headers, logInterval = initialize(start_time, filename, rods[0])
data, abs_val, labels = get_data(filename, start_row, row_labels, col_labels, headers, species, rods)
plot_figure(data, row_labels, col_labels, abs_val, bin_id, labels, time, logInterval)
