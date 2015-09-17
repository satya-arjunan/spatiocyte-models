import matplotlib.pyplot as plt
import glob
import numpy as np

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
startRow = int(np.ceil((startTime-initTime)/logInterval))*bins
name = filename.split("_")
name = name[1:len(name)-1]
labels = []
for i in name:
  labels.append([i])

def get_mean(file):
  data = np.loadtxt(file, delimiter=",", skiprows=startRow+1)
  rows,cols = data.shape
  meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  total = np.zeros(cols)
  for i in meanCols:
    total = np.add(total, data[0:rows, i:i+1].reshape(rows/bins, bins))
  return np.mean(total, axis=0)#.astype(int)

for file in filenames:
  vals = file.split("_")
  vals = vals[1:len(vals)-1]
  for i in range(len(vals)):
    if vals[i] not in labels[i]:
      labels[i].append(vals[i])

col_head_size = len(labels)/2
row_head_size = len(labels)-col_head_size
cols = len(labels[0])
rows = len(labels[col_head_size])
for i in range(col_head_size-1):
  cols = cols*len(labels[i+1])
for i in range(col_head_size, len(labels)-1):
  rows = rows*len(labels[i+1])


data = np.zeros((cols, rows))
col_labels = np.zeros(cols)
row_labels = np.zeros(rows)

for file in filenames:
  vals = file.split("_")
  vals = vals[1:len(vals)-1]
  col = labels[0].index(vals[0])+1
  for i in range(col_head_size-1):
    col = col+(labels[i+1].index(vals[i+1]))*len(labels[i])
  row = labels[col_head_size].index(vals[col_head_size])+1
  for i in range(col_head_size, len(labels)-1):
    row = row+(labels[i+1].index(vals[i+1]))*len(labels[i])
  data[col-1][row-1] = get_mean(file)[bins-1]


fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=0.8)

# Format
fig = plt.gcf()
fig.set_size_inches(8, 11)

# turn off the frame
ax.set_frame_on(False)

# put the major ticks at the middle of each cell
ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(col_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)

# rotate the
plt.xticks(rotation=90)

ax.grid(False)

# Turn off all the ticks
ax = plt.gca()

for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
plt.show()


