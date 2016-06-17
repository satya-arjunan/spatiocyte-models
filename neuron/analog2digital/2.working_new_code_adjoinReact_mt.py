

try:
  T
except NameError:
  T = 540000
  V1 = 290 #nKinesin
  V2 = 0 #iteration
  V3 = 0.8 #p aTUB

import numpy as np
import math

filename = "_%d_%d_" %(int(V1), int(V2))
#volumes = [5.8822e-18]
#nKinesin = 35*2.258e-17/volumes[0]
#80 at 2 hr
binLength = 5e-6/5
nKinesin = V1
pPlusEnd_Detach = 1
VoxelRadius = 0.8e-8
nNeurite = 5
nNeuriteMT = 5
EdgeSpace = VoxelRadius*5
neuriteRadius = 0.2e-6
MTRadius = 12.5e-9
KinesinRadius = VoxelRadius/2
Filaments = 13
neuriteSpace = neuriteRadius*2
somaLength = nNeurite*neuriteRadius*2+neuriteSpace*(nNeurite+1)
somaWidth = somaLength
somaHeight = neuriteRadius*4
inSomaLength = VoxelRadius*6
neuriteLengths = np.empty((nNeurite))
neuriteLengths.fill(5e-6+inSomaLength)
neuriteLengths[0] = 25e-6
neuriteLengths[1] = 20e-6
neuriteLengths[2] = 15e-6
neuriteLengths[3] = 10e-6
neuriteLengths[4] = 5e-6
rootSpace = VoxelRadius*20
rootLengths = np.empty((1,3))
rootLengths = (somaWidth+np.amax(neuriteLengths)-inSomaLength+rootSpace*2,
    somaLength+rootSpace*2, somaHeight+rootSpace*2)
neuriteOrigins = np.zeros((nNeurite, 3))
halfRootLengths = np.divide(rootLengths, 2.0)
somaOrigin = np.zeros((nNeurite, 3))
somaOrigin = (rootSpace+somaWidth/2, rootSpace+somaLength/2,
    rootSpace+somaHeight/2)
with np.errstate(divide='ignore', invalid='ignore'):
  somaOrigin = np.divide(np.subtract(somaOrigin, halfRootLengths),
      halfRootLengths)
  somaOrigin[somaOrigin == np.inf] = 0
  somaOrigin = np.nan_to_num(somaOrigin)

for i in range(nNeurite):
  neuriteOrigins[i] = np.array([rootSpace+somaWidth+(neuriteLengths[i]-
    inSomaLength)/2, 
    rootSpace+neuriteSpace+i*(neuriteRadius*2+neuriteSpace)+neuriteRadius,
    rootSpace+somaHeight/2])
  with np.errstate(divide='ignore', invalid='ignore'):
    neuriteOrigins[i] = np.divide(np.subtract(neuriteOrigins[i],
      halfRootLengths), halfRootLengths)
    neuriteOrigins[i][neuriteOrigins[i] == np.inf] = 0
    neuriteOrigins[i] = np.nan_to_num(neuriteOrigins[i])


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


MTLengths = np.zeros(nNeurite)
for i in range(len(neuriteLengths)):
  MTLengths[i] = neuriteLengths[i]-2*EdgeSpace-inSomaLength
MTsOriginX = np.zeros((nNeurite, nNeuriteMT))
MTsOriginY = np.zeros((nNeurite, nNeuriteMT))
MTsOriginZ = np.zeros((nNeurite, nNeuriteMT))

