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
  abs_val = loaddata[0][0]
  data = loaddata[1:rows, 1:cols].astype(float)
  row_labels = loaddata[1:rows+1, 0:1].reshape(rows-1)
  col_labels = loaddata[0:1, 1:cols+1].reshape(cols-1)
  return data, row_labels, col_labels, abs_val

def plot_figure(data, row_labels, col_labels, abs_val, plot_cols, plot_rows,
    sub_rows):
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

  xticklabels = np.divide(row_headers[plot_rows[0]-1:plot_rows[1], 0:1], 1e-7)
  x = np.arange(len(xticklabels))
  rows, cols = data.shape
  fig, ax = plt.subplots()
  rects = []
  interval = (x[1]-x[0])
  pcols = plot_cols[1]-plot_cols[0]+1
  width = interval/(pcols+1.0)
  ax.set_color_cycle(['r', 'b', 'g', 'a'])
  colors = get_colors(pcols)
  for i in range(pcols):
    y = data[plot_rows[0]-1:plot_rows[1], plot_cols[0]+i-1:plot_cols[0]+i]
    if sub_rows:
      y = np.subtract(y,
          data[sub_rows[0]-1:sub_rows[1], plot_cols[0]+i-1:plot_cols[0]+i])
    xpos = -interval/2.0+width/2.0+i*width
    rects.append(ax.bar(x+xpos, y, width, color=colors[i])[0])
  ax.set_xlim(x[0]-interval/2.0, x[-1]+interval/2.0)
  ax.set_ylabel('Increase in cytosolic kinesin tip concentration\nwrt. no bias walk (% of max)', fontsize=fontsize)
  ax.set_xlabel('Neurite radius expansion (x0.1 um)', fontsize=fontsize)
  ax.set_xticks(x)
  ax.set_xticklabels(np.transpose(xticklabels)[0])
  ax.tick_params(axis='both', which='major', labelsize=fontsize)
  ax.tick_params(axis='both', which='minor', labelsize=fontsize)
  #ax.set_xticklabels(x, fontsize=20)
  legends = []
  for i in range(pcols):
    legends.append("p=%.1f" %col_headers[plot_cols[0]+i-1])
  ax.legend(rects, legends, loc='upper right', title="MT binding\nprobability",
      fontsize=fontsize)

  ax.get_legend().get_title().set_fontsize('20')
  plt.show()

file = "saved_data.csv"
data, row_labels, col_labels, abs_val = load_data(file)
plot_cols = [4, 6]
plot_rows = [13, 20]
sub_rows = [3, 10]
plot_figure(data, row_labels, col_labels, abs_val, plot_cols, plot_rows, sub_rows)




