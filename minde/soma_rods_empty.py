
try:
  T
except NameError:
  T = 4
  V1 = 0 #extra nBin in one rod
  V2 = 55 #ratchet rate
  V3 = 1.0 #p

import math
import scipy.constants
import numpy as np

nBinX = int(V1)
nBin = 10+nBinX
binLength = 0.4e-6
filename = "_%d_%d_%.2f" %(int(V1), int(V2), V3)
rodLength = nBin*binLength
VoxelRadius = 2e-8
rodRadius = 0.5e-6
somaRadius = 0.8e-6
nRod = 3
KinesinConc = 2e-7 #in Molar
volumes = [1.6647e-17, 1.6796e-17, 1.6940e-17, 1.7088e-17, 1.7236e-17, 1.7384e-17, 1.7528e-17, 1.7676e-17, 1.7821e-17, 1.7969e-17, 1.8113e-17]
Volume =  volumes[int(V1)]
nKinesin = int(round(KinesinConc*scipy.constants.N_A*1e+3*Volume))
print "Volume:", Volume, "nKinesin:", nKinesin

def rotatePointAlongVector(P, C, N, angle):
  x = P[0]
  y = P[1]
  z = P[2]
  a = C[0]
  b = C[1]
  c = C[2]
  u = N[0]
  v = N[1]
  w = N[2]
  u2 = u*u
  v2 = v*v
  w2 = w*w
  cosT = math.cos(angle)
  oneMinusCosT = 1-cosT
  sinT = math.sin(angle)
  xx = (a*(v2+w2)-u*(b*v+c*w-u*x-v*y-w*z))*oneMinusCosT+x*cosT+(
      -c*v+b*w-w*y+v*z)*sinT
  yy = (b*(u2+w2)-v*(a*u+c*w-u*x-v*y-w*z))*oneMinusCosT+y*cosT+(
      c*u-a*w+w*x-u*z)*sinT
  zz = (c*(u2+v2)-w*(a*u+b*v-u*x-v*y-w*z))*oneMinusCosT+z*cosT+(
      -b*u+a*v-v*x+u*y)*sinT
  return [xx, yy, zz]

angle = math.pi/nRod
vectorZ = [0.0, 0.0, 1.0]
vectorZpoint = [0.0, 0.0, 0.0]
inSomaLength = VoxelRadius*10
rodsLengthX = [rodLength-nBinX*binLength]*nRod
rodsLengthX[nRod-1] = rodLength #longer rod
rodsRotateZ = np.zeros(nRod)
rodsOrigin = np.zeros((nRod, 3))
maxPoint = np.full(3, -np.inf)
minPoint = np.full(3, np.inf)
for i in range(nRod):
  tip = somaRadius+rodsLengthX[i]-inSomaLength+rodRadius*2
  mid = somaRadius+rodsLengthX[i]/2-inSomaLength
  rad = angle+angle*2*i
  rodsRotateZ[i] = -rad
  origin = [mid, 0, 0]
  rodsOrigin[i] = rotatePointAlongVector(origin, vectorZpoint, vectorZ, rad)
  edge = [tip, 0, 0]
  point = rotatePointAlongVector(edge, vectorZpoint, vectorZ, rad)
  maxPoint = np.amax([maxPoint, point], axis=0)
  minPoint = np.amin([minPoint, point], axis=0)

rootLengths = np.subtract(maxPoint, minPoint)
halfRootLengths = np.divide(rootLengths, 2.0)
center = np.subtract(0, np.add(halfRootLengths, minPoint))
with np.errstate(divide='ignore', invalid='ignore'):
  somaOrigin = np.true_divide(center, halfRootLengths)
  somaOrigin[somaOrigin == np.inf] = 0
  somaOrigin = np.nan_to_num(somaOrigin)
for i in range(nRod):
  with np.errstate(divide='ignore', invalid='ignore'):
    rodsOrigin[i] = np.divide(rodsOrigin[i], halfRootLengths)
    rodsOrigin[i][rodsOrigin[i] == np.inf] = 0
    rodsOrigin[i] = np.nan_to_num(rodsOrigin[i])
  rodsOrigin[i] = np.add(rodsOrigin[i], somaOrigin)

sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'

sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = rootLengths[0]
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = rootLengths[1]
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = rodRadius*4+6*VoxelRadius
sim.createEntity('Variable', 'Variable:/:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:ORIGINX').Value = somaOrigin[0]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINY').Value = somaOrigin[1]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINZ').Value = somaOrigin[2]
sim.createEntity('Variable', 'Variable:/Soma:VACANT').Value = -1
sim.createEntity('Variable', 'Variable:/Soma:KIF').Value = nKinesin
sim.createEntity('Variable', 'Variable:/Soma:TUB_GTP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_GTP_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_GTP_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_M' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_P' ).Value = 0

sim.createEntity('System', 'System:/Soma:Membrane').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Membrane:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Membrane:VACANT')

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pKIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dKIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
d.D = 0.5e-12

#Loggers-----------------------------------------------------------------------
v = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:v')
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P']]
v.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP']]
v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:VACANT']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:PlusSensor']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:MinusSensor']]
v.LogInterval = 1

for i in range(nRod):
  sim.createEntity('System', 'System:/:Rod%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Rod%d:GEOMETRY' %i).Value = 2
  x = sim.createEntity('Variable', 'Variable:/Rod%d:LENGTHX' %i)
  x.Value = rodsLengthX[i]
  y = sim.createEntity('Variable', 'Variable:/Rod%d:LENGTHY' %i)
  y.Value = rodRadius*2
  x = sim.createEntity('Variable', 'Variable:/Rod%d:ORIGINX' %i)
  x.Value = rodsOrigin[i][0]
  y = sim.createEntity('Variable', 'Variable:/Rod%d:ORIGINY' %i)
  y.Value = rodsOrigin[i][1]
  sim.createEntity('Variable', 'Variable:/Rod%d:ORIGINZ' %i).Value = 0
  r = sim.createEntity('Variable', 'Variable:/Rod%d:ROTATEZ' %i)
  r.Value = rodsRotateZ[i]
  sim.createEntity('Variable', 'Variable:/Rod%d:VACANT' %i)
  d = sim.createEntity('Variable', 'Variable:/Rod%d:DIFFUSIVE' %i)
  d.Name = '/:Soma'
  # Create the rod membrane:
  sim.createEntity('System', 'System:/Rod%d:Membrane' %i).StepperID = 'SS'
  sim.createEntity('Variable',
      'Variable:/Rod%d/Membrane:DIMENSION' %i).Value = 2
  sim.createEntity('Variable', 'Variable:/Rod%d/Membrane:VACANT' %i)
  sim.createEntity('Variable',
      'Variable:/Rod%d/Membrane:DIFFUSIVE' %i).Name = '/Soma:Membrane'

  h = sim.createEntity('HistogramLogProcess', 'Process:/Rod%d:Histogram' %i)
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:KIF' ]]
  h.Length = rodsLengthX[i]
  h.Radius = rodRadius
  h.Bins = int(round(rodsLengthX[i]/binLength)) 
  h.LogInterval = 1e-2
  h.ExposureTime = 40
  h.FileName = "histogram" + filename + ("_n%d.csv" %i)
  h.LogEnd = T-1
  h.Iterations = 1

run(T)
