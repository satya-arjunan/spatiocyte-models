import numpy as np
import sys

filename = sys.argv[1]
startTime = 10.0

data = np.genfromtxt(filename, delimiter=',', skip_header=1)
print np.mean(data, axis=0, dtype=np.float64)

