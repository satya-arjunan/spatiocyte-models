import numpy as np
import math


volumes = [5.8822e-18]

T = 540000
#nKinesin = 35*2.258e-17/volumes[0]
nKinesin = 100
pPlusEnd_Detach = 1
VoxelRadius = 0.8e-8
nNeurite = 5
nNeuriteMT = 5
EdgeSpace = VoxelRadius*5
neuriteRadius = 0.2e-6
MTRadius = 12.5e-9
KinesinRadius = 0.4e-8
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
  MTLengths[i] = neuriteLengths[i]-2*EdgeSpace
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


  for j in range(nNeuriteMT):
    m = sim.createEntity('MicrotubuleProcess',
        'Process:/Neurite%d:Microtubule%d' %(i, j))
    m.OriginX = MTsOriginX[i][j]-VoxelRadius*30/(MTLengths[i]/2)
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


nSomaMT = 16
somaMTrotateAngle = math.pi*2/max(1.0, nSomaMT)
somaMTorigin = [0.5, 0.0, 0.0]
somaMTvectorZ = [0.0, 0.0, 1.0]
somaMTvectorZpoint = [0.0, 0.0, 0.0]
mtSpaceY = somaLength/(nSomaMT+1)

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
    m = theSimulator.createEntity('MicrotubuleProcess',
        'Process:/Soma:Microtubule%d%d' %(i,j))
    m.OriginX = somaOrigin[0]
    m.OriginY = (rootSpace+mtSpaceY+i*mtSpaceY)/halfRootLengths[1]
    m.OriginZ = OriginZ
    m.RotateX = 0
    m.RotateY = 0
    m.RotateZ = 0
    m.Radius = MTRadius
    m.SubunitRadius = KinesinRadius
    m.Length = somaWidth*0.8
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
r.p = 0.0001

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

run(T)
