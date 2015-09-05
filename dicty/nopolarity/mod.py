
duration = 10
Iterations = 100
VoxelRadius = 10e-9
LogEvent = 0
LengthX = 4.5e-6
LengthY = 1.35e-6
LengthZ = 0.26e-6

#parameters from 2013.matsuoka.pcb
D1 = 0.035e-12
D2 = 0.133e-12
D3 = 0.693e-12
p1 = 0.479
p2 = 0.480
p3 = 1-p1-p2
q1 = 0.238
q2 = 0.606
q3 = 0.157
l1 = 0.037
l2 = 3.995
l3 = 12.525
k12 = 6.289
k21 = 2.896
k23 = 0.406
k32 = 0.029

#your parameters
k14 = l1
k25 = l2
k36 = l3

PTENvol_frac = 0.5
nVacant_total = 17325
nInterface = 21175
nVolumeVacant = 279864-nInterface
nANIO_frac = 0.1 # 10%
nPIP2_frac = 0.03 # 3%
nPTEN_total = 500

#PTEN fractions, PTEN volume state => 4
f7 = PTENvol_frac
f1 = p1*(1-f7)
f2 = p2*(1-f7)
f3 = p3*(1-f7)

nPIP2_total = nPIP2_frac*nVacant_total
nANIO_total = nANIO_frac*nVacant_total

#ss = steady-state
nPTENp2_ss = f1*nPTEN_total
nPTENa_ss = f2*nPTEN_total
nPTEN_ss = f3*nPTEN_total
nPIP2_ss = nPIP2_total-nPTENp2_ss
nANIO_ss = nANIO_total-nPTENa_ss
nVacant_ss = nVacant_total-nANIO_total-nPIP2_total
Volume = LengthX*LengthY*LengthZ

k41*f4 = f1*k14 + f1*k12 - f2*k21
k52*f5 = f2*k25 + f2*k21 + f2*k23 - f1*k12 - f3*k32
k63*f6 = f3*k36 + f3*k32 - f2*k23
f4+f5+f6 = f7
q1 = k41*f4*nPTEN_total*nPIP2_ss
q2 = k52*f5*nPTEN_total*nANIO_ss
q3 = k63*f6*nPTEN_total*nVacant_ss
q1+q2+q3 = 1


#S1
#f1*k14 + f1*k12          = f4*k41 + f2*k21
#x = f1*k14 + f1*k12 - f2*k21
#S2
#f2*k25 + f2*k21 + f2*k23 = f5*k52 + f1*k12 + f3*k32
#y = f2*k25 + f2*k21 + f2*k23 - f1*k12 - f3*k32
#S3
#f3*k36 + f3*k32          = f6*k63 + f2*k23
#z = f3*k36 + f3*k32 - f2*k23
#S4
f4*k41 + f4*k45 + f4*k46 = f1*k14 + f5*k54 + f6*k64
#S5
f5*k52 + f5*k54 + f5*k56 = f2*k25 + f4*k45 + f6*k65
#S6
f6*k63 + f6*k65 + f6*k64 = f3*k36 + f4*k46 + f5*k56


v1 = nPIP2_ss/(nPIP2_ss + nANIO_ss + nVacant_ss)
v2 = nANIO_ss/(nPIP2_ss + nANIO_ss + nVacant_ss)
v3 = nVacant_ss/(nPIP2_ss + nANIO_ss + nVacant_ss)

uq1 = kk41*f4*nPIP2_ss
uq2 = kk52*f5*nANIO_ss
uq3 = kk63*f6*nVacant_ss

#ax/(ax + by + cz) = q1
#ax - ax(q1) - by(q1) - cz(q1) = 0
#a(x-x(q1)) = by(q1) + cz(q1)
a = (b*y*q1 + c*z*q1)/(x - x*q1)
#by/(ax + by + cz) = q2
#by - ax(q2) - by(q2) - cz(q2) = 0
#b(y-y(q2)) = ax(q2) + cz(q2)
b = (a*x*q2 + c*z*q2)/(y - y*q2)
c = (a*x*q3 + b*y*q3)/(z - z*q3)




#Diffusion coefficients
ProteinDiffusion_a = D2
ProteinDiffusion_p3 = D2
ProteinDiffusion_p2 = D1
ProteinDiffusion_v = D3
LipidDiffusion = 0.5e-12
ProteinDiffusion_vol = 0.9e-12
#ProteinDiffusion_vol = 16e-12

#diffusion step interval
PTENvol_dt = pow(2*VoxelRadius, 2)/(6*ProteinDiffusion_vol)
PTEN_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_v)
PTENa_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_a)
PTENp2_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_p2)
PIP2_dt = pow(2*VoxelRadius, 2)/(4*LipidDiffusion)
ANIO_dt = pow(2*VoxelRadius, 2)/(4*LipidDiffusion)

sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = VoxelRadius
sim.SearchVacant = 1

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = LengthX
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = LengthY
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = LengthZ
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol1')
s.Value = nPTEN_total
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol2')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol3')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PIP2')
s.Value = nPIP2_total
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:ANIO')
s.Value = nANIO_total
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTEN')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENp2')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENa')
s.Value = 0
s.Name = "HD"

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = k12/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '1']]
r.k = k14
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = k21/nPIP2_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '1']]
r.k = k25 
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = k23
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = k32/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '1']]
r.k = k36 
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = kV1/nPIP2_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = kV2/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = kV3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV12')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '1']]
r.k = kV12
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV21')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '1']]
r.k = kV21
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV23')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '1']]
r.k = kV23
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV32')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '1']]
r.k = kV32
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV13')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '1']]
r.k = kV13
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV31')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol1', '1']]
r.k = kV31
r.LogEvent = LogEvent
r.LogStart = 5

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol1']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol3']]
l.LogInterval = 5e-1
l.LogEnd = duration
l.Iterations = Iterations

run(duration+0.1)
