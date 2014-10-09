#!/usr/bin/env python
import sys
import numpy
import math

T = 10.
Rv = 2.5e-9 #voxel radius
Dv = 1e-12 #diffusion coefficient
Vv = [3e-18, ] * 11 #simulation volume
Nv = [100,300,1000,3000,10000,30000,100000,300000,1000000,3000000,10000000] #number of molecules
Tv = [max(1e-5, min(T, 1e0 / math.pow(N, 2.0 / 3.0))) for N in Nv] #duration
REPEAT = 1
