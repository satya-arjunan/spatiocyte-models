
try:
  T
except NameError:
  T = 10
  V1 = 7 #nNeuriteMT
  V2 = 55 #ratchet rate
  V3 = 1.0 #p

import math
import scipy.constants
import numpy as np

nBin = 10
binLength = 0.4e-6
filename = "_%d_%d_%.2f_n0.csv" %(int(V1), int(V2), V3)
neuriteLength = nBin*binLength
Filaments = 13
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
neuriteRadius = 0.5e-6
pPlusEnd_Detach = 1
KinesinConc = 2e-7 #in Molar
Volume =  math.pi*pow(neuriteRadius, 2.0)*neuriteLength
nKinesin = int(round(KinesinConc*scipy.constants.N_A*1e+3*Volume))
print "Volume:", Volume, "nKinesin:", nKinesin

nNeuriteMT = V1
EdgeSpace = 25e-9
MTLength = (neuriteLength-2*EdgeSpace)
MTsOriginX = np.zeros(nNeuriteMT)
MTsOriginY = np.zeros(nNeuriteMT)
MTsOriginZ = np.zeros(nNeuriteMT)

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


if(nNeuriteMT == 2):
  space = (neuriteRadius*2-MTRadius*2*2)/(2+2)
  MTsOriginY[0] = -1+(space+MTRadius)/neuriteRadius
  MTsOriginY[1] = 1-(space+MTRadius)/neuriteRadius
elif(nNeuriteMT == 3):
  y = neuriteRadius*math.cos(math.pi/3)
  y2 = y*math.cos(math.pi/3)
  z = y*math.sin(math.pi/3)
  MTsOriginY[0] = y/neuriteRadius
  MTsOriginY[1] = -y2/neuriteRadius
  MTsOriginZ[1] = -z/neuriteRadius
  MTsOriginY[2] = -y2/neuriteRadius
  MTsOriginZ[2] = z/neuriteRadius
elif(nNeuriteMT == 4):
  space = (neuriteRadius*2-MTRadius*2*2)/(2+3)
  MTsOriginY[0] = -1+(space+MTRadius)/neuriteRadius
  MTsOriginY[1] = 1-(space+MTRadius)/neuriteRadius
  space = (neuriteRadius*2-MTRadius*2*2)/(2+3)
  MTsOriginZ[2] = -1+(space+MTRadius)/neuriteRadius
  MTsOriginZ[3] = 1-(space+MTRadius)/neuriteRadius
else:
  MTsOriginY[0] = 2*2.0/6;
  P = [0.0, MTsOriginY[0], 0.0]
  C = [0.0, 0.0, 0.0]
  N = [1.0, 0.0, 0.0]
  angle = 2*math.pi/(nNeuriteMT-1)
  for i in range(nNeuriteMT-2):
    P = rotatePointAlongVector(P, C, N, angle);
    MTsOriginX[i+1] = P[0]
    MTsOriginY[i+1] = P[1]
    MTsOriginZ[i+1] = P[2]


sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 2 #Cylinder
sim.createEntity('Variable', 'Variable:/:ROTATEZ').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = neuriteLength
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = neuriteRadius*2
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:KIF').Value = nKinesin
sim.createEntity('Variable', 'Variable:/:TUB_GTP' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_GTP_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_GTP_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_M' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_P' ).Value = 0

sim.createEntity('System', 'System:/:Membrane').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Membrane:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Membrane:VACANT')
sim.createEntity('Variable', 'Variable:/Membrane:PlusSensor' ).Value = 19504
sim.createEntity('Variable', 'Variable:/Membrane:MinusSensor' ).Value = 19504

