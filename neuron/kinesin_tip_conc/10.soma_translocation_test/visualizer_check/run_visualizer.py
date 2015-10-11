#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time
import sys
import glob

files = glob.glob('visual*.dat')

for file in files:
  command_line = "spatiocyte " + file
  print "running... ", command_line
  args = shlex.split(command_line)
  popen = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
          close_fds=True)
  val = raw_input("Should I delete this file?")
  if (val == "y"):
    os.remove(file)
    print "File", file, "is deleted."

