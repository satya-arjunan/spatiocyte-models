#!/usr/bin/env python

import os

def run_single(N):
  param = ("--parameters=\"{'N':%e}\"" %(N))
  os.system("ecell3-session " + param + " cubedl.py")

if __name__ == '__main__':
  N = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 145000, 150000, 155000, 160000, 165000, 170000, 175000, 180000, 185000, 190000, 195000]
  for i in N:
    run_single(i)