#Loggers-----------------------------------------------------------------------
v = sim.createEntity('VisualizationLogProcess', 'Process:/:v')
v.VariableReferenceList = [['_', 'Variable:/:TUB']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_M']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_P']]
v.VariableReferenceList = [['_', 'Variable:/:KIF']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
v.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor']]
v.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor']]
v.LogInterval = 1

h = sim.createEntity('HistogramLogProcess', 'Process:/:h')
h.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
h.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
h.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
h.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
h.VariableReferenceList = [['_', 'Variable:/:KIF' ]]
h.Length = neuriteLength
h.Radius = neuriteRadius
h.Bins = 10
h.LogInterval = 1e-2
h.ExposureTime = 40
h.FileName = "histogram" + filename
h.LogEnd = T-1
h.Iterations = 1
#-------------------------------------------------------------------------------

#Collision----------------------------------------------------------------------
d = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
d.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
d.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor','-1']]
d.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor','1']]
d.p = 1
d.Collision = 3

d = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
d.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
d.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor','-1']]
d.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor','1']]
d.p = 1
d.Collision = 3

i = sim.createEntity('IteratingLogProcess', 'Process:/:iter')
i.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor']]
i.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor']]
i.LogInterval = 1e-2
i.LogEnd = T-1
i.Iterations = 1
i.Collision = 3
i.FileName = "collision" + filename
#-------------------------------------------------------------------------------

#Populate-----------------------------------------------------------------------
p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pPlusSensor')
p.VariableReferenceList = [['_', 'Variable:/Membrane:PlusSensor']]
p.EdgeX = 1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pMinusSensor')
p.VariableReferenceList = [['_', 'Variable:/Membrane:MinusSensor']]
p.EdgeX = -1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_KIF')
p.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]

#p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_GTP')
#p.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
#p.LengthBinFractions = [1, 0.3, 0.8]
#p.Priority = 100 #set high priority for accurate fraction

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pKIF')
p.VariableReferenceList = [['_', 'Variable:/:KIF']]
#-------------------------------------------------------------------------------

#Cytosolic KIF recruitment to microtubule---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b1')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.p = V3

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b2')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.p = 0
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol---------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:detach')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.SearchVacant = 1
r.k = 15

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:detachGTP')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.SearchVacant = 1
r.k = 15
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol at plus end---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p3')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p4')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach
#-------------------------------------------------------------------------------

#KIF ATP hydrolysis-------------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:h1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.SearchVacant = 1
r.k = 100

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:h2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.SearchVacant = 1
r.k = 100
#-------------------------------------------------------------------------------

#KIF ADP phosphorylation--------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:phos1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:phos2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145
#-------------------------------------------------------------------------------

#KIF ratchet biased walk_-------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rat1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','0']] #If BindingSite[1]==TUB
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']] #option 1
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','0']] #Elif BindingSite[1]==TUB_GTP
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']] #option 2
r.BindingSite = 1
r.k = V2

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rat2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]    #A
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]         #C
r.VariableReferenceList = [['_', 'Variable:/:TUB','0']]             #E
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']]     #D
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','0']]         #H
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']] #F
r.BindingSite = 1
r.k = V2
#-------------------------------------------------------------------------------

#KIF random walk between GTP and GDP tubulins-----------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w3')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1
#-------------------------------------------------------------------------------

#KIF normal diffusion-----------------------------------------------------------
d = sim.createEntity('DiffusionProcess', 'Process:/:dKIF')
d.VariableReferenceList = [['_', 'Variable:/:KIF']]
d.D = 0.5e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_KIF')
d.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_GTP_KIF')
d.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------

for i in range(nNeuriteMT):
  m = sim.createEntity('MicrotubuleProcess', 'Process:/:Microtubule%d' %i)
  m.OriginX = MTsOriginX[i]
  m.OriginY = MTsOriginY[i]
  m.OriginZ = MTsOriginZ[i]
  m.RotateX = 0
  m.RotateY = 0
  m.RotateZ = 0
  m.Radius = MTRadius
  m.SubunitRadius = KinesinRadius
  m.Length = MTLength
  m.Filaments = Filaments
  m.Periodic = 0
  m.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP' ]]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
  m.VariableReferenceList = [['_', 'Variable:/:TUB', '-1']]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_M', '-2']]
  m.VariableReferenceList = [['_', 'Variable:/:TUB_P', '-3']]

run(T)
