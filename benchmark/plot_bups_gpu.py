#!/usr/bin/env/python

import sys

import numpy
import imp
import scipy.io
from matplotlib.pylab import *
#uncomment the following to create valid eps (scribus) and svg (inkscape):
#rc('svg', embed_char_paths=True)
#rc('mathtext', fontset=r'stixsans')

#matplotlib.rcParams["mathtext.fontset"] = "stix"
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage{amsmath}')
matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage[helvet]{sfmath}')

labelFontSize = 15
legendFontSize = 14
lineFontSize = 15

imp.load_source('spatiocyte_out', 'spatiocyte/spatiocyte_out.py')
from spatiocyte_out import *
imp.load_source('gpu_out', 'spatiocyte/gpu_out.py')
from gpu_out import *
imp.load_source('gpu_dillute_out', 'spatiocyte/gpu_dillute_out.py')
from gpu_dillute_out import *
imp.load_source('spatiocyte_dillute_out', 'spatiocyte/spatiocyte_dillute_out.py')
from spatiocyte_dillute_out import *

imp.load_source('run_all', 'spatiocyte/run_all.py')
from run_all import Nv

X = numpy.array(Nv)
data = numpy.empty([len(Nv)])
print "Serial BUPS:"
for i in range(len(Nv)):
    data[i] = 240000.0*float(Nv[i])/(float(spatiocyte_dillute_data[i][0])/10.0)/1e+9 
    print Nv[i], data[i]
print data
plot(Nv, data,'ro', label=r'Spatiocyte CPU')
loglog(X, numpy.ones(len(X))*0.00315, 'r--')
annotate(r'BUPS = 0.0031', xy=(X[0], data[8]), xycoords='data', xytext=(10,-20), textcoords='offset points', color='r', size=14)

print "GPU BUPS:"
for i in range(len(Nv)):
    data[i] = 240000.0*float(Nv[i])/(float(gpu_dillute_data[i][0])/10.0)/1e+9 
    print Nv[i], data[i]
print data
plot(Nv, data,'bo', label=r'Spatiocyte GPU (Thrust)')
loglog(X, numpy.ones(len(X))*0.45, 'b--')
annotate(r'BUPS = 0.45', xy=(X[0], data[8]), xycoords='data', xytext=(10,-20), textcoords='offset points', color='b', size=14)


leg = legend(loc="center right", labelspacing=0.3, handletextpad=0.2)
for t in leg.get_texts():
  t.set_fontsize(legendFontSize) 

xlabel('$N$ (\# Molecules)', size=17)
ylabel('Billion updates per second (BUPS)', size=17)
xscale("log")
yscale("log")
xlim(X[0]*0.9,X[len(X)-1]*1.1)


#xticks(size=14)
#tick_params(labeltop=True, labelright=True)
savefig('diffusion.eps', format='eps', dpi=1000)
show()
