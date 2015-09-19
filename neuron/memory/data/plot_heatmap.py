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
  labels.append(([float(i)]))

def get_mean(file):
  data = np.loadtxt(file, delimiter=",", skiprows=startRow+1)
  rows,cols = data.shape
  #meanCols = [cols-1, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  meanCols = [cols-1]#, cols-2, cols-3] #Edit this to the species cols that you
                                      #want to average
  total = np.zeros(cols)
  for i in meanCols:
    total = np.add(total, data[0:rows, i:i+1].reshape(rows/bins, bins))
  return np.mean(total, axis=0)#.astype(int)

for file in filenames:
  vals = file.split("_")
  vals = vals[1:len(vals)-1]
  for i in range(len(vals)):
    if float(vals[i]) not in labels[i]:
      labels[i].append(float(vals[i]))

row_head_size = len(labels)-len(labels)/2
rows = len(labels[0])
cols = len(labels[row_head_size])
for i in range(row_head_size-1):
  rows = rows*len(labels[i+1])
for i in range(row_head_size, len(labels)-1):
  cols = cols*len(labels[i+1])

for i in range(len(labels)):
  labels[i].sort()

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
  row_labels[row-1] = "%.2f, %.2f" %(vals[0], vals[1])
  col_labels[col-1] = "%.2f, %.2f" %(vals[2], vals[3])
  mean = get_mean(file)[bins-1]
  data[row-1][col-1] = mean
  if mean < min_mean:
    min_mean = mean

#convert to percentage of lowest value
data = np.divide(np.subtract(data, min_mean), min_mean/100.0)
fig, ax = plt.subplots()
#heatmap = ax.pcolor(data, cmap=plt.cm.Blues, alpha=0.8)
heatmap = ax.pcolor(data)
cbar = plt.colorbar(heatmap)

# Format
#fig = plt.gcf()
#fig.set_size_inches(11, 11)

#box = ax.get_position()
#axColor = plt.axes([box.x0*1.05 + box.width * 1.05, box.y0, 0.01, box.height])
#plt.colorbar(heatmap, cax=axColor, orientation="vertical")

# turn off the black line and white background frame
#ax.set_frame_on(False)

# put the major ticks at the middle of each cell
ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)

plt.gca().set_xlim((0, cols))
plt.gca().set_ylim((0, rows))

#annotate
for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        plt.text(x + 0.5, y + 0.5, '%d' % int(data[y, x]),
                 horizontalalignment='center',
                 verticalalignment='center',
                 rotation=90
                 )

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


