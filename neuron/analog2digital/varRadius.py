
try:
  T
except NameError:
  T = 54000
  V1 = 80 #percentage increase in all except one neurite radius
  V2 = 0.00002 #p TUB
  V3 = 0.8 #p aTUB

import math
import scipy.constants
import numpy as np

binLength = 0.4e-6
nBinX = 0
nBin = 10+(round(int(5e-6/binLength))-10)
filename = "_%d_%d_%.2f" %(int(V1), int(V2), V3)
neuriteLength = nBin*binLength
Filaments = 13
MTRadius = 12.5e-9
#VoxelRadius = 0.7e-8 #(actual value used)
VoxelRadius = 1e-8
KinesinRadius = 0.4e-8
neuriteRadius = 0.2e-6
somaRadius = 1.3e-6
nNeurite = 4
pPlusEnd_Detach = 1
KinesinConc = 2e-7 #in Molar
volumes = [5.8822e-18, 6.5798e-18, 7.2979e-18, 8.0669e-18, 8.8546e-18, 9.6954e-18, 1.0553e-17, 1.1466e-17, 1.2395e-17, 1.3378e-17, 1.4378e-17]
Volume = [9.6945e-18]
#Volume =  math.pi*pow(neuriteRadius, 2.0)*neuriteLength*nNeurite
#Volume =  volumes[int(V1)/10]
#nKinesin = int(round(KinesinConc*scipy.constants.N_A*1e+3*Volume))
nKinesin = 35*volumes[int(V1)/10]/volumes[0]
print "nKinesin:", nKinesin

nNeuriteMT = 5
EdgeSpace = 25e-9

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

angle = math.pi/nNeurite
vectorZ = [0.0, 0.0, 1.0]
vectorZpoint = [0.0, 0.0, 0.0]
inSomaLength = VoxelRadius*30
neuritesLengthX = [neuriteLength-nBinX*binLength]*nNeurite
neuritesLengthX[nNeurite-1] = neuriteLength #longer neurite
maxNeuriteRadius = neuriteRadius*(1.0+V1/100.0)
neuriteRadii = [maxNeuriteRadius]*nNeurite
neuriteRadii[nNeurite-1] = neuriteRadius
neuritesRotateZ = np.zeros(nNeurite)
neuritesOrigin = np.zeros((nNeurite, 3))
maxPoint = np.full(3, -np.inf)
minPoint = np.full(3, np.inf)
for i in range(nNeurite):
  tip = somaRadius+neuritesLengthX[i]-inSomaLength+maxNeuriteRadius
  mid = somaRadius+neuritesLengthX[i]/2-inSomaLength
  rad = angle+angle*2*i
  neuritesRotateZ[i] = -rad
  origin = [mid, 0, 0]
  neuritesOrigin[i] = rotatePointAlongVector(origin, vectorZpoint, vectorZ, rad)
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
for i in range(nNeurite):
  with np.errstate(divide='ignore', invalid='ignore'):
    neuritesOrigin[i] = np.divide(neuritesOrigin[i], halfRootLengths)
    neuritesOrigin[i][neuritesOrigin[i] == np.inf] = 0
    neuritesOrigin[i] = np.nan_to_num(neuritesOrigin[i])
  neuritesOrigin[i] = np.add(neuritesOrigin[i], somaOrigin)

MTLengths = np.zeros(nNeurite)
for i in range(len(neuritesLengthX)):
  MTLengths[i] = neuritesLengthX[i]-2*EdgeSpace
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
      if(i == 0):
          P = rotatePointAlongVector(P, C, N, angle/2);
      else:
          P = rotatePointAlongVector(P, C, N, angle);
      MTsOriginX[i][j+1] = P[0]
      MTsOriginY[i][j+1] = P[1]
      MTsOriginZ[i][j+1] = P[2]

sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'

sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = rootLengths[0]
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = rootLengths[1]
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = maxNeuriteRadius*4+6*VoxelRadius
sim.createEntity('Variable', 'Variable:/:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = maxNeuriteRadius*4
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
sim.createEntity('Variable', 'Variable:/Soma:aTUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_M' ).Value = 0
sim.createEntity('Variable', 'Variable:/Soma:TUB_P' ).Value = 0

sim.createEntity('System', 'System:/Soma:Membrane').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Membrane:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Membrane:VACANT')
#sim.createEntity('Variable', 'Variable:/Soma/Membrane:PlusSensor' ).Value = 7440
#sim.createEntity('Variable', 'Variable:/Soma/Membrane:MinusSensor' ).Value = 7440

#Loggers-----------------------------------------------------------------------
v = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:v')
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB']]
v.VariableReferenceList = [['_', 'Variable:/Soma:aTUB']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P']]
v.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:VACANT']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:PlusSensor']]
#v.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:MinusSensor']]
v.LogInterval = 10
v.FileName = "visual" + filename + ".dat"

m = sim.createEntity('MicroscopyTrackingProcess', 'Process:/Soma:m')
m.VariableReferenceList = [['_', 'Variable:/Soma:KIF', '1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF', '1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP', '1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF', '-1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF', '-1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF', '-1']]
m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF', '12500']]
m.LogInterval = 1
m.ExposureTime = 60
m.FileName = "micro" + filename + ".dat"
#-------------------------------------------------------------------------------

#Collision----------------------------------------------------------------------
#d = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:r3')
#d.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
#d.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor','-1']]
#d.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor','1']]
#d.p = 1
#d.Collision = 3
#
#d = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:r4')
#d.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
#d.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor','-1']]
#d.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor','1']]
#d.p = 1
#d.Collision = 3
#
#i = sim.createEntity('IteratingLogProcess', 'Process:/Soma:iter')
#i.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor']]
#i.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor']]
#i.LogInterval = 1e-2
#i.LogEnd = T-1
#i.Iterations = 1
#i.Collision = 3
#i.FileName = "collision" + filename
#-------------------------------------------------------------------------------

