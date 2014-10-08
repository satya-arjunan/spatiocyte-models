#!/usr/bin/env/python

import sys

import numpy
import imp
import scipy.io
from matplotlib.pylab import *
matplotlib.rcParams["mathtext.fontset"] = "stix"

N_A = 6.0221367e23

def plot_data(N, T, fmt):
    T = numpy.array(T)

    mean = T.mean(1)
    std_err = T.std()/math.sqrt(len(T))

    #errorbar(N, mean, yerr=std_err, fmt=fmt)
    print N, mean
    loglog(N, mean, fmt)


imp.load_source('spatiocyte_out', 'spatiocyte/spatiocyte_out.py')
from spatiocyte_out import *
imp.load_source('egfrd_out', 'egfrd/egfrd_out.py')
from egfrd_out import *
imp.load_source('smoldyn_out', 'smoldyn/smoldyn_out.py')
from smoldyn_out import *

from run_all import Nv

axes([.12,.14,.86,.83])

X = numpy.array(Nv)

plot(Nv, spatiocyte_data,'ro', label="Spatiocyte")
loglog(X, 0.24*X**1.05, 'r-')
annotate(r'$\mathsf{t} \ \propto \ \mathsf{N}^{\mathsf{1.05}}$', xy=(X[2], spatiocyte_data[2][0]),  xycoords='data', xytext=(-20, 10), textcoords='offset points', color='r', size=16)

plot(Nv, egfrd_data,'bs', label="eGFRD")
loglog(X, 0.8e-4*X**1.8, 'b-')
annotate(r'$\mathsf{t} \ \propto \ \mathsf{N}^{\mathsf{1.8}}$', xy=(X[3], egfrd_data[3][0]),  xycoords='data', xytext=(-10, -20), textcoords='offset points', color='b', size=16)

plot(Nv, smoldyn_data,'g^', label="Smoldyn")
loglog(X, 3e-2*X**1.25, 'g-')
annotate(r'$\mathsf{t} \ \propto \ \mathsf{N}^{\mathsf{1.25}}$', xy=(X[1], smoldyn_data[1][0]),  xycoords='data', xytext=(-30, -30), textcoords='offset points', color='g', size=16)

legend(loc='upper left')
#legend(loc='upper left', labelspacing=0.2, handletextpad=0.2, fancybox=True)

xlabel('N (# Molecules)', size=17)
#ylabel('Execution Time', size=17)

Y = numpy.array([60,3600,3600*24,3600*24*30, 3600*24*30*12])

xlim(X[0]*0.9,X[len(X)-1]*1.1)

xticks(size=18)
yticks(Y, ['minute', 'hour', 'day', 'month', 'year'], size=16)

savefig('data.eps', format='eps', dpi=1000)
show()
