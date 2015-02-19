#!/usr/bin/env python
import os

def run_single(T, K1, K6, K4, K8):
  print 'T (sim time) =', T, '; K1 = ', K1, '; K6 =', K6, '; K4 =', K4, '; K8 =', K8
  filename = ('Histogram_%e_%e.csv' %(K1,K4))
  param = ("--parameters=\"{'T':%e, 'K1':%e, 'K6':%e, 'K4':%e, 'K8':%e, 'filename':'%s'}\"" %(T, K1, K6, K4, K8, filename))
  print param
  os.system("ecell3-session " + param + " edge_nocooperativity_iterate.py")

T = 10
K1 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]
K6 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]
K4 = [1e-3, 5e-3, 1e-2, 5e-2, 1e-1, 5e-1, 1e-0, 5e-0, 1e+1, 5e+1, 1e+2, 5e+1, 1e+3, 5e+3]
K8 = [1e-3, 5e-3, 1e-2, 5e-2, 1e-1, 5e-1, 1e-0, 5e-0, 1e+1, 5e+1, 1e+2, 5e+1, 1e+3, 5e+3]
if __name__ == '__main__':
  for i in range(len(K1)):
    for j in range(len(K8)):
      run_single(T, K1[i], K6[i], K4[j], K8[j])