#Populate-----------------------------------------------------------------------
#p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pPlusSensor')
#p.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:PlusSensor']]
#p.EdgeX = 1
#
#p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pMinusSensor')
#p.VariableReferenceList = [['_', 'Variable:/Soma/Membrane:MinusSensor']]
#p.EdgeX = -1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pTUB_KIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF']]

#p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pTUB_GTP')
#p.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP']]
#p.LengthBinFractions = [1, 0.3, 0.8]
#p.Priority = 100 #set high priority for accurate fraction

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pKIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
#-------------------------------------------------------------------------------

#Cytosolic KIF recruitment to microtubule---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b1')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','1']]
r.p = 0.00001

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b2')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','1']]
r.p = 0

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b3')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','1']]
r.p = 0.9
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol---------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:detach')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.SearchVacant = 1
r.k = 15

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:detachGTP')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.SearchVacant = 1
r.k = 15
#-------------------------------------------------------------------------------

#Active tubulin inactivation----------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:i1')
r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
r.k = 0.055
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol at plus end---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p3')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:p4')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','1']]
r.p = pPlusEnd_Detach
#-------------------------------------------------------------------------------

#KIF ATP hydrolysis-------------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:h1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','1']]
r.SearchVacant = 1
r.k = 100

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:h2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','1']]
r.SearchVacant = 1
r.k = 100
#-------------------------------------------------------------------------------

#KIF ADP phosphorylation--------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:phos1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:phos2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145
#-------------------------------------------------------------------------------

#KIF ratchet biased walk_-------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:rat1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','0']] #If BindingSite[1]==TUB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']] #option 1
r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','0']] #Elif BindingSite[1]==TUB_GTP
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']] #option 2
r.BindingSite = 1
r.k = 55

#r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:rat1')
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:aTUB','1']]
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','0']] #If BindingSite[1]==TUB
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']] #option 1
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','0']] #Elif BindingSite[1]==TUB_GTP
#r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','1']] #option 2
#r.BindingSite = 1
#r.k = 55

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:rat2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','-1']]    #A
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]         #C
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','0']]             #E
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']]     #D
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','0']]         #H
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','1']] #F
r.BindingSite = 1
r.k = 55
#-------------------------------------------------------------------------------

#KIF random walk between GTP and GDP tubulins-----------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:w1')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:w2')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:w3')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1
#-------------------------------------------------------------------------------

#KIF normal diffusion-----------------------------------------------------------
d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dKIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
d.D = 0.5e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dTUB_KIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF']]
d.VariableReferenceList = [['_', 'Variable:/Soma:aTUB', '1']]
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dTUB_GTP_KIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------

nSomaMT = 16
somaMTrotateAngle = math.pi*2/max(1.0, nSomaMT)
somaMTorigin = [0.5, 0.0, 0.0]
somaMTvectorZ = [0.0, 0.0, 1.0]
somaMTvectorZpoint = [0.0, 0.0, 0.0]
for i in range(nSomaMT):
  for j in range(3):
    startAngle = math.pi/3.3
    OriginZ = 0.0
    if(j != 0):
      startAngle = math.pi/2
      if(j == 1):
        OriginZ = 0.5 
      else:
        OriginZ = -0.5 
    m = theSimulator.createEntity('MicrotubuleProcess', 'Process:/Soma:Microtubule%d%d' %(i,j))
    P = rotatePointAlongVector(somaMTorigin, somaMTvectorZpoint, somaMTvectorZ, somaMTrotateAngle*i+startAngle)
    m.OriginX = P[0]
    m.OriginY = P[1]
    m.OriginZ = OriginZ
    m.RotateX = 0
    m.RotateY = 0
    m.RotateZ =  somaMTrotateAngle*i+startAngle
    m.Radius = MTRadius
    m.SubunitRadius = KinesinRadius
    m.Length = somaRadius*0.7
    m.Filaments = Filaments
    m.Periodic = 0
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:aTUB']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB', '-1']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M', '-2']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P', '-3']]

for i in range(nNeurite):
  sim.createEntity('System', 'System:/:Neurite%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Neurite%d:GEOMETRY' %i).Value = 2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHX' %i)
  x.Value = neuritesLengthX[i]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHY' %i)
  y.Value = neuriteRadii[i]*2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINX' %i)
  x.Value = neuritesOrigin[i][0]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINY' %i)
  y.Value = neuritesOrigin[i][1]
  sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINZ' %i).Value = 0
  r = sim.createEntity('Variable', 'Variable:/Neurite%d:ROTATEZ' %i)
  r.Value = neuritesRotateZ[i]
  sim.createEntity('Variable', 'Variable:/Neurite%d:VACANT' %i)
  d = sim.createEntity('Variable', 'Variable:/Neurite%d:DIFFUSIVE' %i)
  d.Name = '/:Soma'
  # Create the neurite membrane:
  sim.createEntity('System', 'System:/Neurite%d:Membrane' %i).StepperID = 'SS'
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Membrane:DIMENSION' %i).Value = 2
  sim.createEntity('Variable', 'Variable:/Neurite%d/Membrane:VACANT' %i)
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Membrane:DIFFUSIVE' %i).Name = '/Soma:Membrane'

  h = sim.createEntity('HistogramLogProcess', 'Process:/Neurite%d:Histogram' %i)
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:KIF' ]]
  h.Length = neuritesLengthX[i]
  h.Radius = neuriteRadii[i]
  h.Bins = int(round(neuritesLengthX[i]/binLength)) 
  h.LogInterval = 1e-2
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
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:aTUB']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB', '-1']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M', '-2']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P', '-3']]

run(T)
