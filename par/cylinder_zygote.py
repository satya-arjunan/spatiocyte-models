import math

PAR1_kinase_dead = 0
MT_nucleation = 0
MT_PAR2m_rate = 8e-3
MT_number = 300

T = 3000
interval = 0.1

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 3e-8
s.SearchVacant = 0
s.RemoveSurfaceBias = 1

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 14.5e-6
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
sim.createEntity('Variable', 'Variable:/Cell:GEOMETRY').Value = 3
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 14e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 10e-6
sim.createEntity('Variable', 'Variable:/Cell:ORIGINZ').Value = -1.6
sim.createEntity('Variable', 'Variable:/Cell:VACANT')

sim.createEntity('System', 'System:/Cell:Cortex').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell/Cortex:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Cell/Cortex:VACANT').Value = 1

MT_PAR2m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:MT_PAR2m')
if(MT_nucleation):
  MT_PAR2m.Value = MT_number
else:
  MT_PAR2m.Value = 0 
PAR1m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR1m')
PAR1m.Value = 0
PAR2m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR2m')
PAR2m.Value = 0
PAR3m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR3m')
PAR3m.Value = 0
PKC3_PAR3m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PKC3_PAR3m')
PKC3_PAR3m.Value = 4404
PKC3_PAR3m_PAR1m = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m')
PKC3_PAR3m_PAR1m.Value = 0

PAR1 = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR1')
PAR1.Value = 2500
PAR1.Name = "HD"

PAR2 = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR2')
if(MT_nucleation):
  PAR2.Value = 8700
else:
  PAR2.Value = 3700 + MT_number
PAR2.Name = "HD"

PAR3 = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PAR3')
PAR3.Value = 630
PAR3.Name = "HD"

PKC3 = sim.createEntity('Variable', 'Variable:/Cell/Cortex:PKC3')
PKC3.Value = 0
PKC3.Name = "HD"

l = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Cortex:logger')
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m']]
l.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m']]
#l.VariableReferenceList = [['_', 'Variable:/:A']]
#l.VariableReferenceList = [['_', 'Variable:/:B']]
l.LogInterval = 0.5

h = sim.createEntity('HistogramLogProcess', 'Process:/Cell/Cortex:his')
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m']]
#h.VariableReferenceList = [['_', 'Variable:/:A', '-1']]
#h.VariableReferenceList = [['_', 'Variable:/:B', '-2']]
h.Density = 0
h.Bins = 50
h.LogInterval = interval/10.0
h.ExposureTime = interval
h.RadialHeight = 100*s.VoxelRadius
h.LogEnd = T-1
h.Iterations = 1
h.RotateX = math.pi/2
h.InnerRadius = 4.5e-6
h.OuterRadius = 5.5e-6
h.FileName = "original.csv"

h = sim.createEntity('IteratingLogProcess', 'Process:/Cell/Cortex:')
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m']]
#h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m']]
h.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m']]
h.LogInterval = 5
h.LogEnd = T-1
h.Iterations = 1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Cortex:popMT')
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m']]
#p.EdgeX = 1
p.OriginX = 1
p.UniformLengthX = 0.1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Cortex:pop')
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m']]
p.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m']]

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Cortex:diffusePAR1')
d.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m']]
d.D = 4e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Cortex:diffusePAR2')
d.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m']]
d.D = 4e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Cortex:diffusePAR3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m']]
d.D = 4e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Cortex:diffusePKC3_PAR3')
d.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m']]
d.D = 4e-14

d = sim.createEntity('DiffusionProcess', 'Process:/Cell/Cortex:diffusePKC3_PAR3_PAR1')
d.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m']]
d.D = 4e-14


r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r1')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '1']]
r.k = 1e-2

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r2')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '1']]
r.k = 1e-15

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r4')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '1']]
r.k = 1e-15

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r3')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m', '1']]
r.k = 1e-15

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r5')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '1']]
r.k = 1e-5

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r6')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '1']]
r.k = 2e-14

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r7')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '1']]
r.k = 2e-14

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r8')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m', '1']]
r.k = 1e-5

r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r9')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m', '1']]
r.k = 2e-14


#phosphorylate PAR2
r = sim.createEntity('DiffusionInfluencedReactionProcess','Process:/Cell/Cortex:r10')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m','1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2','1']]
r.p = 0.07 #[unitless]

#complex PKC3_PAR3m_PAR1m
r = sim.createEntity('DiffusionInfluencedReactionProcess','Process:/Cell/Cortex:r11')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m','1']]
r.p = 0.5 #[unitless]

#phosphorylate PAR1
r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r12')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m', '1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1', '1']]
r.k = 10 #change this to change period

#phosphorylate PAR3
r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r13')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m_PAR1m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m', '1']]
if(PAR1_kinase_dead):
  r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3_PAR3m', '1']]
else:
  r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PKC3', '1']]
  r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3', '1']]
r.k = 10 #change this to change period

#phosphorylate PAR3
r = sim.createEntity('DiffusionInfluencedReactionProcess','Process:/Cell/Cortex:r14')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR1m','1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR3','1']]
if(PAR1_kinase_dead):
  r.p = 0 #[unitless]
else:
  r.p = 0.1 #[unitless]

#dissociate MT_PAR2m
r = sim.createEntity('SpatiocyteNextReactionProcess','Process:/Cell/Cortex:r15')
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:MT_PAR2m','-1']]
r.VariableReferenceList = [['_', 'Variable:/Cell/Cortex:PAR2', '1']]
r.k = MT_PAR2m_rate #change this to change period


while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PAR1m:",PAR1m.Value,"PAR2m:",PAR2m.Value,"PAR3m:",PAR3m.Value,"PKC3_PAR3m:",PKC3_PAR3m.Value,"PKC3_PAR3m_PAR1m:",PKC3_PAR3m_PAR1m.Value,"MT_PAR2m:",MT_PAR2m.Value,"PAR1:",PAR1.Value,"PAR2:",PAR2.Value,"PAR3:",PAR3.Value,"PKC3:",PKC3.Value
