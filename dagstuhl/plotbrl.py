import math
from pylab import *

#A+B -> C (with rate k)
#d[A]/dt = -k[A][B]
#(1/V)*(dn_A/dt) = -k*(n_A/V)*(n_B/V)
#-(V/(n_A*n_B))*(dn_A/dt) = k
# we used A+B -> C+B
# so we can remove B

N = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 145000, 150000, 155000, 160000, 165000, 170000, 175000, 180000, 185000, 190000, 195000]


#N = [100000]

filenames = []
for i in N:
  filenames.append('log%drl.csv' %(i))

k = []
L = 50e-9
V = L*L*L
n_A = 100.0
n_B = 100.0
const = V/(n_A*n_B)
k = []
for name in filenames:
  f = open(name, 'r')
  first = f.readline().strip().split(',')
  kt = 0.0
  for i in range(90):
    second = f.readline().strip().split(',')
    dn_A = float(first[1])-float(second[1])
    dt = float(second[0])-float(first[0])
    kt = kt+const*dn_A/dt
    first = second
  k.append(kt/90.0)

max_occupancy = (4.0/3.0*math.pi)/(4*math.pow(2.0,0.5))
for i in range(len(N)):
  N[i] = N[i]/199680.0*max_occupancy

print k
plot(N, k, ls='-', color='b', linewidth=1)
show()

