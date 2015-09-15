import math

Filaments = 13
RotateAngle = 0 #math.pi/4
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
dendriteRadius = 0.15e-6
dendriteLength = 0.7e-6
totalMTLength = 0.6e-6

theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

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

somaMTvectorZ = [0.0, 0.0, 1.0]
somaMTvectorZpoint = [0.0, 0.0, 0.0]
angle = math.pi/4
A = [0.5, 0, 0]
A = rotatePointAlongVector(A, somaMTvectorZpoint, somaMTvectorZ, angle)
B = rotatePointAlongVector(A, somaMTvectorZpoint, somaMTvectorZ, angle*2)
C = rotatePointAlongVector(B, somaMTvectorZpoint, somaMTvectorZ, angle*2)
D = rotatePointAlongVector(C, somaMTvectorZpoint, somaMTvectorZ, angle*2)

neuritesLengthX = [dendriteLength, dendriteLength, dendriteLength, dendriteLength]
neuritesOriginX = [A[0], B[0], C[0], D[0]]
neuritesOriginY = [A[1], B[1], C[1], D[1]]
neuritesRotateZ = [-angle, -(angle+angle*2), -(angle+angle*4), -(angle+angle*6)]

MTsOriginX = [0,    0.2,     0,    0,     0]
MTsOriginY = [0,     0,    0,    0,     0]
#MTsOriginY = [0,    0,     0,    0,     0]
MTsOriginZ = [0,    0,     0, 0.55, -0.55]


theSimulator.createEntity('System', 'System:/:neurite').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/neurite:GEOMETRY').Value = 3
theSimulator.createEntity('Variable', 'Variable:/neurite:LENGTHX').Value = dendriteLength
theSimulator.createEntity('Variable', 'Variable:/neurite:LENGTHY').Value = dendriteRadius*2

#theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINX').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINY').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINZ').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/neurite:ROTATEZ').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINX').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINZ').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ROTATEZ').Value = neuritesRotateZ[0]

theSimulator.createEntity('Variable', 'Variable:/neurite:VACANT')
theSimulator.createEntity('System', 'System:/neurite:Membrane').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/neurite/Membrane:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/neurite/Membrane:VACANT')

theSimulator.createEntity('Variable', 'Variable:/neurite:Kinesin').Value = 80
theSimulator.createEntity('Variable', 'Variable:/neurite:MTKinesin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:MTKinesinATP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:Tubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:actTubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:TubulinM' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:TubulinP' ).Value = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populate')
populator.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseKinesin')
diffuse.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]
diffuse.D = 4e-12

visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Tubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:TubulinM']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:TubulinP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesinATP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Interface']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite/Membrane:VACANT']]
visualLogger.LogInterval = 0.0001

for j in range(3):
  Microtubule = theSimulator.createEntity('FilamentProcess', 'Process:/neurite:Microtubule%d' %j)
  Microtubule.OriginX = MTsOriginX[j]
  Microtubule.OriginY = MTsOriginY[j]
  Microtubule.OriginZ = MTsOriginZ[j]
  Microtubule.RotateX = 0
  Microtubule.RotateY = 0
  Microtubule.RotateZ = 0
  Microtubule.SubunitRadius = KinesinRadius
  Microtubule.Length = totalMTLength
  Microtubule.Filaments = 1
  Microtubule.Periodic = 0
  Microtubule.BindingDirection = 0
  Microtubule.DissociationDirection = 0
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesin' ]]
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesinATP' ]]
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:actTubulin' ]]
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:Tubulin' , '-1']]
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:TubulinM' , '-2']]
  Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:TubulinP' , '-3']]

run(0.01)

