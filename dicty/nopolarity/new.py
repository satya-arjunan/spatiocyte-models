
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
PTENvol_frac = 0.5
nVacant_total = 17325
nInterface = 21175
nVolumeVacant = 279864-nInterface
nANIO_frac = 0.1 # 10%
nPIP2_frac = 0.03 # 3%
nPTEN_total = 500

#PTEN fractions, PTEN volume state => 4
f4 = PTENvol_frac
f1 = p1*(1-f4)
f2 = p2*(1-f4)
f3 = p3*(1-f4)
kV1 = (f1*l1 + f1*k12 - f2*k21)/(f4)
kV2 = (f2*l2 + f2*k23 + f2*k21 - f1*k12 - f3*k32)/(f4)
kV3 = (f3*l3 + f3*k32 - f2*k23)/(f4)

#ss = steady-state
nPIP2_total = nPIP2_frac*nVacant_total
nANIO_total = nANIO_frac*nVacant_total
nPTENp2_ss = f1*nPTEN_total
nPTENa_ss = f2*nPTEN_total
nPTEN_ss = f3*nPTEN_total
nPIP2_ss = nPIP2_total-nPTENp2_ss
nANIO_ss = nANIO_total-nPTENa_ss
nVacant_ss = nVacant_total-nANIO_total-nPIP2_total

#tot = nPIP2_ss + nANIO_ss + nVacant_ss
#fpip2 = nPIP2_ss/tot
#fanio = nANIO_ss/tot
#fvacant = nVacant_ss/tot
#
#e1 = kV1*f41*fpip2
#e2 = kV2*f42*fanio
#e3 = kV3*f43*fvacant
#
#
#
#c1 = q1/(e1*fpip2)
#c2 = q2/(e2*fanio)
#c3 = q3/(e3*fvacant)
#
#
#tot = c1 + c2 + c3
#c1 = c1/tot*f4
#c2 = c2/tot*f4
#c3 = c3/tot*f4
#
#f41 = PTENvol1_frac
#f42 = PTENvol2_frac
#f43 = PTENvol3_frac


PTENp2_frac = f1
PTENa_frac = f2
PTEN_frac = f3

#ss = steady-state
nPTENa_ss = PTENa_frac*nPTEN_total
nPTENp2_ss = PTENp2_frac*nPTEN_total
nPTEN_ss = PTEN_frac*nPTEN_total
nPIP2_ss = nPIP2_total-nPTENp2_ss
nANIO_ss = nANIO_total-nPTENa_ss
nVacant_ss = nVacant_total-nANIO_total-nPIP2_total
Volume = LengthX*LengthY*LengthZ

print kV1, kV2, kV3


#print nPIP2_ss, nANIO_ss, nVacant_ss, nPTENvol_ss
#print nPIP2_total, nANIO_total, nVacant_total
#print nPTENp2_ss, nPTENa_ss, nPTEN_ss
#print kV1, kV2, kV3
#tot = kV1*nPIP2_ss + kV2*nANIO_ss + kV3*nVacant_ss
#print kV1*nPIP2_ss/tot, kV2*nANIO_ss/tot, kV3*nVacant_ss/tot


#tot = kV1*nPIP2_ss*c1 + kV2*nANIO_ss*c2 + kV3*nVacant_ss*c3
#kV1*c1/tot = 0.24
#kV2*c2/tot = 0.60
#kV3*c3/tot = 0.16

#kV1*c1 = f1*l1 + f1*k12 - f2*k21
#kV2*c2 = f2*l2 + f2*k23 + f2*k21 - f1*k12 - f3*k32
#kV3*c3 = f3*l3 + f3*k32 - f2*k23
#
#
#c1 = PTENvol_frac*

#PTENvol_frac = 0.50
#400.0 1612.5 15072.75 250.0
#519.75 1732.5 17325
#119.75 120.0 10.25
#0.104709692115 0.125840008501 0.769450299384
#
#PTENvol_frac = 0.25
#340.125 1552.5 15072.75 125.0
#519.75 1732.5 17325
#179.625 180.0 15.375
#0.0908860502352 0.123675139388 0.785438810377

#PTENvol_frac = 0.9
#495.8 1708.5 15072.75 450.0
#519.75 1732.5 17325
#23.95 24.0 2.05
#0.125693835086 0.129126257045 0.745179907869

#PTENvol_frac = 0.05
#292.225 1504.5 15072.75 25.0
#519.75 1732.5 17325
#227.525 228.0 19.475
#0.0794065142292 0.121877371972 0.798716113799

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

#s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol')
#s.Value = nPTEN_total
#s.Name = "HD"

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

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol1')
s.Value = nPTEN_total
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol2')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol3')
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
r.k = l1
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
r.k = l2
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
r.k = l3
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
r.VariableReferenceList = [['_', 'Variable:/:PTENvol2', '-1']]
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
