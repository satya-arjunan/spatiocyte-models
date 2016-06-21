import numpy as np
import pylab as P
import matplotlib as mpl

fontsize = 15
mpl.rcParams.update({'font.size': fontsize})


labelFontSize = fontsize
tickFontSize = fontsize
legendFontSize = fontsize
lineFontSize = fontsize

co = 24

fileNames = ["MTIterateLog.%dnM.csv" %co, "Fig.5.%dnM.sim.csv" %co, "Fig.5.%dnM.exp.csv" %co, "verified_hd_mt_nocop_%dnM.csv" %co]
legendTitles = ["3D Particle Simulation", "Simulation", "Experiment", "No Cooperativity"]
lines = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
colors = ['y', 'r', 'b', 'm', 'c', 'g', '#6b420c', '#33aa00', '#990022', '#005599', '#220088', '#aa8822', '#110077','#003355']

P.xticks(fontsize=tickFontSize)
P.yticks(fontsize=tickFontSize)

f = open(fileNames[0], 'r')

data = np.genfromtxt(fileNames[0], delimiter=',', skip_header=1).T

colSize = len(data)-1
combined = np.sum(data[1:], axis=0)
amax = np.amax(combined)
#for i in range(colSize):
#  P.plot(np.divide(data[0],60.0), np.divide(data[i+1],amax), ls=lines[i], color=colors[i], label=speciesNames[i], linewidth=1.5)

P.plot(np.divide(data[0],60.0), np.divide(combined, amax), linewidth=1.5, label=legendTitles[0].split('.csv')[0])

#data = np.genfromtxt(fileNames[1], delimiter=',', skip_header=0).T
#P.plot(data[0], data[1], linewidth=0, marker='o', color='k', markersize=5, label=legendTitles[1].split('.csv')[0])

data = np.genfromtxt(fileNames[3], delimiter=',', skip_header=1).T
colSize = len(data)-1
combined = np.sum(data[1:], axis=0)
amax = np.amax(combined)
#for i in range(colSize):
#  P.plot(np.divide(data[0],60.0), np.divide(data[i+1],amax), ls=lines[i], color=colors[i], label=speciesNames[i], linewidth=1.5)

P.plot(np.divide(data[0],60.0), np.divide(combined, amax), linestyle='--', linewidth=1.5, label=legendTitles[3].split('.csv')[0])


data = np.genfromtxt(fileNames[2], delimiter=',', skip_header=0).T
P.plot(data[0], data[1], linewidth=0, marker='o', color='r', markersize=10, label=legendTitles[2].split('.csv')[0])


ax = P.gca()
#ax.grid(color='k', linestyle='--')
ax.set_ylim([-0.02, 1.1])
ax.set_xlim(left=-0.1)
#ax.yaxis.set_major_locator(MaxNLocator(14))
leg = P.legend(loc=0, labelspacing=0.2, handletextpad=0.2, fancybox=True)
for t in leg.get_texts():
  t.set_fontsize(legendFontSize)   
frame = leg.get_frame()
frame.set_linewidth(None)
frame.set_facecolor('0.95')
frame.set_edgecolor('0.75')
P.title("%d nM" %co)
P.ylabel('P/Pequilibrium')
P.xlabel('Time (min)')
P.savefig('%dnM.png' %co, bbox_inches='tight')
P.show()
