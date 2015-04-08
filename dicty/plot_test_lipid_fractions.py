import numpy as np
import pylab as P

labelFontSize = 14
tickFontSize = 14
legendFontSize = 14
lineFontSize = 14

fileNames = ["IterateLog.csv"]
legendTitles = []
lines = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
colors = ['y', 'r', 'b', 'm', 'c', 'g', '#6b420c', '#33aa00', '#990022', '#005599', '#220088', '#aa8822', '#110077','#003355']

P.xticks(fontsize=tickFontSize)
P.yticks(fontsize=tickFontSize)

f = open(fileNames[0], 'r')
legendTitles = f.readline().strip().split(",")
logInterval = float(legendTitles[0].split("=")[1])
len_x = float(legendTitles[1].split("=")[1])
len_y = float(legendTitles[2].split("=")[1])
len_z = float(legendTitles[3].split("=")[1])
voxelRadius = float(legendTitles[4].split("=")[1])
scale = voxelRadius*2
speciesNames = []
speciesRadii = []
for i in range(len(legendTitles)-5):
  speciesNames.append(legendTitles[i+5].split("=")[0])
  speciesRadii.append(float(legendTitles[i+5].split("=")[1]))
speciesSize = len(speciesNames)

data = np.genfromtxt('anio.csv', delimiter=',', skip_header=1).T

colSize = len(data)-1
for i in range(colSize):
  P.plot(data[0], data[i+1], label=speciesNames[i], color='k', linewidth=1.5)

data = np.genfromtxt('anio_pip2_pip3.csv', delimiter=',', skip_header=1)
rows,cols = data.shape
t = data[0:rows,0:1].ravel()
P.plot(t, (data[0:rows,1:2]+data[0:rows,3:4]+data[0:rows,5:6]).ravel(), label='a', color='y', ls='-', linewidth=1.5)
P.plot(t, (data[0:rows,2:3]+data[0:rows,4:5]+data[0:rows,6:7]).ravel(), label=speciesNames[0], color='r', ls='-', linewidth=1.5)
P.plot(t, (data[0:rows,8:9]+data[0:rows,10:11]+data[0:rows,12:13]).ravel(), label=speciesNames[0], color='m', ls='-', linewidth=1.5)
P.plot(t, (data[0:rows,9:10]+data[0:rows,11:12]+data[0:rows,13:14]).ravel(), label=speciesNames[0], color='c', ls='-', linewidth=1.5)
P.plot(t, data[0:rows,7:8].ravel(), label=speciesNames[0], color='g', ls='-', linewidth=1.0)
P.plot(t, (data[0:rows,14:15]+data[0:rows,16:17]+data[0:rows,18:19]).ravel(), label=speciesNames[0], color='m', ls='-', linewidth=1.5)
P.plot(t, (data[0:rows,15:16]+data[0:rows,17:18]+data[0:rows,19:20]).ravel(), label=speciesNames[0], color='c', ls='-', linewidth=1.5)
P.plot(t, data[0:rows,20:21].ravel(), label=speciesNames[0], color='g', ls='-', linewidth=1.5)

ax = P.gca()
ax.grid(color='b', linestyle='--')
#ax.yaxis.set_major_locator(MaxNLocator(14))
leg = P.legend(loc=0, labelspacing=0.2, handletextpad=0.2, fancybox=True)
for t in leg.get_texts():
  t.set_fontsize(legendFontSize)   
frame = leg.get_frame()
frame.set_linewidth(None)
frame.set_facecolor('0.95')
frame.set_edgecolor('0.75')
P.ylabel('# Molecules')
P.xlabel('Time (s)')
P.show()