for i in range(nNeurite):
  if(nNeuriteMT == 1):
    MTsOriginX[i][0] = 0.0
    MTsOriginY[i][0] = 0.0
    MTsOriginZ[i][0] = 0.0
  elif(nNeuriteMT == 2):
    space = (neuriteRadii[i]*2-MTRadius*2*2)/(2+2)
    MTsOriginY[i][0] = -1+(space+MTRadius)/neuriteRadii[i]
    MTsOriginY[i][1] = 1-(space+MTRadius)/neuriteRadii[i]
  elif(nNeuriteMT == 3):
    y = neuriteRadii[i]*math.cos(math.pi/3)
    y2 = y*math.cos(math.pi/3)
    z = y*math.sin(math.pi/3)
    MTsOriginY[i][0] = y/neuriteRadii[i]
    MTsOriginY[i][1] = -y2/neuriteRadii[i]
    MTsOriginZ[i][1] = -z/neuriteRadii[i]
    MTsOriginY[i][2] = -y2/neuriteRadii[i]
    MTsOriginZ[i][2] = z/neuriteRadii[i]
  elif(nNeuriteMT == 4):
    space = (neuriteRadius*2-MTRadius*2*2)/(2+3)
    MTsOriginY[i][0] = -1+(space+MTRadius)/neuriteRadii[i]
    MTsOriginY[i][1] = 1-(space+MTRadius)/neuriteRadii[i]
    space = (neuriteRadius*2-MTRadius*2*2)/(2+3)
    MTsOriginZ[i][2] = -1+(space+MTRadius)/neuriteRadii[i]
    MTsOriginZ[i][3] = 1-(space+MTRadius)/neuriteRadii[i]
  else:
    MTsOriginY[i][0] = 2*2.0/6;
    P = [0.0, MTsOriginY[i][0], 0.0]
    C = [0.0, 0.0, 0.0]
    N = [1.0, 0.0, 0.0]
    angle = 2*math.pi/(nNeuriteMT-1)
    for j in range(nNeuriteMT-2):
      P = rotatePointAlongVector(P, C, N, angle);
      MTsOriginX[i][j+1] = P[0]
      MTsOriginY[i][j+1] = P[1]
      MTsOriginZ[i][j+1] = P[2]

ka0_v = 2.9557e-22
ka1_v = 5.9115e-22
ka2_v = 1.1823e-21

kd0 = 0.001667
kd1 = 0.000667
kd2 = 0.000267

p1 = 0.00001
p2 = 0.9

kd0 = 15
kd1 = 15
kd2 = 15

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = VoxelRadius
s.SearchVacant = 1
s.RemoveSurfaceBias = 1
sim.rootSystem.StepperID = 'SS'

sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = rootLengths[0]
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = rootLengths[1]
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = rootLengths[2]
sim.createEntity('Variable', 'Variable:/:VACANT')

#sim.createEntity('System', 'System:/:Surface').StepperID = 'SS'
#sim.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
#sim.createEntity('Variable', 'Variable:/Surface:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaWidth
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaLength
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = somaHeight
sim.createEntity('Variable', 'Variable:/Soma:ORIGINX').Value = somaOrigin[0]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINY').Value = somaOrigin[1]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINZ').Value = somaOrigin[2]
sim.createEntity('Variable', 'Variable:/Soma:VACANT').Value = -1

sim.createEntity('System', 'System:/Soma:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Surface:VACANT')

