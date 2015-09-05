
duration = 1
Iterations = 1
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

#q1 = 0.237524284976795
#q2 = 0.605689082115426
#q3 = 0.156786632907779
#l1 = 0.0371083460085474
#l2 = 3.99533611676107
#l3 = 12.5246469927403
#k12 = 6.28908951033160
#k21 = 2.89587518051729
#k23 = 0.405469954974635
#k32 = 0.0288340937175279
R = 0.762 # PTEN_membrane_ss/PTEN_cytosol_ss
#R = 1 # PTEN_membrane_ss/PTEN_cytosol_ss
p0 = 1

m4=(k12+l1)*(k21+k23+l2)*(k32+l3)-k12*k21*(k32+l3)-k23*k32*(k12+l1)
m1=((k21+k23+l2)*(k32+l3)-k23*k32+k12*(k32+l3)+k12*k23)/m4
m2=(k21*(k32+l3)+(k32+l3)*(k12+l1)+k23*(k12+l1))/m4
m3=(k21*k32+k32*(k12+l1)+(k21+k23+l2)*(k12+l1)-k12*k21)/m4

print m1, m2, m3, m4

m4=(k21*l1*(k32+l3)+(k12+l1)*(k32*l2+(k23+l2)*l3))
m1=(k32*l2+k23*l3+l2*l3+k21*(k32+l3)+k12*(k23+k32+l3))/m4
m2=(k21*(k32+l3)+k12*(k23+k32+l3)+l1*(k23+k32+l3))/m4
m3=(k21*(k32+l1)+k12*(k23+k32+l2)+l1*(k23+k32+l2))/m4

print m1, m2, m3, m4

mu=R/(m1*q1+m2*q2+m3*q3)

mu1=q1*mu
mu2=q2*mu;
mu3=q3*mu;

p1=(mu1*((k21+k23+l2)*(k32+l3)-k23*k32)+mu2*k21*(k32+l3)+mu3*k21*k32)/m4
p2=(mu1*k12*(k32+l3)+mu2*(k32+l3)*(k12+l1)+mu3*k32*(k12+l1))/m4
p3=(mu1*k12*k23+mu2*k23*(k12+l1)+mu3*((k21+k23+l2)*(k12+l1)-k12*k21))/m4
print p1, p2, p3

#Solve the p1,p2,p3 differential equations using mathematica:
p1=(((k32*l2+(k23+l2)*l3)*mu1+k21*(l3*(mu1+mu2)+k32*(mu1+mu2+mu3)))*p0)/(k21*l1*(k32+l3)+(k12+l1)*(k32*l2+(k23+l2)*l3))
p2=((l1*(l3*mu2+k32*(mu2+mu3))+k12*(l3*(mu1+mu2)+k32*(mu1+mu2+mu3)))*p0)/(k21*l1*(k32+l3)+(k12+l1)*(k32*l2+(k23+l2)*l3))
p3=((l1*((k21+l2)*mu3+k23*(mu2+mu3))+k12*(l2*mu3+k23*(mu1+mu2+mu3)))*p0)/(k21*l1*(k32+l3)+(k12+l1)*(k32*l2+(k23+l2)*l3))

print p1, p2, p3

print m1, m2, m3, m4
print mu
print mu1, mu2, mu3, mu1+mu2+mu3
print p1, p2, p3

#p1+p2+p3
#p1/(p1+p2+p3)
#p2/(p1+p2+p3)
#p3/(p1+p2+p3)



#your parameters
PTENvol_frac = 0.56
nVacant_total = 17325
nInterface = 21175
nVolumeVacant = 279864-nInterface
nANIO_frac = 0.1 # 10%
nPIP2_frac = 0.03 # 3%
nPTEN_total = 35200

#PTEN fractions, PTEN volume state => 4
f4 = PTENvol_frac
f1 = p1*(1-f4)
f2 = p2*(1-f4)
f3 = p3*(1-f4)

mu1 = (f1*l1 + f1*k12 - f2*k21)/f4
mu2 = (f2*l2 + f2*k23 + f2*k21 - f1*k12 - f3*k32)/f4
mu3 = (f3*l3 + f3*k32 - f2*k23)/f4
#mu1 = 0.54
#mu2 = 1.38
#mu3 = 0.36

nPIP2_total = nPIP2_frac*nVacant_total
nANIO_total = nANIO_frac*nVacant_total
PTENp2_frac = f1
PTENa_frac = f2
PTEN_frac = f3

a = mu1+mu2+mu3
#print mu1, mu2, mu3
#print mu1/a, mu2/a, mu3/a


#ss = steady-state
nPTENvol_ss = PTENvol_frac*nPTEN_total
nPTENa_ss = PTENa_frac*nPTEN_total
nPTENp2_ss = PTENp2_frac*nPTEN_total
nPTEN_ss = PTEN_frac*nPTEN_total
nPIP2_ss = nPIP2_total-nPTENp2_ss
nANIO_ss = nANIO_total-nPTENa_ss
nVacant_ss = nVacant_total-nANIO_total-nPIP2_total
Volume = LengthX*LengthY*LengthZ

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

s = theSimulator.createEntity('Variable', 'Variable:/:PTENvol')
s.Value = nPTEN_total
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
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = k12
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l1
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = k21
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = k23
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = k32
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = mu1
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = mu2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = mu3
r.LogEvent = LogEvent
r.LogStart = 5

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
l.LogInterval = 5e-1
l.LogEnd = duration
l.Iterations = Iterations

run(duration+0.1)
