#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time

def get_param(T, Iterations, String, V1, V2, V3, V4, cnt):
  param = ("--parameters=\"{'T':%f, 'Iterations':%d, 'String':'%s', 'V1':%e, 'V2':%e, 'V3':%e, 'V4':%e}\"" %(T, Iterations, String, V1, V2, V3, V4))
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

T = 54000
Iterations = 1
V1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0] #percentage increase in radius
V2 = [0.00001] #ratchet rate
V3 = [0.9]
V4 = [0]
String = 'None'
if __name__ == '__main__':
  params = []
  cnt = 0
  for i in range(len(V1)):
    for j in range(len(V2)):
      for k in range(len(V3)):
        for l in range(len(V4)):
          cnt = cnt + 1
          params.append(get_param(T, Iterations, String, V1[i], V2[j], V3[k],
            V4[l], cnt))

  SLICE_IN_SECONDS = 0.1
  param = get_param(1, 1, String, V1[0], V2[0], V3[0], V4[0], 0)
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
          #print "fast",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
        else: 
          skipCnt = 1
          print "sleep before break",skipCnt,"virt:",psutil.virtual_memory().available/1024/1024,"typ:",skipCnt*typicalMemory/1024/1024
          time.sleep(duration)
          break
    if (doneCnt == jobEnd-jobStart):
      break

