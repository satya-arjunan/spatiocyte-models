sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 4.4e-9 
s = sim.createStepper('ODEStepper', 'DE')
s.MaxStepInterval = 1e-3
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 5e-7
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 5e-7
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 5e-7
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:A').Value = 1500
sim.createEntity('Variable', 'Variable:/:B').Value = 0
sim.createEntity('Variable', 'Variable:/:C').Value = 0

v = sim.createEntity('Variable', 'Variable:/:E')
v.Value = 100
v.Name = 'HD'
v = sim.createEntity('Variable', 'Variable:/:S')
v.Value = 1000
v.Name = 'HD'
v = sim.createEntity('Variable', 'Variable:/:ES')
v.Value = 0
v.Name = 'HD'
v = sim.createEntity('Variable', 'Variable:/:P')
v.Value = 0
v.Name = 'HD'

# E + S -> ES
r = sim.createEntity('MassActionProcess', 'Process:/:r1')
r.StepperID = 'DE'
r.VariableReferenceList = [['_', 'Variable:.:E','-1']]
r.VariableReferenceList = [['_', 'Variable:.:S','-1']]
r.VariableReferenceList = [['_', 'Variable:.:ES','1']]
r.k = 1e-22

# ES -> E + S
r = sim.createEntity('MassActionProcess', 'Process:/:r2')
r.StepperID = 'DE'
r.VariableReferenceList = [['_', 'Variable:.:ES', '-1']]
r.VariableReferenceList = [['_', 'Variable:.:E', '1']]
r.VariableReferenceList = [['_', 'Variable:.:S', '1']]
r.k = 1e-1

# ES -> E + P
r = sim.createEntity('MassActionProcess', 'Process:/:r3')
r.StepperID = 'DE'
r.VariableReferenceList = [['_', 'Variable:.:ES', '-1']]
r.VariableReferenceList = [['_', 'Variable:.:E', '1']]
r.VariableReferenceList = [['_', 'Variable:.:P', '1']]
r.k = 1e-1

# P + A -> B
s = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
s.VariableReferenceList = [['_', 'Variable:/:P', '-1']]
s.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
s.VariableReferenceList = [['_', 'Variable:/:B', '1']]
s.k = 5e-24

# A + B -> C
d = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
d.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
d.VariableReferenceList = [['_', 'Variable:/:B', '-1']]
d.VariableReferenceList = [['_', 'Variable:/:C', '1']]
d.k = 5e-24

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pop')
p.VariableReferenceList = [['_', 'Variable:/:A']]

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseA')
d.VariableReferenceList = [['_', 'Variable:/:A']]
d.D = 5e-16

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseB')
d.VariableReferenceList = [['_', 'Variable:/:B']]
d.D = 5e-16

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseC')
d.VariableReferenceList = [['_', 'Variable:/:C']]
d.D = 5e-16

l = sim.createEntity('VisualizationLogProcess', 'Process:/:logger')
l.VariableReferenceList = [['_', 'Variable:/:A']]
l.VariableReferenceList = [['_', 'Variable:/:B']]
l.VariableReferenceList = [['_', 'Variable:/:C']]
l.LogInterval = 1e-1

l = sim.createEntity('IteratingLogProcess', 'Process:/:logiter')
l.VariableReferenceList = [['_', 'Variable:/:A']]
l.VariableReferenceList = [['_', 'Variable:/:B']]
l.VariableReferenceList = [['_', 'Variable:/:C']]
l.VariableReferenceList = [['_', 'Variable:.:E']]
l.VariableReferenceList = [['_', 'Variable:.:S']]
l.VariableReferenceList = [['_', 'Variable:.:ES']]
l.VariableReferenceList = [['_', 'Variable:.:P']]
l.LogInterval = 1e-2
l.LogEnd = 99

run(100)
