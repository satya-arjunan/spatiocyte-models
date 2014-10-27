import numpy
import csv
import math
from matplotlib import rc
from pylab import *
matplotlib.rcParams["mathtext.fontset"] = "stix"

labelFontSize = 15
legendFontSize = 14
lineFontSize = 15

fileNames = ['egfrd/egfrd.csv', 'egfrd/egfrd_small_r.csv','smoldyn/smoldyn.csv','smoldyn/smoldyn_small_dt.csv','spatiocyte/spatiocyte.csv','spatiocyte/spatiocyte_small_dt.csv','spatiocyte/ode.csv',]
legendTitles = ['eGFRD ($r=10\ \mathrm{nm},\ \mathrm{RT}=2897\ \mathrm{s}$)','eGFRD ($r=1\ \mathrm{nm},\ \mathrm{RT}=2232\ \mathrm{s}$)','Smoldyn ($\Delta t=1\ \mathrm{ms},\ \mathrm{RT}=17\ \mathrm{s}$)','Smoldyn ($\Delta t=67\ \mathrm{\mu s},\ \mathrm{RT}=243\ \mathrm{s}$)','Spatiocyte ($\Delta t=1\ \mathrm{ms},\ r=38.73\ \mathrm{nm},\ \mathrm{RT}=11\ \mathrm{s}$)','Spatiocyte ($\Delta t=67\ \mathrm{\mu s},\ r=10\ \mathrm{nm},\ \mathrm{RT}=254\ \mathrm{s}$)','Mass Action']
speciesList = ['E','S','ES','P']
lines = ['-','--','-','--','-','--','-']
colors = ['b', 'b', 'g', 'g', 'r', 'r','k']

for f in range(len(fileNames)):
  deli = ','
  if (f == 2 or f == 3):
    deli = ' '
  data = genfromtxt(fileNames[f], delimiter=deli).T
  colSize = len(data)-1
  for i in range(colSize):
    if (i == 0):
      plot(data[0], data[i+1], ls=lines[f], color=colors[f], label=legendTitles[f], linewidth=1)
    else:
      plot(data[0], data[i+1], ls=lines[f], color=colors[f], linewidth=1)

annotate('ES', xy=(90, 0),  xycoords='data', xytext=(-29, 10), textcoords='offset points', color='k', size=16)

annotate('E', xy=(90, 60),  xycoords='data', xytext=(-27, 15), textcoords='offset points', color='k', size=16)

annotate('P', xy=(90, 230),  xycoords='data', xytext=(-27, 12), textcoords='offset points', color='k', size=16)

annotate('S', xy=(90, 680),  xycoords='data', xytext=(-27, 12), textcoords='offset points', color='k', size=16)

annotate(r'E + S $k_1 k_2\rightleftharpoons$ ES $k_3\rightarrow$ E + P', xy=(55, 880),  xycoords='data', xytext=(-29, 10), textcoords='offset points', color='k', size=16)

ax = gca()
leg = legend(loc=(0.02,0.23), labelspacing=0.3, handletextpad=0.2)
for t in leg.get_texts():
  t.set_fontsize(legendFontSize)   
xticks(size=17)
yticks(size=17)
xlabel('time, t (s)',size=17)
ylabel('# Molecules',size=17)
xlim(0,100)
savefig('reaction.eps', format='eps', dpi=1000)
show()

