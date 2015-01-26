import math
from matplotlib.pylab import *

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage{amsmath}')
matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage[helvet]{sfmath}')


#A+B -> C (with rate k)
#d[A]/dt = -k[A][B]
#(1/V)*(dn_A/dt) = -k*(n_A/V)*(n_B/V)
#-(V/(n_A*n_B))*(dn_A/dt) = k
# we used A+B -> C+B
# so we can remove B

N = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 145000, 150000, 155000, 160000, 165000, 170000, 175000, 180000, 185000, 190000, 195000]

#N = [100000]
L = 50e-9
V = L*L*L
n_A = 100.0
n_B = 100.0
const = V/(n_A*n_B)
max_occupancy = (4.0/3.0*math.pi)/(4*math.pow(2.0,0.5))
Np = []
for i in range(len(N)):
  Np.append(N[i]/199680.0*max_occupancy)

#dl = diffusion limited
#lrl = low reaction limited
#irl = intermediate reaction limited
#rl = reaction limited

R = ['dl','lrl','irl','rl']
species = [r'$k_0=84.9\ \mathrm{nm}^3/\mu s^{-1}$ (diffusion-limited)', r'$k_0=42.5\ \mathrm{nm}^3/\mu s^{-1}$', r'$k_0=8.49\ \mathrm{nm}^3/\mu s^{-1}$', r'$k_0=0.85\ \mathrm{nm}^3/\mu s^{-1}$ (activation-limited)']
colors = ['y', 'r', 'b', 'm', 'c', 'g']
lineCnt = 0

markers = []
for s in R:
  max_k= 0
  filenames = []
  for i in N:
    filenames.append('log%d%s.csv' %(i,s))
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
    val = kt/90.0
    if (val > max_k):
      max_k = val
    k.append(val)
  #normalize
  for i in range(len(k)):
    k[i] = k[i]/max_k
  plot(Np, k, ls='-', color=colors[lineCnt], linewidth=1)
  markers.append(Rectangle((0, 0), 1, 1, fc=colors[lineCnt]))
  lineCnt = lineCnt + 1

legend(markers, species, loc='upper center', labelspacing=0.2, handletextpad=0.2, fancybox=True)
ylim(0,1.4)
ylabel('Normalized simulated reaction rate, k', size=17)
xlabel('Occupied volume fraction, $\phi$', size=17)
savefig('spatiocyte.eps', format='eps', dpi=1000)

show()

