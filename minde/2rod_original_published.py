
try:
  T
except NameError:
  T = 400
  V1 = 0 #extra nBin in one rod
  V2 = 55 #ratchet rate
  V3 = 1.0 #p

import math
import scipy.constants
import numpy as np

interval = 1

nBinX = int(V1)
nBin = 10+nBinX
binLength = 0.225e-6
filename = "_%d_%d_%.2f" %(int(V1), int(V2), V3)
rodLength = nBin*binLength
VoxelRadius = 1e-8
rodRadius = 0.5e-6
somaRadius = 0.5e-6
nRod = 2

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
inSomaLength = VoxelRadius*10+rodRadius
rodsLengthX = [rodLength-nBinX*binLength]*nRod
rodsLengthX[nRod-1] = rodLength #longer rod
rodsRotateZ = np.zeros(nRod)
rodsOrigin = np.zeros((nRod, 3))
maxPoint = np.full(3, -np.inf)
minPoint = np.full(3, np.inf)
somaAdjRadius = VoxelRadius*5+max(somaRadius, rodRadius)
for i in range(nRod):
  #tip = somaRadius+rodsLengthX[i]-inSomaLength+rodRadius*2
  tip = somaRadius+rodsLengthX[i]+rodRadius
  mid = somaRadius+rodsLengthX[i]/2-inSomaLength
  #rad = angle+angle*2*i
  rad = angle*2*i
  rodsRotateZ[i] = -rad
  origin = [mid, 0, 0]
  rodsOrigin[i] = rotatePointAlongVector(origin, vectorZpoint, vectorZ, rad)
  edge = [tip, rodRadius, 0]
  point = rotatePointAlongVector(edge, vectorZpoint, vectorZ, rad)
  maxPoint = np.amax([maxPoint, point], axis=0)
  minPoint = np.amin([minPoint, point], axis=0)

maxPoint = np.amax([maxPoint, [somaAdjRadius, somaAdjRadius, somaAdjRadius]], axis=0)
minPoint = np.amin([minPoint, [-somaAdjRadius, -somaAdjRadius, -somaAdjRadius]], axis=0)

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
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = VoxelRadius
s.SearchVacant = 1
#s.RemoveSurfaceBias = 1
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

sim.createEntity('System', 'System:/Soma:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Surface:VACANT')

for i in range(nRod):
  sim.createEntity('System', 'System:/:Rod%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Rod%d:GEOMETRY' %i).Value = 3
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
  sim.createEntity('System', 'System:/Rod%d:Surface' %i).StepperID = 'SS'
  sim.createEntity('Variable',
      'Variable:/Rod%d/Surface:DIMENSION' %i).Value = 2
  sim.createEntity('Variable', 'Variable:/Rod%d/Surface:VACANT' %i)
  sim.createEntity('Variable',
      'Variable:/Rod%d/Surface:DIFFUSIVE' %i).Name = '/Soma:Surface'

  h = sim.createEntity('HistogramLogProcess', 'Process:/Rod%d:Histogram' %i)
  h.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:MinEE' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE' ]]
#  if(i == 2):
#    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:A', '-2']]
#    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:C', '-3']]
#    h.VariableReferenceList = [['_', 'Variable:/Soma:B', '-1']]
  h.Density = 1
  h.Length = rodsLengthX[i]
  h.Radius = rodRadius*1.5
  #h.Bins = int(round(rodsLengthX[i]/binLength))/2 
  h.Bins = 10
  h.LogInterval = interval/10.0
  h.ExposureTime = interval
  h.FileName = "histogram" + filename + ("_n%d.csv" %i)
  h.LogEnd = T-1
  h.Iterations = 1

sim.createEntity('Variable', 'Variable:/Soma:MinDatp').Value = 0
sim.createEntity('Variable', 'Variable:/Soma:MinDadp').Value = 1300
sim.createEntity('Variable', 'Variable:/Soma:MinEE').Value = 0
sim.createEntity('Variable', 'Variable:/Soma:B').Value = 0

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:diffuseMinDatp')
d.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp']]
d.D = 16e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:diffuseMinDadp')
d.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp']]
d.D = 16e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:diffuseMinE')
d.VariableReferenceList = [['_', 'Variable:/Soma:MinEE']]
d.D = 10e-12

l = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:logger')
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE']]
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE']]
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED']]
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD']]
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:VACANT']]
#l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:A']]
#l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:C']]
#l.VariableReferenceList = [['_', 'Variable:/Soma:B']]
l.LogInterval = 0.5

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pop')
p.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp']]
p.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp']]
p.VariableReferenceList = [['_', 'Variable:/Soma:MinEE']]
p.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE']]
p.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE']]
p.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED']]
p.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD']]


sim.createEntity('Variable', 'Variable:/Soma/Surface:MinD').Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:MinEE').Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:MinDEE').Value = 700
sim.createEntity('Variable', 'Variable:/Soma/Surface:MinDEED').Value = 0
#sim.createEntity('Variable', 'Variable:/Soma/Surface:A').Value = 0
#sim.createEntity('Variable', 'Variable:/Soma/Surface:C').Value = 0

diffuser = sim.createEntity('DiffusionProcess', 'Process:/:diffuseMinD')
diffuser.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD']]
diffuser.D = 0.02e-12

diffuser = sim.createEntity('DiffusionProcess', 'Process:/:diffuseMinEE')
diffuser.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE']]
diffuser.D = 0.02e-12

diffuser = sim.createEntity('DiffusionProcess', 'Process:/:diffuseMinDEE')
diffuser.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE']]
diffuser.D = 0.02e-12

diffuser = sim.createEntity('DiffusionProcess', 'Process:/:diffuseMinDEED')
diffuser.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED']]
diffuser.D = 0.02e-12

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:VACANT','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','1']]
r.k = 2.2e-8

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','1']]
r.k = 3e-20

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE','1']]
r.k = 5e-19

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp','1']]
r.k = 1

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r5')
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDatp','1']]
r.k = 5

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED','1']]
r.k = 5e-15

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r7')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEED','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinDEE','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp','1']]
r.k = 1

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r8')
r.VariableReferenceList = [['_', 'Variable:/Soma/Surface:MinEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:MinEE','1']]
r.k = 0.83

run(T)
