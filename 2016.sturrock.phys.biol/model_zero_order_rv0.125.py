try:
  T
except NameError:
  T = 2000
  Iterations = 5000

import math 
sim = theSimulator
dt = 0.1
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 0.125
s.SearchVacant = 1
#s.DebugLevel = 0
nVoxels = 384.0

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 1 #periodic
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 1 #periodic
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 1 #periodic
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:A').Value = 0
sim.createEntity('Variable', 'Variable:/:B').Value = 1

#l = sim.createEntity('VisualizationLogProcess', 'Process:/:logger')
#l.VariableReferenceList = [['_', 'Variable:/:A']]
#l.VariableReferenceList = [['_', 'Variable:/:B']]
#l.LogInterval = dt

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:p1')
p.VariableReferenceList = [['_', 'Variable:/:A']]

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:p2')
p.VariableReferenceList = [['_', 'Variable:/:B']]
p.UniformLengthX = 0.3
p.UniformLengthY = 0.3
p.UniformLengthZ = 0.3
p.Priority = 100

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseA')
d.VariableReferenceList = [['_', 'Variable:/:A']]
d.D = 0.1

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
b.VariableReferenceList = [['_', 'Variable:/:A','-1']]
b.VariableReferenceList = [['_', 'Variable:/:B','-1']]
b.VariableReferenceList = [['_', 'Variable:/:VACANT','1']]
b.VariableReferenceList = [['_', 'Variable:/:B','1']]
b.ForcedSequence = 1
#b.k = 0.02
#b.k = 0.023785
b.k = 0.02/(1-0.02/(4*math.pi*2*s.VoxelRadius*d.D))
#b.p = 0.02/(6*math.sqrt(2.0)*d.D*2*s.VoxelRadius)

b = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3')
b.VariableReferenceList = [['_', 'Variable:/:A','1']]
b.k = 0.1/4.24264


l = sim.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:A']]
l.LogInterval = dt
l.LogEnd = T
l.Iterations = Iterations
l.Verbose = 1

run(T+1.0)
