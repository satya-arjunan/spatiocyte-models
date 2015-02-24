#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time

def get_param(T, K1, K6, K7, K8):
  filename = ('HistogramCooperativity_%e_%e_%e_%e.csv' %(K1,K6,K7,K8))
  param = ("--parameters=\"{'T':%e, 'K1':%e, 'K6':%e, 'K7':%e, 'K8':%e, 'filename':'%s'}\"" %(T, K1, K6, K7, K8, filename))
  return param

def add_job(param):
  command_line = "ecell3-session " + param + " edge_cooperativity_iterate.py"
  args = shlex.split(command_line)
  return subprocess.Popen(args, stdout=subprocess.PIPE)

def register_job(param, subproc, subprocs, poller, jobCnt):
  fd = subproc.stdout.fileno()
  subprocs[fd] = subproc
  poller.register(subproc.stdout, select.EPOLLHUP)
  print "started job:", jobCnt, "id:", fd, param

N = 500
T = 10
K6 = 1.0
#K1 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.009, 0.008, 0.007, 0.006, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0009, 0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00009, 0.00008, 0.00007, 0.00006, 0.00005, 0.00004, 0.00003, 0.00002, 0.00001, 0.00009, 0.000008, 0.000007, 0.000006, 0.000005, 0.000004, 0.000003, 0.000002, 0.000001]
K1 = [7.5e-1, 5e-1, 2.5e-1, 1e-1, 7.5e-2, 5e-2, 2.5e-2, 1e-2, 7.5e-3, 5e-3, 2.5e-3, 1e-3, 7.5e-4, 5e-4, 2.5e-4, 1e-4, 7.5e-5, 5e-5, 2.5e-5, 1e-5, 7.5e-6, 5e-6, 2.5e-6, 1e-6]
K7 = [5e+2, 1e+2, 5e+1, 1e+1, 5e+0, 1e+0, 5e-1, 1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-4, 5e-5, 1e-5]
K8 = [1e-3, 5e-3, 1e-2, 5e-2, 1e-1, 5e-1, 1e-0, 5e-0, 1e+1, 5e+1, 1e+2, 5e+1, 1e+3, 5e+3]
if __name__ == '__main__':
  params = []
  for i in range(len(K1)):
    for j in range(len(K7)):
      for k in range(len(K8)):
        params.append(get_param(T, K1[i], K6, K7[j], K8[k]))

  SLICE_IN_SECONDS = 1
  param = get_param(10, K1[0], K6, K7[0], K8[0])
  subproc = add_job(param)
  resultTable = []
  while subproc.poll() == None:
    resultTable.append(psutil.Process(subproc.pid).memory_info().rss)
    time.sleep(SLICE_IN_SECONDS)
  print max(resultTable)/1024/1024

  jobStart = 3
  jobEnd = 5
  print "total jobs:",len(params), "start:", jobStart, "end:", jobEnd
  jobCnt = jobStart
  cpuCnt = psutil.cpu_count()
  availableMemory = psutil.virtual_memory().available
  poller = select.epoll()
  subprocs = {}
  for i in xrange(2):
    subproc = add_job(params[jobCnt])
    register_job(params[jobCnt], subproc, subprocs, poller, jobCnt) 
    jobCnt = jobCnt + 1
  doneCnt = 0
  while True:
    for fd, flags in poller.poll(timeout=1):
      done_proc = subprocs[fd]
      poller.unregister(fd)
      doneCnt = doneCnt + 1
      print "done id:",fd
      if (jobCnt != jobEnd):
        subproc = add_job(params[jobCnt])
        register_job(params[jobCnt], subproc, subprocs, poller, jobCnt) 
        jobCnt = jobCnt + 1
    if (doneCnt == jobEnd-jobStart):
      break

