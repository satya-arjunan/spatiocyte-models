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

PAR2m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PAR2m')
PAR2m.Value = 4600
PAR1m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PAR1m')
PAR1m.Value = 4600
PTENm = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTENm')
PTENm.Value = 309
PKC3m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PKC3m')
PKC3m.Value = 3096

PAR2 = sim.createEntity('Variable', 'Variable:/Cell/Surface:PAR2')
PAR2.Value = 0
PAR2.Name = "HD"

PKC3 = sim.createEntity('Variable', 'Variable:/Cell/Surface:PKC3')
PKC3.Value = 5000
PKC3.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
PTEN.Value = 5000 #increase this to change from lateral wave to spiral
PTEN.Name = "HD"

l = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Surface:logger')
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
#l.VariableReferenceList = [['_', 'Variable:/:A']]
#l.VariableReferenceList = [['_', 'Variable:/:B']]
#l.VariableReferenceList = [['_', 'Variable:/Membrane:VACANT']]
l.LogInterval = 0.5

h = sim.createEntity('HistogramLogProcess', 'Process:/Cell/Surface:his')
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m']]
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
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m']]

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePAR2')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePAR1')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
d.D = 3e-13/4 #[m2/s] change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePKC3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m']]
d.D = 3e-13/4 #[m2/s] change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3.6e-5 (for DIRP A_vol + mem.VACANT -> A_mem, unit k is m/s)
#so max k_snrp = k_dirp*A/V = 3.6e-5*8.9e-10/1.17e-15 (unit is 1/s)
#max k_snrp = 27 (for SNRP first order, unit of k is 1/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPAR2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m', '1']]
r.k = 3e-1 #[1/s] change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPKC3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m', '1']]
r.k = 5e-1 #[1/s] change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3e-21 (for DIRP A_vol+B_mem -> A_mem+B_mem, unit is m3/s)
#so max k_snrp = 3e-21*A/V = 3e-21*8.9e-10/1.17e-15 (unit of k is m2/s)
#max k_snrp = 2.28e-15 (for SNRP 2nd order A(HD)_mem+B_mem -> A_mem+B_mem, m2/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m', '1']]
r.k = 6e-13/4 #[m2/s] change this to change period

#k in 1/s = k*nPAR1steadystate/A 
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPKC3m')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m', '1']]
r.k = 6e-13/4 #[m2/s] change this to change period

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PAR2toPAR1')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m','1']]
b.p = 0.1 #[unitless]

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PAR1toPAR2')
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN','1']]
b.p = 0.8 #[unitless]

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePTEN')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '1']]
r.k = 2.7 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePKC3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PKC3', '1']]
r.k = 2.0 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePAR1')
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR1m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PAR2', '1']]
r.k = 0.06 #change this to change period #reduce this to increase period and duration of PAR1/PAR2

while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PAR2:",PAR2.Value,"PAR2m:",PAR2m.Value,"PAR1m:",PAR1m.Value,"PKC3:",PKC3.Value,"PTEN:",PTEN.Value,"PKC3m:",PKC3m.Value,"PTENm:",PTENm.Value
