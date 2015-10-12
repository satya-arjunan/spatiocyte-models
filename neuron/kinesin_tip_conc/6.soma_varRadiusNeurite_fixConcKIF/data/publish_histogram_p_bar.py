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
  bins = 1
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

  xticklabels = row_headers[plot_rows[0]-1:plot_rows[1], 0:1]
  x = np.arange(len(xticklabels))
  bins, rows, cols = data.shape
  fig, ax = plt.subplots()
  rects = []
  interval = (x[1]-x[0])
  pcols = len(plot_cols)
  width = interval/(pcols+1.0)
  colors = get_colors(pcols)
  for i in range(pcols):
    y = data[bins-1:bins, plot_rows[0]-1:plot_rows[1],
        plot_cols[i]-1:plot_cols[i]]
    if sub_rows:
      y = np.subtract(y,
          data[bins-1:bins, sub_rows[0]-1:sub_rows[1],
            plot_cols[i]-1:plot_cols[i]])
    xpos = -interval/2.0+width/2.0+i*width
    rects.append(ax.bar(x+xpos, y[0], width, color=colors[i])[0])
  ax.set_xlim(x[0]-interval/2.0, x[-1]+interval/2.0)
  ax.set_ylabel('Cytosolic kinesin concentration at\nneurite tip with p=1.0 (% of max)', fontsize=fontsize)
  ax.set_xlabel('% radius expansion of neurite #4', fontsize=fontsize)
  ax.set_xticks(x)
  ax.set_xticklabels(np.multiply(np.transpose(xticklabels)[0], 1).astype(int))
  ax.tick_params(axis='both', which='major', labelsize=fontsize)
  ax.tick_params(axis='both', which='minor', labelsize=fontsize)
  #ax.set_xticklabels(x, fontsize=20)
  legends = []
  col_headers = np.transpose(col_headers)
  for i in range(pcols):
    legends.append("%d" %(col_headers[1][plot_cols[i]-1]+1))
  ax.legend(rects, legends, loc='upper left', title="Neurite #",
      fontsize=fontsize, labelspacing=0.1, framealpha=0.9, ncol=1, columnspacing=0.3, handletextpad=0.2)

  ax.get_legend().get_title().set_fontsize('20')
  plt.show()

file = "saved_histogram_data.csv"
data, row_labels, col_labels, abs_val = load_data(file)
plot_bar = 1
plot_cols = [6, 12, 18, 24]
plot_rows = [12, 22]
#sub_rows = [1, 10]
sub_rows = []
plot_figure(data, row_labels, col_labels, abs_val, plot_cols, plot_rows, sub_rows, plot_bar)




