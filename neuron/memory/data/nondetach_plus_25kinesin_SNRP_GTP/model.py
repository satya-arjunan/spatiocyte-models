
try:
  T
except NameError:
  T = 1000
  V1 = 0.0
  V2 = 0.5
  V3 = 0.0
  V4 = 0.0
  filename = "histogram"

import math
duration = T
Filaments = 13
RotateAngle = math.pi
MTRadius = 12.5e-9
VoxelRadius = 1.5e-8
KinesinRadius = 0.7e-8
neuriteRadius = 0.2e-6
neuriteLength = 5e-6
somaRadius = 1.3e-6
MTLength = neuriteLength*0.95


sim = theSimulator

sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius

sim.rootSystem.StepperID = 'SS'
x = sim.createEntity('Variable', 'Variable:/:LENGTHX')
x.Value = somaRadius*2+neuriteLength*2
y = sim.createEntity('Variable', 'Variable:/:LENGTHY')
y.Value = somaRadius*2+neuriteLength*2
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value =neuriteRadius*4.5
sim.createEntity('Variable', 'Variable:/:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = neuriteRadius*4
sim.createEntity('Variable', 'Variable:/Soma:VACANT').Value = -1
sim.createEntity('Variable', 'Variable:/Soma:KIF').Value = 25
sim.createEntity('Variable', 'Variable:/Soma:TUB_GTP' ).Value = 1
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

#Populate-----------------------------------------------------------------------
p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pTUB_KIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF']]

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pTUB_GTP')
p.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP']]
p.LengthBinFractions = [V1, V2, V3, V4]
p.Priority = 100 #set high priority for accurate fraction

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pKIF')
p.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
#-------------------------------------------------------------------------------

#Cytosolic KIF recruitment to microtubule---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b1')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF','1']]
r.p = 0.333

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Soma:b2')
r.VariableReferenceList = [['_', 'Variable:/Soma:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF','1']]
r.p = 1
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol---------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Soma:detach')
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
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
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','1']]
#if BindingSite[1]==TUB
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB','0']]
#set product as
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP','1']]
#else if BindingSite[1]==TUB_GTP
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP','0']]
#set product as
r.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP','1']]
r.BindingSite = 1
r.k = 55

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
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:dTUB_GTP_KIF')
d.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------


#v = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:v')
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB']]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M']]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P']]
#v.VariableReferenceList = [['_', 'Variable:/Soma:KIF']]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
#v.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP']]
#v.LogInterval = 1

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

somaMTs = 0
somaMTrotateAngle = math.pi*2/max(1.0,somaMTs)
somaMTorigin = [0.5, 0.0, 0.0]
somaMTvectorZ = [0.0, 0.0, 1.0]
somaMTvectorZpoint = [0.0, 0.0, 0.0]
for i in range(somaMTs):
  if(i==0):
    for j in range(3):
      if(j==0):
        startAngle = math.pi/3.3
        OriginZ = 0.0
        if(j != 0):
          startAngle = math.pi/2
          if(j == 1):
            OriginZ = 0.5 
          else:
            OriginZ = -0.5 
        m = sim.createEntity('MicrotubuleProcess',
            'Process:/Soma:Microtubule%d%d' %(i,j))
        P = rotatePointAlongVector(somaMTorigin, somaMTvectorZpoint,
            somaMTvectorZ, somaMTrotateAngle*i+startAngle)
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
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP' ]]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB' , '-1']]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M' , '-2']]
        m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P' , '-3']]

angle = math.pi/4
A = [0.5, 0, 0]
A = rotatePointAlongVector(A, somaMTvectorZpoint, somaMTvectorZ, angle)
B = rotatePointAlongVector(A, somaMTvectorZpoint, somaMTvectorZ, angle*2)
C = rotatePointAlongVector(B, somaMTvectorZpoint, somaMTvectorZ, angle*2)
D = rotatePointAlongVector(C, somaMTvectorZpoint, somaMTvectorZ, angle*2)

neuritesLengthX = [neuriteLength, neuriteLength, neuriteLength, neuriteLength]
neuritesOriginX = [A[0], B[0], C[0], D[0]]
neuritesOriginY = [A[1], B[1], C[1], D[1]]
neuritesRotateZ = [-angle, -(angle+angle*2), -(angle+angle*4), -(angle+angle*6)]

MTsOriginX = [0, 0, 0, 0, 0]
MTsOriginY = [0, 0.55, -0.55, 0, 0]
MTsOriginZ = [0, 0, 0, 0.55, -0.55]

nNeurites = 1
nNeuriteMTs = 1

for i in range(nNeurites):
  # Create the neurite:
  sim.createEntity('System', 'System:/:Neurite%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Neurite%d:GEOMETRY' %i).Value = 3
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHX' %i)
  x.Value = neuritesLengthX[i]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHY' %i)
  y.Value = neuriteRadius*2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINX' %i)
  x.Value = neuritesOriginX[i]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINY' %i)
  y.Value = neuritesOriginY[i]
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
  h = sim.createEntity('HistogramLogProcess',
      'Process:/Neurite%d:Histogram' %i)
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
  h.VariableReferenceList = [['_', 'Variable:/Soma:KIF' ]]
  h.Length = neuritesLengthX[i]
  h.Radius = neuriteRadius
  h.Bins = 5
  h.LogInterval = 1
  h.ExposureTime = 60
  h.FileName = filename + ("_n%d.csv" %i)
  h.LogEnd = duration-1
  h.Iterations = 1

  for j in range(nNeuriteMTs):
    m = sim.createEntity('MicrotubuleProcess',
        'Process:/Neurite%d:Microtubule%d' %(i, j))
    m.OriginX = MTsOriginX[j]
    m.OriginY = MTsOriginY[j]
    m.OriginZ = MTsOriginZ[j]
    m.RotateX = 0
    m.RotateY = 0
    m.RotateZ =  0
    m.Radius = MTRadius
    m.SubunitRadius = KinesinRadius
    m.Length = MTLength
    m.Filaments = Filaments
    m.Periodic = 0
    m.Verbose = 1
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_GTP_KIF_ATP' ]]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB', '-1']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_M', '-2']]
    m.VariableReferenceList = [['_', 'Variable:/Soma:TUB_P', '-3']]

run(duration)

