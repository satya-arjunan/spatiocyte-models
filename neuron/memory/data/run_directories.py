#!/usr/bin/env python
import os
import psutil
import subprocess
import select
import shlex
import time
import sys


dirs = ['GTP_2x_tubConc_fixInt', 'GTP_3x_tubConc_fixInt', 'GTP_4x_tubConc_fixInt', 'GTP_2x_fixConc', 'GTP_3x_fixConc', 'GTP_4x_fixConc', '25kinesin_GTP', 'GTP_2x_fixConc_fixInt', 'GTP_3x_fixConc_fixInt', 'GTP_4x_fixConc_fixInt', '25kinesin_GTP_fixInt', 'GTP_2x_tubConc', 'GTP_3x_tubConc', 'GTP_4x_tubConc']
#dirs = ['250kinesin_tauleap', '25kinesin_GTP_pmax0.1', 'GTP_2x_tubConc_fixInt',  'GTP_3x_tubConc_fixInt',  'GTP_4x_tubConc_fixInt', '25kinesin', '25kinesin_GTP_pmax0.3',  'GTP_2x_fixConc', 'GTP_3x_fixConc', 'GTP_4x_fixConc', '25kinesin_GTP', '25kinesin_tauleap', 'GTP_2x_fixConc_fixInt', 'GTP_3x_fixConc_fixInt', 'GTP_4x_fixConc_fixInt', '25kinesin_GTP_fixInt', 'detach_minus_tauleap', 'GTP_2x_tubConc', 'GTP_3x_tubConc', 'GTP_4x_tubConc']
#dirs = ['25kinesin_GTP','25kinesin_GTP_fixInt']

for dir in dirs:
  command_line = "python run_model.py"
  cwd = dir
  print "running... ", command_line, "in", dir
  args = shlex.split(command_line)
  popen = subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True, cwd=cwd)
  for line in popen.stdout:
    sys.stdout.write(line)
    sys.stdout.flush()
    print dir
