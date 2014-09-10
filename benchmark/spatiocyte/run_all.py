#!/usr/bin/env python
import sys
import numpy
import math
import run_single

def run_set(outfile, name, V_list, N_list, T_list, R, D, REPEAT):
    outfile.write('%s = [\n' % name)
    for i in range(len(V_list)):
        outfile.write('# T=%g, N=%g, V=%g\n' % 
                      (T_list[i], N_list[i], V_list[i]))
        run_times = []
        est_times = []
        for c in range(REPEAT):
            run_time = run_single.run_single(T_list[i], V_list[i], N_list[i], R, D)
            est_time = run_time * (T / T_list[i])
            run_times.append(run_time)
            est_times.append(est_time)
        outfile.write('# run_times = %s\n' % str(run_times))
        outfile.write('%s,\n' % str(est_times))
        outfile.flush()
    outfile.write(']\n')

T = 10.
Rv = 2.5e-9 #voxel radius
Dv = 1e-12 #diffusion coefficient
Vv = [2e-15, ] * 11 #simulation volume (should be 2e-14)
Nv = [100,300,1000,3000,10000,30000,100000,300000,1000000,3000000,10000000] #number of molecules
Tv = [max(1e-5, min(T, 1e0 / math.pow(N, 2.0 / 3.0))) for N in Nv] #duration
REPEAT = 1

if __name__ == '__main__':
    prefix = 'out_'
    mode = "Vspatiocyte"
    outfile = open(prefix+mode+'.py','w'); 
    dataname = 'data_' + mode
    run_set(outfile, dataname, Vv, Nv, Tv, Rv, Dv, REPEAT); outfile.write('\n\n')
