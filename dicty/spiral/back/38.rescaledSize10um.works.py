import math

T = 1000
interval = 0.1

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 3e-8
s.SearchVacant = 0
s.RemoveSurfaceBias = 1

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 12e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 12e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 7e-6
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
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 10e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 10e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHZ').Value = 5.5e-6
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
PI3K.Value = 5000
PI3K.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
PTEN.Value = 5000 #increase this to change from lateral wave to spiral
PTEN.Name = "HD"

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
h.InnerRadius = 4.5e-6
h.OuterRadius = 5.5e-6
h.FileName = "original.csv"

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Surface:pop')
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP2')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePI3K')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
d.D = 3e-13/4 #[m2/s] change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3.6e-5 (for DIRP A_vol + mem.VACANT -> A_mem, unit k is m/s)
#so max k_snrp = k_dirp*A/V = 3.6e-5*8.9e-10/1.17e-15 (unit is 1/s)
#max k_snrp = 27 (for SNRP first order, unit of k is 1/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPIP2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 3e-1 #[1/s] change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3K')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
r.k = 5e-1 #[1/s] change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3e-21 (for DIRP A_vol+B_mem -> A_mem+B_mem, unit is m3/s)
#so max k_snrp = 3e-21*A/V = 3e-21*8.9e-10/1.17e-15 (unit of k is m2/s)
#max k_snrp = 2.28e-15 (for SNRP 2nd order A(HD)_mem+B_mem -> A_mem+B_mem, m2/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
r.k = 6e-13/4 #[m2/s] change this to change period

#k in 1/s = k*nPIP3steadystate/A 
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3Km')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
r.k = 6e-13/4 #[m2/s] change this to change period

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP2toPIP3')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','1']]
b.p = 0.1 #[unitless]

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3toPIP2')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN','1']]
b.p = 0.8 #[unitless]

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '1']]
r.k = 2.7 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePI3K')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '1']]
r.k = 2.0 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
r.k = 0.06 #change this to change period #reduce this to increase period and duration of PIP3/PIP2

while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PIP2:",PIP2.Value,"PIP2m:",PIP2m.Value,"PIP3m:",PIP3m.Value,"PI3K:",PI3K.Value,"PTEN:",PTEN.Value,"PI3Km:",PI3Km.Value,"PTENm:",PTENm.Value
