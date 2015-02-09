import math

Filaments = 13
RotateAngle = math.pi
MTRadius = 12.5e-9
KinesinRadius = 0.4e-8
neuriteRadius = 0.2e-6
neuriteLength = 5e-6
Radius = 1.3e-6
MTLength = neuriteLength*0.95

comp_length = 30e-6
comp_width = 10e-6
comp_depth = 500e-9
VoxelRadius = 0.8e-8

singleMTVolumeVoxels = 717256.0
singleNeuriteVolumeVoxels = 48325789.0
totalKinesins = 1000*singleMTVolumeVoxels/singleNeuriteVolumeVoxels
print "totalKinesins:", totalKinesins

theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius

# Create the root container compartment using the default Cuboid geometry:
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = comp_length
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = comp_width
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = comp_depth
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

theSimulator.createEntity('Variable', 'Variable:/:Kinesin').Value = 25
theSimulator.createEntity('Variable', 'Variable:/:MTKinesin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MTKinesinATP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:Tubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:actTubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:TubulinM' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:TubulinP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:GFP' ).Value = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populate')
populator.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
populator.VariableReferenceList = [['_', 'Variable:/:actTubulin']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populateK')
populator.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
#populator.OriginX = -1.0
#populator.UniformRadiusX = 0.1

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:detachPlus')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:TubulinP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.VariableReferenceList = [['_', 'Variable:/:TubulinP','1']]
react.p = 1

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseKinesin')
diffuse.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
diffuse.D = 0.5e-12

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:explicitAttachAct_k6')
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
#react.k = 2.5863133e-22
react.p = 1
#react.k = 1.69706e-20

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:explicitAttach_k1')
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
#react.k = 2.5863133e-24
react.p = 0.00005
#react.k = 6.78823e-24

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:detach_k4')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.SearchVacant = 1
react.k = 15

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:inactive_k7')
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','1']]
react.k = 0.055

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:hydrolysis_k3')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
react.SearchVacant = 1
react.k = 100

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:phosphorylate_k2')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','1']]
react.SearchVacant = 1
react.k = 145

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:ratchet_k5')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.BindingSite = 1
react.k = 55

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePlus')
diffuse.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
diffuse.VariableReferenceList = [['_', 'Variable:/:actTubulin', '1']]
diffuse.D = 0.04e-12

#tagger = theSimulator.createEntity('TagProcess', 'Process:/:tagger')
#tagger.VariableReferenceList = [['_', 'Variable:/:GFP', '-1' ]]
#tagger.VariableReferenceList = [['_', 'Variable:/:Kinesin', '5' ]]
#tagger.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
#tagger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP']]

#life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
#life.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '-1']]
#life.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '-1']]
#life.VariableReferenceList = [['_', 'Variable:/:Kinesin', '1']]

visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
visualLogger.VariableReferenceList = [['_', 'Variable:/:Tubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TubulinM']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TubulinP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:Kinesin', '10600']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '10600']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '10600']]
visualLogger.LogInterval = 10

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
  xx = (a*(v2 + w2) - u*(b*v + c*w - u*x - v*y - w*z)) * oneMinusCosT + x*cosT + (-c*v + b*w - w*y + v*z)*sinT
  yy = (b*(u2 + w2) - v*(a*u + c*w - u*x - v*y - w*z)) * oneMinusCosT + y*cosT + (c*u - a*w + w*x - u*z)*sinT
  zz = (c*(u2 + v2) - w*(a*u + b*v - u*x - v*y - w*z)) * oneMinusCosT + z*cosT + (-b*u + a*v - v*x + u*y)*sinT
  return [xx, yy, zz]

MTs = 16
MTrotateAngle = math.pi*2/max(1.0,MTs)
MTorigin = [0.5, 0.0, 0.0]
MTvectorZ = [0.0, 0.0, 1.0]
MTvectorZpoint = [0.0, 0.0, 0.0]
for i in range(MTs):
  for j in range(3):
    startAngle = math.pi/3.3
    OriginZ = 0.0
    if(j != 0):
      startAngle = math.pi/2
      if(j == 1):
        OriginZ = 0.5 
      else:
        OriginZ = -0.5 
    Microtubule = theSimulator.createEntity('MicrotubuleProcess', 'Process:/:Microtubule%d%d' %(i,j))
    P = rotatePointAlongVector(MTorigin, MTvectorZpoint, MTvectorZ, MTrotateAngle*i+startAngle)
    Microtubule.OriginX = P[0]
    Microtubule.OriginY = P[1]
    Microtubule.OriginZ = OriginZ
    Microtubule.RotateX = 0
    Microtubule.RotateY = 0
    Microtubule.RotateZ =  MTrotateAngle*i+startAngle
    Microtubule.Radius = MTRadius
    Microtubule.SubunitRadius = KinesinRadius
    Microtubule.Length = Radius*0.7
    Microtubule.Filaments = Filaments
    Microtubule.Periodic = 0
    Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesin' ]]
    Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP' ]]
    Microtubule.VariableReferenceList = [['_', 'Variable:/:actTubulin' ]]
    Microtubule.VariableReferenceList = [['_', 'Variable:/:Tubulin' , '-1']]
    Microtubule.VariableReferenceList = [['_', 'Variable:/:TubulinM' , '-2']]
    Microtubule.VariableReferenceList = [['_', 'Variable:/:TubulinP' , '-3']]

run(180000)


