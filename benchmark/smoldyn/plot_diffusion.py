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


imp.load_source('smoldyn_out', 'smoldyn_out.py')
from smoldyn_out import *

from run_all import Nv

axes([.12,.14,.86,.83])

X = numpy.array(Nv)
plot_data(Nv, smoldyn_data,'r.')
loglog(X, 3e-2*X**1.25, 'r-')

xlabel('N [# particles]', size=22)

Y = numpy.array([60,3600,3600*24,3600*24*30, 3600*24*30*12])

xlim(X[0],X[len(X)-1]*2)
ylim(0,Y[3])

xticks(size=18)
yticks(Y, ['minute', 'hour', 'day', 'month', 'year'], size=16)

show()
