#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time

def get_param(T, K1, K6, K7, K8, cnt):
  filename = ('visual_%e_%e_%e_%e.dat' %(K1,K6,K7,K8))
  #if (filename == "HistogramCooperativity_1.000000e-02_1.000000e+00_1.000000e-01_1.000000e+03.csv"):
  #  print "jobCnt:",cnt
  #  exit()
  param = ("--parameters=\"{'T':%e, 'K1':%e, 'K6':%e, 'K7':%e, 'K8':%e, 'filename':'%s'}\"" %(T, K1, K6, K7, K8, filename))
  return param

def add_job(param):
  command_line = "ecell3-session " + param + " model.py"
  args = shlex.split(command_line)
  return subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True)

def register_job(param, obj, fdmap, epoll, jobCnt):
  fd = obj.fileno()
  fdmap[fd] = obj
  epoll.register(obj, select.EPOLLHUP)
  print "started job:", jobCnt, "id:", fd, param

T = 1000
K1 = [10, 20, 30, 40, 50, 60, 70, 80]
K6 = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
K7 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
K8 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
if __name__ == '__main__':
  params = []
  cnt = 0
  for i in range(len(K1)):
    for j in range(len(K6)):
      for k in range(len(K7)):
        for l in range(len(K8)):
          cnt = cnt + 1
          if(K8 >= K7 and K6 >= K1):
            params.append(get_param(T, K1[i], K6[j], K7[k], K8[l], cnt))

  SLICE_IN_SECONDS = 0.1
  param = get_param(0.001, K1[0], K6[0], K7[0], K8[0], 0)
  subproc = add_job(param)
  resultTable = []
  startTime = time.time()
  while subproc.poll() == None:
    #resultTable.append(psutil.Process(subproc.pid).memory_info().vms)
    resultTable.append(psutil.Process(subproc.pid).get_memory_info().vms)
    time.sleep(SLICE_IN_SECONDS)
  duration = time.time()-startTime
  typicalMemory = max(resultTable)*1.7

  jobStart = 0
  #jobStart = 4300
  jobEnd = len(params)
  print "total jobs:",len(params), "start:", jobStart, "end:", jobEnd
  jobCnt = jobStart
  #cpuCnt = psutil.cpu_count()
  cpuCnt = psutil.NUM_CPUS
  #cpuCnt = 70
  print "cpuCnt:",cpuCnt
  availableMemory = psutil.virtual_memory().available
  epoll = select.epoll()
  fdmap = {}
  doneCnt = 0
  skipCnt = 1
  while (jobCnt != jobEnd and jobCnt-jobStart-doneCnt < cpuCnt and psutil.virtual_memory().available > typicalMemory):
    #print "avail:",psutil.virtual_memory().available/1024/1024,"req:",typicalMemory/1024/1024
    subproc = add_job(params[jobCnt])
    register_job(params[jobCnt], subproc.stdout, fdmap, epoll, jobCnt) 
    jobCnt = jobCnt + 1
    if (psutil.virtual_memory().available > skipCnt*typicalMemory):
      skipCnt = skipCnt + 1
      print "init fast",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
    else: 
      skipCnt = 1
      print "sleep:",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
      time.sleep(duration)
  while True:
    for fd, flags in epoll.poll(timeout=1):
      del fdmap[fd]
      epoll.unregister(fd)
      doneCnt = doneCnt + 1
      print "done id:",fd
      while (jobCnt != jobEnd and psutil.virtual_memory().available > typicalMemory and jobCnt-jobStart-doneCnt < cpuCnt): 
        #print "avail:",psutil.virtual_memory().available/1024/1024,"req:",typicalMemory/1024/1024
        subproc = add_job(params[jobCnt])
        register_job(params[jobCnt], subproc.stdout, fdmap, epoll, jobCnt) 
        jobCnt = jobCnt + 1
        if (psutil.virtual_memory().available > skipCnt*typicalMemory):
          skipCnt = skipCnt + 1
          print "fast",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
        else: 
          skipCnt = 1
          print "sleep before break",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
          time.sleep(duration)
          break
    if (doneCnt == jobEnd-jobStart):
      break

