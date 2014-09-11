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
imp.load_source('egfrd_out', 'egfrd/egfrd_out.py')
from spatiocyte_out import *
from egfrd_out import *

from run_all import Nv

axes([.12,.14,.86,.83])

X = numpy.array(Nv)
plot_data(Nv, spatiocyte_data,'r.')
loglog(X, 0.4*X, 'r-')

plot_data(Nv, egfrd_data,'b.')
loglog(X, 0.1*X, 'b-')

xlabel('N [# particles]', size=22)

Y = numpy.array([60,3600,3600*24,3600*24*30, 3600*24*30*12])

xticks(size=18)
yticks(Y, ['minute', 'hour', 'day', 'month', 'year'], size=16)

show()
