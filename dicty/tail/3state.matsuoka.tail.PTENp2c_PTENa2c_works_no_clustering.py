
duration = 10
Iterations = 10
VoxelRadius = 10e-9
LogEvent = 0
LengthX = 4.5e-6
LengthY = 1.35e-6
LengthZ = 0.26e-6
FileName = "IterateLog.csv"

#parameters from 2013.matsuoka.pcb
D1 = 0.034e-12
D2 = 0.150e-12
D3 = 0.722e-12
p1 = 0.639
p2 = 0.331
p3 = 1-p1-p2
q1 = 0.298
q2 = 0.581
q3 = 0.121
l1 = 0.010
l2 = 4.708
l3 = 13.919
k12 = 4.663
k21 = 4.187
k23 = 0.414
k32 = 0.028
PTEN_cytosol = 20000.0
#PTEN_membrane = 15200.0
PTEN_membrane = 20000.0

#Uncomment the following to correct the final PTEN ratio to the correct 
#p1, p2 and p3 (the were values were adjusted manually by me)
k12 = 3.063
k21 = 4.100
k23 = 0.574

m4=(k12+l1)*(k21+k23+l2)*(k32+l3)-k12*k21*(k32+l3)-k23*k32*(k12+l1)
m1=((k21+k23+l2)*(k32+l3)-k23*k32+k12*(k32+l3)+k12*k23)/m4
m2=(k21*(k32+l3)+(k32+l3)*(k12+l1)+k23*(k12+l1))/m4
m3=(k21*k32+k32*(k12+l1)+(k21+k23+l2)*(k12+l1)-k12*k21)/m4

#Here mu1 does not include PTEN_cytosol in its term
#PTEN_membrane = PTEN_cytosol*(m1*mu1+m2*mu2+m3*mu3)
#              = PTEN_cytosol*mu*(m1*q1+m2*q2+m3*q3)
mu = PTEN_membrane/(PTEN_cytosol*(m1*q1+m2*q2+m3*q3))

mu1=q1*mu
mu2=q2*mu
mu3=q3*mu

#print "ori:", p1, p2, p3
p1=(mu1*((k21+k23+l2)*(k32+l3)-k23*k32)+mu2*k21*(k32+l3)+mu3*k21*k32)/m4
p2=(mu1*k12*(k32+l3)+mu2*(k32+l3)*(k12+l1)+mu3*k32*(k12+l1))/m4
p3=(mu1*k12*k23+mu2*k23*(k12+l1)+mu3*((k21+k23+l2)*(k12+l1)-k12*k21))/m4

a = p1+p2+p3
p1 = p1/a
p2 = p2/a
p3 = p3/a
#print p1, p2, p3

kV1 = mu1
kV2 = mu2
kV3 = mu3


#your parameters
PTENvol_frac = PTEN_cytosol/(PTEN_cytosol+PTEN_membrane)
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

#kV1 = (f1*l1 + f1*k12 - f2*k21)/f4
#kV2 = (f2*l2 + f2*k23 + f2*k21 - f1*k12 - f3*k32)/f4
#kV3 = (f3*l3 + f3*k32 - f2*k23)/f4
nPIP2_total = nPIP2_frac*nVacant_total
nANIO_total = nANIO_frac*nVacant_total
PTENp2_frac = f1
PTENa_frac = f2
PTEN_frac = f3

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


