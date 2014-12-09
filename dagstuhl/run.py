#!/usr/bin/env python

import os

def run_single(N):
  param = ("--parameters=\"{'N':%e}\"" %(N))
  os.system("ecell3-session " + param + " cube.py")

if __name__ == '__main__':
  N = [0, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000]
  for i in N:
    run_single(i)
