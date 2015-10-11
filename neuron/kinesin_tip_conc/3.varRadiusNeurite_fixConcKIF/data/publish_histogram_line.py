#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import colorsys

fontsize = 20

def get_colors(num_colors):
    colors=[]
    for i in np.arange(0., 360., 360. / num_colors):
        hue = i/360.
        lightness = (35 + np.random.rand() * 10)/100.
        saturation = (70 + np.random.rand() * 10)/100.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors

kelly_colors = ['#007D34', '#00538A', '#7F180D', '#53377A', '#FF8E00', '#B32851', '#F4C800', '#93AA00', '#593315', '#F13A13', '#232C16', '#FFB300', '#803E75', '#FF6800', '#A6BDD7', '#C10020', '#CEA262', '#817066', '#F6768E', '#FF7A5C']


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

def plot_figure(data, row_labels, col_labels, abs_val, plot_cols, plot_rows,
    sub_rows, plot_bar):
  row_headers = np.zeros((len(row_labels), len(row_labels[0].split(" "))))
  for i in range(len(row_labels)):
    labels = row_labels[i].split(" ")
    for j in range(len(labels)):
      row_headers[i, j] = float(labels[j])

  col_headers = np.zeros((len(col_labels), len(col_labels[0].split(" "))))
  for i in range(len(col_labels)):
    labels = col_labels[i].split(" ")
    for j in range(len(labels)):
      col_headers[i, j] = float(labels[j])

  #xticklabels = np.add(row_headers[plot_rows[0]-1:plot_rows[1], 0:1], 0.4e-6)
  #xticklabels = np.divide(xticklabels, 1e-7)
  bins, rows, cols = data.shape
  x = np.arange(bins)
  xticklabels = np.add(x, 1)
  xticklabels = np.divide(xticklabels, 10.0)
  fig, ax = plt.subplots()
  rects = []
  interval = (x[1]-x[0])
  prows = plot_rows[1]-plot_rows[0]+1
  width = interval/(prows+1.0)
  colors = get_colors(prows)
  for i in range(prows):
    y = data[0:bins, plot_rows[0]+i-1:plot_rows[0]+i,
        plot_cols[0]-1:plot_cols[1]]
    if sub_rows:
      y = np.subtract(y,
          data[0:bins, sub_rows[0]+i-1:sub_rows[0]+i,
            plot_cols[0]-1:plot_cols[1]])
    y = np.ravel(y)
    xpos = -interval/2.0+width/2.0+i*width
    if plot_bar:
      rects.append(ax.bar(x+xpos, y, width, color=colors[i])[0])
    else:
      rects.append(ax.plot(x, y, color=colors[i], linewidth=5)[0])
  if plot_bar:
    ax.set_xlim(x[0]-interval/2.0, x[-1]+interval/2.0)
    ax.set_ylim(0, 80)
  else:
    ax.set_xlim(x[0], x[-1])
  ax.set_ylabel('Cytosolic kinesin concentration at p=0.5 (% of max)',
      fontsize=fontsize)
  ax.set_xlabel('Normalized distance along neurite', fontsize=fontsize)
  ax.set_xticks(x)
  ax.set_xticklabels(xticklabels)
  ax.tick_params(axis='both', which='major', labelsize=fontsize)
  ax.tick_params(axis='both', which='minor', labelsize=fontsize)
  #ax.set_xticklabels(x, fontsize=20)
  legends = []
  for i in range(prows):
    legends.append("%.1f" %((row_headers[plot_rows[0]+i-1][0]+0.4e-6)/1e-7))
  ax.legend(rects, legends, loc='lower left',
      title="Neurite radius\n(x0.1 um)", fontsize=fontsize, labelspacing=0.1, framealpha=0.7, ncol=1, columnspacing=0.3, handletextpad=0.2)

  ax.get_legend().get_title().set_fontsize('20')
  plt.show()

file = "saved_histogram_data.csv"
data, row_labels, col_labels, abs_val = load_data(file)
plot_bar = 0
plot_cols = [5, 5]
#plot_rows = [11, 20]
plot_rows = [12, 22]
#sub_rows = [1, 11]
sub_rows = []
plot_figure(data, row_labels, col_labels, abs_val, plot_cols, plot_rows, sub_rows, plot_bar)




