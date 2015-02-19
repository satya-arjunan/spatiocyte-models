#!/usr/bin/env python
import os

def run_single(T, K1, K6, K4, K8):
  print 'T (sim time) =', T, '; K1 = ', K1, '; K6 =', K6, '; K4 =', K4, '; K8 =', K8
  filename = ('Histogram_%e_%e.csv' %(K1,K4))
  param = ("--parameters=\"{'T':%e, 'K1':%e, 'K6':%e, 'K4':%e, 'K8':%e, 'filename':'%s'}\"" %(T, K1, K6, K4, K8, filename))
  print param
  os.system("ecell3-session " + param + " edge_nocooperativity_iterate.py")

T = 4000
K1 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
K6 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
K4 = [1e-3, 1e-1, 1e-0, 1e+1, 1e+2, 1e+3]
K8 = [1e-3, 1e-1, 1e-0, 1e+1, 1e+2, 1e+3]
if __name__ == '__main__':
  for i in range(len(K1)):
    for j in range(len(K8)):
      run_single(T, K1[i], K6[i], K4[j], K8[j])
