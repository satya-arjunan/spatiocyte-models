import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os
import pylab as P
from astropy.stats import RipleysKEstimator
from matplotlib import pyplot as plt 

labelFontSize = 14
tickFontSize = 14
legendFontSize = 14
lineFontSize = 14

fileNames = ["CoordinateLog.csv"]
legendTitles = []
lines = ['-', '-', '-', '-']
colors = ['y', 'r', 'b', 'm', 'c', 'g']

max_frames = 2000

for i in range(len(fileNames)):
  f = open(fileNames[i], 'r')
  legendTitles = f.readline().strip().split(",")
  logInterval = float(legendTitles[0].split("=")[1])
  len_x = float(legendTitles[1].split("=")[1])
  len_y = float(legendTitles[2].split("=")[1])
  len_z = float(legendTitles[3].split("=")[1])
  voxelRadius = float(legendTitles[4].split("=")[1])
  scale = voxelRadius*2
  speciesNames = []
  speciesRadii = []
  for j in range(len(legendTitles)-5):
    speciesNames.append(legendTitles[j+5].split("=")[0])
    speciesRadii.append(float(legendTitles[j+5].split("=")[1]))
  speciesSize = len(speciesNames)
  logCnt = 0
  lineCnt = 0
  markers = []
  frameCnt = 0
  for line in f:
    frameCnt = frameCnt + 1
    if frameCnt > max_frames*speciesSize:
      break
    coords = line.strip().split(",")
    time = float(coords[0])
    y = []
    z = []
    for l in range((len(coords)-1)/3):
      y.append(float(coords[l*3+2])*scale*1e+9)
      z.append(float(coords[l*3+3])*scale*1e+9)
    lineCnt = lineCnt + 1
    data = np.column_stack((y,z))
    if lineCnt == speciesSize:
      x_max = max(z)
      x_min = min(z)
      y_max = max(y)
      y_min = min(y)
      area = (x_max-x_min)*(y_max-y_min)
      Kest = RipleysKEstimator(area=area, x_max=x_max, y_max=y_max,
          x_min=x_min, y_min=y_min)
      r = np.linspace(0, 240e-9*1e+9, 80)
      plt.plot(r, Kest.Lfunction(data=data, radii=r, mode='ohser')-r)
      fileName = fileNames[i]+'.%03d.png'%logCnt
      print 'Saving frame', fileName
      plt.savefig(fileName)
      plt.cla()
      logCnt = logCnt + 1
      lineCnt = 0

#os.system("ffmpeg -i " + fileNames[0] + ".%03d.png -vcodec qtrle " + 
#    fileNames[0] + ".mov")



