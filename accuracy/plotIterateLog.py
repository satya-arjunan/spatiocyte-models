import numpy as np
import pylab as P
from scipy.special import erfc,erf
import math

def g(t):
  n = 10000.0
  A = 100e-6*100e-6
  V = 100e-6*100e-6*100e-6
  k = 5e-6
  D = 1e-6
  h = k/D
  return n*A/(h*V)*(np.exp(h*h*D*t)*erfc(h*np.sqrt(D*t))-1.0+2/np.pi*h*np.sqrt(D*t))

def g2(t):
  n = 10000.0
  A = 100e-6*100e-6
  V = 100e-6*100e-6*100e-6
  k = 5e-6
  D = 1e-6
  h = k/D
  return n*A/(h*V)*(math.exp(h*h*D*t)*(1-erf(h*math.sqrt(D*t)))-1.0+2/math.pi*h*math.sqrt(D*t))

labelFontSize = 14
tickFontSize = 14
legendFontSize = 14
lineFontSize = 14

fileNames = ["IterateLogXY.csv"]
legendTitles = []
lines = ['-', '-', '-', '-', '-', '-', '-', '-']
colors = ['y', 'r', 'b', 'm', 'c', 'g', '#6b420c']

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

data = np.genfromtxt(fileNames[0], delimiter=',', skip_header=1).T

colSize = len(data)-1
for i in range(colSize):
  P.plot(data[0], data[i+1], ls=lines[i], color=colors[i], label=speciesNames[i], linewidth=1.5)


#x = np.linspace(0,200,50)
#P.plot(x, g(x))

#y = []
#for i in x:
#  y.append(g2(i))
#P.plot(x, y)


#data = np.loadtxt('plot-data.csv', delimiter=",")
data = np.loadtxt('data-mathematica-ori.csv', delimiter=",")
rows,cols = data.shape
col0 = data[0:rows, cols-2:cols-1]
col1 = data[0:rows, cols-1:cols]

P.plot(col0, col1)

#P.plotfile('plot-data.csv', delimiter=',', cols=(0, 1), names=('col1', 'col2'), marker='o')


ax = P.gca()
ax.grid(color='b', linestyle='--')
#ax.yaxis.set_major_locator(MaxNLocator(14))
leg = P.legend(loc=0, labelspacing=0.2, handletextpad=0.2, fancybox=True)
P.ylabel('# Molecules')
P.xlabel('Time (s)')
P.show()

