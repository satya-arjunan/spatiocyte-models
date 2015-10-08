#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time
import sys
import glob

dirs = ['5.*', '6.*', '7.*', '8.*']

for dir in dirs:
  command_line = "python run_model.py"
  dir = glob.glob(dir)[0]
  cwd = dir
  print "running... ", command_line, "in", dir
  args = shlex.split(command_line)
  popen = subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True, cwd=cwd)
  for line in popen.stdout:
    sys.stdout.write(line)
    sys.stdout.flush()
    print dir
