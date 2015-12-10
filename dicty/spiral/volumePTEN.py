import math

T = 1000
interval = 0.1

volume = 1.17332e-15
area = 8.9156e-10
ratio = area/volume

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 5e-9 
s.SearchVacant = 0
s.RemoveSurfaceBias = 1

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 13e-6
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 3
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 5
sim.createEntity('Variable', 'Variable:/:A').Value = 0
sim.createEntity('Variable', 'Variable:/:B').Value = 0

sim.createEntity('System', 'System:/:Membrane').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Membrane:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Membrane:VACANT')

sim.createEntity('System', 'System:/:Cell').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHZ').Value = 11e-6
sim.createEntity('Variable', 'Variable:/Cell:ORIGINZ').Value = -1.0
sim.createEntity('Variable', 'Variable:/Cell:VACANT')

sim.createEntity('System', 'System:/Cell:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Cell/Surface:VACANT').Value = 1

PIP2m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2m')
PIP2m.Value = 4600
PIP3m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3m')
PIP3m.Value = 4600
PTENm = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTENm')
PTENm.Value = 309
PI3Km = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3Km')
PI3Km.Value = 3096

PIP2 = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2')
PIP2.Value = 0
PIP2.Name = "HD"

PI3K = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3K')
PI3K.Value = 4000
PI3K.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
PTEN.Value = 5000 #increase this to change from lateral wave to spiral
PTEN.Name = "HD"

PTENv = sim.createEntity('Variable', 'Variable:/Cell:PTENv')
PTENv.Value = 0 #increase this to change from lateral wave to spiral
#PTENv.Name = "HD"

l = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Surface:logger')
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
#l.VariableReferenceList = [['_', 'Variable:/:A']]
#l.VariableReferenceList = [['_', 'Variable:/:B']]
#l.VariableReferenceList = [['_', 'Variable:/Membrane:VACANT']]
l.LogInterval = 0.5

h = sim.createEntity('HistogramLogProcess', 'Process:/Cell/Surface:his')
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
#h.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
#h.VariableReferenceList = [['_', 'Variable:/:B', '-2']]
h.Density = 0
h.Bins = 50
h.LogInterval = interval/10.0
h.ExposureTime = interval
h.RadialHeight = 20*s.VoxelRadius
h.LogEnd = T-1
h.Iterations = 1
h.RotateX = math.pi/2
h.InnerRadius = 9e-6
h.OuterRadius = 11e-6
h.FileName = "original.csv"

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Surface:pop')
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP2')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
d.D = 3e-13 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
d.D = 3e-13 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
d.D = 3e-13 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePI3K')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
d.D = 3e-13 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTENv')
d.VariableReferenceList = [['_', 'Variable:/Cell:PTENv']]
d.D = 3e-13 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPIP2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 3e-1 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3K')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
r.k = 1e-1 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 6e-13 #change this to change period

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:recruitPTENv')
r.VariableReferenceList = [['_', 'Variable:/Cell:PTENv', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
#r.k = 1e-14/ratio #change this to change period
#r.k = 3e-14/ratio #max k for p=1 at D=1e-13
r.p = 1
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3Km')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
r.k = 2e-13 #change this to change period

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP2toPIP3')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','1']]
b.p = 0.25

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3toPIP2')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN','1']]
b.p = 0.5

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '1']]
r.k = 2.7 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePI3K')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '1']]
r.k = 2 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
r.k = 0.05 #change this to change period #reduce this to increase period and duration of PIP3/PIP2

while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PIP2:",PIP2.Value,"PIP2m:",PIP2m.Value,"PIP3m:",PIP3m.Value,"PI3K:",PI3K.Value,"PTEN:",PTEN.Value,"PI3Km:",PI3Km.Value,"PTENm:",PTENm.Value
