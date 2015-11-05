sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 4.4e-9 
s.SearchVacant = 0

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 0

sim.createEntity('System', 'System:/:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Surface:VACANT')

sim.createEntity('Variable', 'Variable:/:Ankyrin').Value = 0
sim.createEntity('Variable', 'Variable:/:Gag').Value = 200

sim.createEntity('Variable', 'Variable:/Surface:Ankyrin').Value = 0
sim.createEntity('Variable', 'Variable:/Surface:Gag').Value = 0

l = sim.createEntity('VisualizationLogProcess', 'Process:/:logger')
l.VariableReferenceList = [['_', 'Variable:/:Ankyrin']]
l.VariableReferenceList = [['_', 'Variable:/:Gag']]
l.VariableReferenceList = [['_', 'Variable:/Surface:Ankyrin']]
l.VariableReferenceList = [['_', 'Variable:/Surface:Gag']]
l.LogInterval = 0.1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pop')
p.VariableReferenceList = [['_', 'Variable:/:Ankyrin']]
p.VariableReferenceList = [['_', 'Variable:/:Gag']]

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
b.VariableReferenceList = [['_', 'Variable:/:Ankyrin','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Ankyrin','1']]
b.p = 0

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
b.VariableReferenceList = [['_', 'Variable:/:Ankyrin','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Gag','-1']]
b.VariableReferenceList = [['_', 'Variable:/:Ankyrin','1']]
b.VariableReferenceList = [['_', 'Variable:/:Gag','1']]
b.ForcedSequence = 1
b.p = 1

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
b.VariableReferenceList = [['_', 'Variable:/:Gag','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Gag','1']]
b.p = 0.00001

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
b.VariableReferenceList = [['_', 'Variable:/:Gag','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Gag','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Gag','1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:Gag','1']]
b.p = 1

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseA')
d.VariableReferenceList = [['_', 'Variable:/:Ankyrin']]
d.D = 1e-13

d = sim.createEntity('DiffusionProcess', 'Process:/:diffuseB')
d.VariableReferenceList = [['_', 'Variable:/:Gag']]
d.D = 1e-13

run(1000)
