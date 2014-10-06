#!/usr/bin/env/python

import sys

import numpy
import imp
import scipy.io
from matplotlib.pylab import *


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
plot_data(Nv, spatiocyte_data,'r.')
loglog(X, 0.24*X**1.06, 'r-', label="Spatiocyte")

plot_data(Nv, egfrd_data,'b.')
loglog(X, 0.8e-4*X**1.8, 'b-', label="eGFRD")

plot_data(Nv, smoldyn_data,'g.')
loglog(X, 3e-2*X**1.25, 'g-', label="Smoldyn")

legend(loc='upper left', labelspacing=0.2, handletextpad=0.2, fancybox=True)

xlabel('# Molecules', size=17)
ylabel('Execution Time', size=17)

Y = numpy.array([60,3600,3600*24,3600*24*30, 3600*24*30*12])

xlim(X[0]*0.9,X[len(X)-1]*1.1)

xticks(size=18)
yticks(Y, ['minute', 'hour', 'day', 'month', 'year'], size=16)

show()
