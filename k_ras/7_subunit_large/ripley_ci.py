import numpy as np
from matplotlib import pyplot as plt
from astropy.stats import RipleysKEstimator

Kest = RipleysKEstimator(area=1000*1000, x_max=1000, y_max=1000, x_min=0, y_min=0)
r = np.linspace(0, 240, 100)
vals = []
size = 1000
for i in xrange(size):
  z = np.random.uniform(low=0, high=1000, size=(600, 2))
  vals.append(Kest.Lfunction(data=z, radii=r, mode='ohser')-r) 
  #plt.plot(r, vals[i], color='blue')
vals = np.sort(np.array(vals), axis=0)
high = int(0.01*size)
low = int(0.99*size)-size-1
plt.plot(r, vals[low], color='red', ls='-.')
plt.plot(r, vals[high], color='yellow', ls='-.')
plt.show()
#print vals