for i in range(nNeurite):
  sim.createEntity('System', 'System:/:Neurite%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Neurite%d:GEOMETRY' %i).Value = 2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHX' %i)
  x.Value = neuriteLengths[i]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHY' %i)
  y.Value = neuriteRadius*2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINX' %i)
  x.Value = neuriteOrigins[i][0]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINY' %i)
  y.Value = neuriteOrigins[i][1]
  sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINZ' %i).Value = 0
  sim.createEntity('Variable', 'Variable:/Neurite%d:VACANT' %i)
  d = sim.createEntity('Variable', 'Variable:/Neurite%d:DIFFUSIVE' %i)
  d.Name = '/:Soma'
  # Create the neurite membrane:
  sim.createEntity('System', 'System:/Neurite%d:Surface' %i).StepperID = 'SS'
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Surface:DIMENSION' %i).Value = 2
  sim.createEntity('Variable', 'Variable:/Neurite%d/Surface:VACANT' %i)
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Surface:DIFFUSIVE' %i).Name = '/Soma:Surface'


  h = sim.createEntity('HistogramLogProcess', 'Process:/Neurite%d:Histogram' %i)
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP']]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP']]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP']]
  h.VariableReferenceList = [['_', 'Variable:/Soma:KIF' ]]
  if(i == 0):
    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:A', '-3']]
    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:B', '-4']]
  if(i == 1):
    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:C', '-3']]
    h.VariableReferenceList = [['_', 'Variable:/Soma/Surface:D', '-4']]
  h.OriginX = inSomaLength/(neuriteLengths[i]/2)
  h.Density = 1
  h.Length = neuriteLengths[i]
  h.Radius = neuriteRadius*1.2
  h.Bins = int(round(neuriteLengths[i]/binLength)) 
  h.LogInterval = 1e-1
  h.ExposureTime = 40
  h.FileName = "histogram" + filename + ("_n%d.csv" %i)
  h.LogEnd = T-1
  h.Iterations = 1

  for j in range(nNeuriteMT):
    m = sim.createEntity('MicrotubuleProcess',
        'Process:/Neurite%d:Microtubule%d' %(i, j))
    m.OriginX = MTsOriginX[i][j]
    m.OriginY = MTsOriginY[i][j]
    m.OriginZ = MTsOriginZ[i][j]
    m.RotateX = 0
    m.RotateY = 0
    m.RotateZ = 0
    m.Radius = MTRadius
    m.SubunitRadius = KinesinRadius
    m.Length = MTLengths[i]
    m.Filaments = Filaments
    m.Periodic = 0
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB0' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB1' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB2' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB', '-1']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M', '-2']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P', '-3']]



nSomaMT = 16
mtSpaceY = somaLength/(nSomaMT)
for i in range(nSomaMT):
  for j in range(3):
    OriginZ = 0.0
    if(j != 0):
      if(j == 1):
        OriginZ = 0.5 
      else:
        OriginZ = -0.5 
    m = theSimulator.createEntity('MicrotubuleProcess',
        'Process:/Soma:Microtubule%d%d' %(i,j))
    m.OriginX = 0
    m.OriginY = (mtSpaceY/2+i*mtSpaceY)/(somaLength/2)-1
    m.OriginZ = OriginZ
    m.RotateX = 0
    m.RotateY = 0
    m.RotateZ = 0
    m.Radius = MTRadius
    m.SubunitRadius = KinesinRadius
    m.Length = somaWidth*0.8
    m.Filaments = Filaments
    m.Periodic = 0
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB0' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB1' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB2' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB', '-1']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M', '-2']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P', '-3']]


sim.createEntity('Variable', 'Variable:/Soma:KIF').Value = nKinesin
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF0' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF1' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF2' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF0_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF1_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_KIF2_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB0' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB1' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB2' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_M' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_P' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:A').Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:B').Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:C').Value = 0
sim.createEntity('Variable', 'Variable:/Soma/Surface:D').Value = 0


#Populate-----------------------------------------------------------------------
p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pKIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
#-------------------------------------------------------------------------------

#Cytosolic KIF recruitment to microtubule---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b1')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.RandomC = 0
#r.k = ka0_vf
#r.k = ka0_v
r.p = p1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b2')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.RandomC = 0
#r.k = ka0_v
r.p = p2

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b3')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.RandomC = 0
#r.k = ka1_v
r.p = p2

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b4')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.RandomC = 0
#r.k = ka2_v
r.p = p2
#------------------------------------------------------------------------------

#MT KIF detachment to cytosol---------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:r1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
r.k = kd0

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:r2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
r.k = kd1

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:r3')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
r.k = kd2
#-------------------------------------------------------------------------------


# WalkReact --------------------------------------------------------------------
# | TUB1/TUB2 | KIF0 | TUB1 | TUB/TUB0/TUB1 | ->
# | TUB0/TUB1 | TUB1 | KIF0 | TUB1/TUB1/TUB2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:d5')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.ForcedSequence = 1
r.p = 1

