import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import glob
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import csv
import math
from scipy.optimize import curve_fit

fontsize = 15 

def get_mean(data, row_labels, col_labels, labels, start_time, end_time, bin_id):
  return np.mean(data[:, :, bin_id][0])

def get_headers(filename):
  f = open(filename, 'rb')
  reader = csv.reader(f)
  headers = reader.next()[2:]
  for i in range(len(headers)):
    headers[i] = headers[i].split(']')[0].strip('[')
    headers[i] = headers[i].split(':')[1] #remove path of species
  return headers

def initialize(startTime, filename):
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
  return start_row, row_labels, col_labels, headers

def get_data(filename, start_row, row_labels, col_labels, headers, species):
  data = np.loadtxt(filename, delimiter=",", skiprows=start_row+1)
  rows,cols = data.shape
  bins = len(col_labels)
  dataset = np.zeros([1, rows/bins, bins])
  labels = ""
  for i in range(len(species)):
    dataset = np.add(dataset, data[0:rows, species[i]+2:species[i]+3].reshape(rows/bins, bins))
    labels = labels+"\n"+headers[species[i]]
  labels = [labels]
  abs_val = np.amax(dataset)
  return dataset, abs_val, labels


def func(x,M,a):
   return M*(1.0-np.exp(-x/a))

start_time = 1000
end_time = 1700
bin_id = -1 #last bin
species = [0, 1, 2, 3, 4, 5, 6]
cut_off = 0.1
iteration = 1
filenames = glob.glob("histogram_*.csv")
nKinesin = np.empty(0)
for file in filenames:
  nKinesin = np.append(nKinesin, int(file.split("_")[1]))
nKinesin = np.unique(nKinesin)
cnts = np.zeros(1)
kinesins = np.zeros(1)
for val in nKinesin:
  if(val <= 1950):
    filenames = glob.glob("histogram_%d_%d_*.csv" %(val, iteration))
    cnt = 0
    for file in filenames:
      start_row, row_labels, col_labels, headers = initialize(start_time, file)
      data, abs_val, labels = get_data(file, start_row, row_labels, col_labels, headers, species)
      mean = np.mean(data[:, :, bin_id][0])
      if(mean > cut_off):
        mean = 1
        cnt = cnt+1
      else:
        mean = 0
    cnts = np.append(cnts, cnt)
    kinesins = np.append(kinesins, val)
    print val, cnts
print kinesins, cnts
fig, ax = plt.subplots()
ax.bar(kinesins, cnts)
#ax.plot(kinesins, cnts)
popt, pcov = curve_fit(func, kinesins, cnts, bounds=(0,[16.0,1500.0]))
y = func(kinesins, *popt)
ax.plot(kinesins,y)
y = np.empty(0)
for i in kinesins:
  y = np.append(y, i*0.025)
ax.plot(kinesins,y)
ax.set_ylim([0,17])
plt.ylabel("# branch switched on", fontsize=fontsize)
plt.xlabel('# kinesin', fontsize=fontsize)
plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.savefig('analog2digital_dual.png', bbox_inches='tight')
plt.show()
