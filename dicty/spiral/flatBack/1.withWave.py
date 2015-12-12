
import math

T = 3000
interval = 0.1
latAmoebaDiameter = 8e-6

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 10e-9
s.SearchVacant = 0

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-8
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = latAmoebaDiameter*1
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = latAmoebaDiameter*1
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
sim.createEntity('Variable', 'Variable:/:A').Value = 0
sim.createEntity('Variable', 'Variable:/:B').Value = 0

# Create the surface compartment:
sim.createEntity('System', 'System:/:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Surface:VACANT')

PIP2m = sim.createEntity('Variable', 'Variable:/Surface:PIP2m')
PIP2m.Value = 10000
PIP3m = sim.createEntity('Variable', 'Variable:/Surface:PIP3m')
PIP3m.Value = 0
PTENm = sim.createEntity('Variable', 'Variable:/Surface:PTENm')
PTENm.Value = 0
PI3Km = sim.createEntity('Variable', 'Variable:/Surface:PI3Km')
PI3Km.Value = 100

PIP2 = sim.createEntity('Variable', 'Variable:/Surface:PIP2')
PIP2.Value = 0
PIP2.Name = "HD"

PI3K = sim.createEntity('Variable', 'Variable:/Surface:PI3K')
PI3K.Value = 5000
PI3K.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Surface:PTEN')
PTEN.Value = 5000
PTEN.Name = "HD"

l = sim.createEntity('VisualizationLogProcess', 'Process:/Surface:logger')
l.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m']]
l.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m']]
l.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km']]
l.VariableReferenceList = [['_', 'Variable:/Surface:PTENm']]
#l.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
#l.VariableReferenceList = [['_', 'Variable:/:B', '-2']]
l.LogInterval = 0.5

#h = sim.createEntity('HistogramLogProcess', 'Process:/Surface:his')
#h.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m']]
#h.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km']]
#h.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m']]
#h.VariableReferenceList = [['_', 'Variable:/Surface:PTENm']]
#h.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
#h.VariableReferenceList = [['_', 'Variable:/:B', '-2']]
#h.Density = 0
#h.Bins = 50
#h.LogInterval = interval/10.0
#h.ExposureTime = interval
#h.RadialHeight = 20*s.VoxelRadius
#h.LogEnd = T-1
#h.Iterations = 1
##h.RotateY = math.pi/2
##h.InnerRadius = 9e-6
##h.OuterRadius = 11e-6
#h.FileName = "original.csv"

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Surface:pop')
p.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m']]
p.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m']]
p.VariableReferenceList = [['_', 'Variable:/Surface:PTENm']]
p.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km']]

d = sim.createEntity('DiffusionProcess', 'Process:/Surface:diffusePIP2')
d.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m']]
d.D = 1e-14 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Surface:diffusePIP3')
d.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m']]
d.D = 1e-14 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Surface:diffusePTEN')
d.VariableReferenceList = [['_', 'Variable:/Surface:PTENm']]
d.D = 1e-14 #change this to change period

d = sim.createEntity('DiffusionProcess', 'Process:/Surface:diffusePI3K')
d.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km']]
d.D = 1e-14 #change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3.6e-5 (for DIRP A_vol + mem.VACANT -> A_mem, unit k is m/s)
#so max k_snrp = k_dirp*A/V = 3.6e-5*8.9e-10/1.17e-15 (unit is 1/s)
#max k_snrp = 27 (for SNRP first order, unit of k is 1/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:recruitPIP2')
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m', '1']]
r.k = 1e-1 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:recruitPI3K')
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km', '1']]
r.k = 1e-4#change this to change period

#at 5e-9 voxel radius
#when p=1, k_dirp = 3e-21 (for DIRP A_vol+B_mem -> A_mem+B_mem, unit is m3/s)
#so max k_snrp = 3e-21*A/V = 3e-21*8.9e-10/1.17e-15 (unit of k is m2/s)
#max k_snrp = 2.28e-15 (for SNRP 2nd order A(HD)_mem+B_mem -> A_mem+B_mem, m2/s)
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:recruitPTEN')
r.VariableReferenceList = [['_', 'Variable:/Surface:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PTENm', '1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m', '1']]
r.k = 1e-15 #change this to change period

#k*PI3K*3000/A 
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:recruitPI3Ka')
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km', '1']]
r.k = 1e-15 #change this to change period

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:PIP2toPIP3')
b.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m','1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km','1']]
b.p = 0.4

b = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:PIP3toPIP2')
b.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PTENm','-1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PIP2m','1']]
b.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
b.p = 0.8

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dissociatePTEN')
r.VariableReferenceList = [['_', 'Variable:/Surface:PTENm', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PTEN', '1']]
r.k = 1.5 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dissociatePI3K')
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3Km', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PI3K', '1']]
r.k = 1.0 #change this to change period

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dissociatePIP3')
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '1']]
r.k = 0.05 #change this to change period #reduce this to increase period and duration of PIP3/PIP2

while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PIP2:",PIP2.Value,"PIP2m:",PIP2m.Value,"PIP3m:",PIP3m.Value,"PI3K:",PI3K.Value,"PTEN:",PTEN.Value,"PI3Km:",PI3Km.Value,"PTENm:",PTENm.Value