# | TUB1/TUB2 | KIF0 | TUB2 | KIF0/KIF1 | ->
# | TUB0/TUB1 | TUB1 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:d6')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.ForcedSequence = 1
r.p = 1
#
# | KIF1/KIF2 | KIF1 | TUB1 | TUB/TUB0/TUB1 | ->
# | KIF0/KIF1 | TUB2 | KIF0 | TUB1/TUB1/TUB2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:d7')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.ForcedSequence = 1
r.p = 1
#
# | KIF1/KIF2 | KIF1 | TUB2 | KIF0/KIF1 | ->
# | KIF0/KIF1 | TUB2 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:d8')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.ForcedSequence = 1
r.p = 1
#-------------------------------------------------------------------------------

#Active tubulin inactivation----------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:d9')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
r.k = 0.055
#-------------------------------------------------------------------------------

##MT KIF detachment to cytosol at plus end---------------------------------------
#r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p3')
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
#r.p = pPlusEnd_Detach
#
#r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p4')
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
#r.p = pPlusEnd_Detach
##-------------------------------------------------------------------------------

#KIF ATP hydrolysis-------------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:h1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','1']]
r.k = 100

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:h2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','1']]
r.k = 100

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:h3')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','1']]
r.k = 100
#-------------------------------------------------------------------------------


#KIF ADP phosphorylation--------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:phos1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','1']]
r.k = 145

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:phos2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','1']]
r.k = 145

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:phos3')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','1']]
r.k = 145
#-------------------------------------------------------------------------------


#KIF ratchet biased walk_-------------------------------------------------------
# | TUB1/TUB2 | KIF0 | TUB1 | TUB/TUB0/TUB1 | ->
# | TUB0/TUB1 | TUB1 | KIF0 | TUB1/TUB1/TUB2 |

# | TUB1/TUB2 | KIF0 | TUB2 | KIF0/KIF1 | ->
# | TUB0/TUB1 | TUB1 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:rat1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-1']] #A
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','1']]      #C
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','0']] #If BindingSite[1]==TUB1 #E
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','1']] #option 1      #D
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','0']] #Elif BindingSite[1]==TUB2 #H
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','1']] #option 2      #F
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.BindingSite = 1
r.k = 55

# | KIF1/KIF2 | KIF1 | TUB1 | TUB/TUB0/TUB1 | ->
# | KIF0/KIF1 | TUB2 | KIF0 | TUB1/TUB1/TUB2 |

# | KIF1/KIF2 | KIF1 | TUB2 | KIF0/KIF1 | ->
# | KIF0/KIF1 | TUB2 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:rat2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','0']] #If BindingSite[1]==TUB1
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','1']] #option 1
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','0']] #Elif BindingSite[1]==TUB2
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','1']] #option 2
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','-10']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP','-20']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP','20']]
r.BindingSite = 1
r.k = 55
#-------------------------------------------------------------------------------

#KIF normal diffusion-----------------------------------------------------------
d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dKIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
d.D = 0.5e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dTUB_KIF0')
d.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0']]
d.WalkReact = 1
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dTUB_KIF1')
d.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------

v = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:v')
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB0']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB1']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB2']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Surface:A']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Surface:B']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Surface:C']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Surface:D']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Surface:VACANT']]
v.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0_ATP']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1_ATP']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2_ATP']]
#v.VariableReferenceList = [['_', 'Variable:/Neurite0:Interface']]
v.LogInterval = 10
#v.FileName = "visual" + filename + ".dat"


#l = theSimulator.createEntity('IteratingLogProcess', 'Process:/Soma:iter')
#l.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF0']]
#l.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF1']]
#l.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF2']]
#l.LogInterval = 1e-1
#l.LogEnd = T-1
#l.Iterations = 1
#l.FileName = "IterateLog.9pM.csv"

run(T)

