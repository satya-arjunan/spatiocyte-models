try:
  T
except NameError:
  T = 800
  Iterations = 100

import math 
sim = theSimulator
dt = 0.1
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 0.05
s.SearchVacant = 0
#s.DebugLevel = 0
nVoxels = 2352

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
sim.createEntity('Variable', 'Variable:/:C').Value = nVoxels-1
sim.createEntity('Variable', 'Variable:/:B').Value = 1

#l = sim.createEntity('VisualizationLogProcess', 'Process:/:logger')
#l.VariableReferenceList = [['_', 'Variable:/:A']]
#l.VariableReferenceList = [['_', 'Variable:/:B']]
#l.LogInterval = dt

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:p1')
p.VariableReferenceList = [['_', 'Variable:/:A']]

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:p2')
p.VariableReferenceList = [['_', 'Variable:/:B']]
p.UniformLengthX = 0.1
p.UniformLengthY = 0.1
p.UniformLengthZ = 0.1
p.Priority = 100

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:p3')
p.VariableReferenceList = [['_', 'Variable:/:C']]

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseA')
d.VariableReferenceList = [['_', 'Variable:/:A']]
d.WalkReact = 1
d.D = 0.1

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
b.VariableReferenceList = [['_', 'Variable:/:A','-1']]
b.VariableReferenceList = [['_', 'Variable:/:C','-1']]
b.VariableReferenceList = [['_', 'Variable:/:C','1']]
b.VariableReferenceList = [['_', 'Variable:/:A','1']]
b.ForcedSequence = 1
b.p = 1

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
b.VariableReferenceList = [['_', 'Variable:/:A','-1']]
b.VariableReferenceList = [['_', 'Variable:/:B','-1']]
b.VariableReferenceList = [['_', 'Variable:/:C','1']]
b.VariableReferenceList = [['_', 'Variable:/:B','1']]
b.ForcedSequence = 1
b.k = 0.023785

b = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3')
b.VariableReferenceList = [['_', 'Variable:/:C','-1']]
b.VariableReferenceList = [['_', 'Variable:/:A','1']]
b.k = 0.1/nVoxels


l = sim.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:A']]
l.LogInterval = dt
l.LogEnd = T
l.Iterations = Iterations
l.Verbose = 0

run(T+0.01)
