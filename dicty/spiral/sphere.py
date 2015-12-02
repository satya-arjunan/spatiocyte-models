T = 1000
sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 6e-8 
s.SearchVacant = 0
s.RemoveSurfaceBias = 1

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 0

sim.createEntity('System', 'System:/:Cell').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHZ').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:VACANT')

sim.createEntity('System', 'System:/Cell:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Cell/Surface:VACANT')
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2m').Value = 1872
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3m').Value = 0
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3a').Value = 0
sim.createEntity('Variable', 'Variable:/Cell/Surface:PTENm').Value = 469
sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3Km').Value = 4701

h = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2')
h.Value = 12229
h.Name = "HD"

h = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3K')
h.Value = 14066
h.Name = "HD"

h = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
h.Value = 9404
h.Name = "HD"

l = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Surface:logger')
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
l.LogInterval = 20

h = sim.createEntity('HistogramLogProcess', 'Process:/Cell/Surface:his')
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
h.Density = 0
h.Bins = 50
h.LogInterval = 20
h.ExposureTime = 20
h.RadialHeight = 20*s.VoxelRadius
h.LogEnd = T-1
h.Iterations = 1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Surface:pop')
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP2')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
d.D = 1e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
d.D = 1e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3a')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
d.D = 1e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
d.D = 1e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePI3K')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
d.D = 1e-14

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPIP2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 4e-2

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 2e-14

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3Ka')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
r.k = 1e-13

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:dimerPIP3')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
b.p = 0.8

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP2toPIP3')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','1']]
b.p = 0.15

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3toPIP2')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','1']]
b.p = 1

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3atoPIP2')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','1']]
b.p = 1

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '1']]
r.k = 0.09

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePI3K')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '1']]
r.k = 0.02

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
r.k = 0.02

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3a')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
r.k = 0.02

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
r.k = 0.0001

run(T)