#DIRP rates
Ze = 3.0/12*(nANIO_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV2*nPTENvol_ss
PTENvol_to_a = a/Ze

Ze = 3.0/12*(nVacant_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV3*nPTENvol_ss
PTENvol_to_v = a/Ze

Ze = 3.0/12*(nPIP2_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV1*nPTENvol_ss
PTENvol_to_p2 = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt + (nPTEN_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k32*nPTEN_ss
v_to_a = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt
a = k32*nPTEN_ss
v_to_ac = a/Ze

Ze = (nVacant_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt
a = k23*nPTENa_ss
a_to_v = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt + (nPTENa_ss/nVacant_total)*nPIP2_ss*1/PIP2_dt
a = k21*nPTENa_ss
a_to_p2 = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt
a = k21*nPTENa_ss
a_to_p2c = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt + (nPTENp2_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k12*nPTENp2_ss
p2_to_a = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt
a = k12*nPTENp2_ss
p2_to_ac = a/Ze

#Clustering
cl_a_to_a = 0
cl_a_to_p2 = 0
cl_p2_to_p2 = 0
cl_p2_to_a = 0
#a_to_a = 1.0
#a_to_p2 = 1.0
#p2_to_p2 = 1.0
#p2_to_a = 1.0

isDeoligomerize = 0
Deoligomerize = 3
DeoligomerizePTEN = 3
DeoligomerizePI3K = 3

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

#s = theSimulator.createEntity('Variable', 'Variable:/:PI3Kvol')
#s.Value = 0
#s.Name = "HD"

#s = theSimulator.createEntity('Variable', 'Variable:/:PTEN')
#s.Value = 0
#s.Name = "HD"

#s = theSimulator.createEntity('Variable', 'Variable:/:PTENp2')
#s.Value = 0
#s.Name = "HD"

#s = theSimulator.createEntity('Variable', 'Variable:/:PIP2')
#s.Value = nPIP2_total
#s.Name = "HD"

theSimulator.createEntity('Variable', 'Variable:/:PTENvol').Value = nPTEN_total
theSimulator.createEntity('Variable', 'Variable:/:ANIO').Value = nANIO_total
theSimulator.createEntity('Variable', 'Variable:/:PIP2').Value = nPIP2_total
theSimulator.createEntity('Variable', 'Variable:/:PTENa').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTEN').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:ANIOc').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENac').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PIP3').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3K').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PIP3c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PTENp3').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PTENp3c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Ka').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kac').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3c').Value = 0
#
f = theSimulator.createEntity('CompartmentProcess', 'Process:/:Surface')
f.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
f.VariableReferenceList = [['_', 'Variable:/:ANIO']]
f.VariableReferenceList = [['_', 'Variable:/:PTENa']]
f.VariableReferenceList = [['_', 'Variable:/:PIP2']]
f.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
f.VariableReferenceList = [['_', 'Variable:/:PTEN']]
f.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
f.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
f.VariableReferenceList = [['_', 'Variable:/:PTENac']]
f.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#f.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#f.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
#f.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
#f.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
#f.Periodic = 0

l = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
l.VariableReferenceList = [['_', 'Variable:/:ANIO']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PIP2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
l.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
l.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
l.VariableReferenceList = [['_', 'Variable:/:PTENac']]
l.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
##l.VariableReferenceList = [['_', 'Variable:/:PIP3']]
##l.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
##l.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
##l.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3K']]
l.LogInterval = 1e-1
#
#logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
##logger.VariableReferenceList = [['_', 'Variable:/:ANIO']]
##logger.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
##logger.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
##logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
###logger.VariableReferenceList = [['_', 'Variable:/:PTENa']]
###logger.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
###logger.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
###logger.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
##logger.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
##logger.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#logger.LogInterval = 1e-1
#logger.LogEnd = duration
#logger.Iterations = 1
#
#logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:pten')
#logger.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENa']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#logger.LogInterval = 1e-1
#logger.LogEnd = duration
#logger.FileName = "pten.csv"
#logger.Iterations = 1
#
populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:ANIO']]
populator.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#populator.VariableReferenceList = [['_', 'Variable:/:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#populator.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
#populator.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#
##Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIO')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIO']]
diffuser.D = LipidDiffusion
#
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
diffuser.D = LipidDiffusion
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#diffuser.D = LipidDiffusion
#
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = ProteinDiffusion_v
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#diffuser.D = ProteinDiffusion_v
#
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENa')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENa']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_a

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENac']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_a

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p2

#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p3
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3c')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p3
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Ka')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_a
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kac')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_a
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p2
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2c')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p2
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p3
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3c')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p3
#
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENvol')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
diffuser.D = ProteinDiffusion_vol
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kvol')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
#diffuser.D = ProteinDiffusion_vol
##-------------------------------------------------------------------------------



r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.ForcedSequence = 1
r.p = p2_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p2_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.ForcedSequence = 1
r.p = p2_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12cc')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p2_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l1
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1Vc')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l1
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.ForcedSequence = 1
r.p = a_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.ForcedSequence = 1
r.p = a_to_p2c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21c')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.ForcedSequence = 1
r.p = a_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21cc')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.ForcedSequence = 1
r.p = a_to_p2c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2Vc')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.ForcedSequence = 1
r.p = a_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r23c')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.ForcedSequence = 1
r.p = a_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.ForcedSequence = 1
r.p = v_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32c')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = v_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.p = PTENvol_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1c')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.p = PTENvol_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.p = PTENvol_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV2c')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.p = PTENvol_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.p = PTENvol_to_v
r.LogEvent = LogEvent
r.LogStart = 5

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PTENac']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
l.LogInterval = 1e-1
l.LogEnd = duration
l.Iterations = Iterations
l.FileName = FileName

#Lipid clustering reactions-------------------------------------------------------
#PTENa + ANIO => ANIOc + PTENac
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:aa1')
r.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
r.ForcedSequence = 1
r.p = cl_a_to_a

#PTENa + ANIOc => ANIOc + PTENac
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:aa2')
r.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
r.ForcedSequence = 1
r.p = cl_a_to_a

#PTENac + ANIO => ANIOc + PTENac
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:aa3')
r.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
r.ForcedSequence = 1
r.p = cl_a_to_a

#PTENac + ANIOc => ANIOc + PTENac
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:aa4')
r.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
r.ForcedSequence = 1
r.p = cl_a_to_a

#PTENa + PIP2 => ANIOc + PTENp2c
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ap1')
#r.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
#r.ForcedSequence = 1
#r.p = a_to_p2

#PTENa + PIP2c => ANIOc + PTENp2c
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ap2')
#r.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
#r.ForcedSequence = 1
#r.p = a_to_p2

#PTENac + PIP2 => ANIOc + PTENp2c
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ap3')
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
#r.ForcedSequence = 1
#r.p = a_to_p2

#PTENac + PIP2c => ANIOc + PTENp2c
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ap4')
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
#r.ForcedSequence = 1
#r.p = a_to_p2

#PTENp2 + ANIO => PIP2c + PTENac
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pa1')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
#r.ForcedSequence = 1
#r.p = p2_to_a

#PTENp2c + ANIO => PIP2c + PTENac
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pa2')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
#r.ForcedSequence = 1
#r.p = p2_to_a

#PTENp2c + ANIOc => PIP2c + PTENac
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pa3')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
#r.ForcedSequence = 1
#r.p = p2_to_a

##PTENp2 + ANIOc => PIP2c + PTENac
#r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pa4')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
#r.ForcedSequence = 1
#r.p = p2_to_a

#PTENp2 + PIP2 => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp1')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

#PTENp2 + PIP2c => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp2')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

#PTENp2c + PIP2 => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

#PTENp2c + PIP2c => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp4')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2



#Deoligomerization--------------------------------------------------------------
#ANIOc => ANIO
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d1')
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize

#PIP2c => PIP2
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d2')
react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize

#PTENac => PTENa
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d4')
react.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PTENp2c => PTENp2
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d5')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = DeoligomerizePTEN


#PIP3c => PIP3
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d3')
#react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
#react.Deoligomerize = isDeoligomerize
#react.SearchVacant = 1
#react.k = Deoligomerize

#PTENp3c => PTENp3
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d6')
#react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '1']]
#react.Deoligomerize = isDeoligomerize
#react.SearchVacant = 1
#react.k = DeoligomerizePTEN

##PI3Kac => PI3Ka
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d7')
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kac', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PI3Ka', '1']]
#react.Deoligomerize = isDeoligomerize
#react.SearchVacant = 1
#react.k = DeoligomerizePI3K
#
##PI3Kp2c => PI3Kp2
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d8')
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
#react.Deoligomerize = isDeoligomerize
#react.SearchVacant = 1
#react.k = DeoligomerizePI3K
#
##PI3Kp3c => PI3Kp3
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d9')
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
#react.Deoligomerize = isDeoligomerize
#react.SearchVacant = 1
#react.k = DeoligomerizePI3K
#-------------------------------------------------------------------------------

run(duration+0.1)
