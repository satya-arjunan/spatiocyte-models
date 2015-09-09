
duration = 1000
Iterations = 1
VoxelRadius = 10e-9
LogEvent = 0
#LengthX = 10e-6
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
#p1, p2 and p3 (the values were adjusted manually by me)
k12 = 3.45
k21 = 4.1
k23 = 0.57

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
if(LengthX == 10e-6):
  print "here"
  nVacant_total = 38500
  nInterface = 47124
  nVolumeVacant = 620568-nInterface
nANIO_frac = 0.1 # 10%
nPIP2_frac = 0.06 # 3%

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
nPTEN_total = nPIP2_total*0.95
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
ProteinDiffusion_p2 = D1
ProteinDiffusion_v = D3
ProteinDiffusion_vol = 0.9e-12
LipidDiffusion = 0.5e-12
ClusterDiffusion_p2 = ProteinDiffusion_p2
ClusterDiffusion_a = ProteinDiffusion_p2
#ProteinDiffusion_vol = 16e-12

#diffusion step interval
PTENvol_dt = pow(2*VoxelRadius, 2)/(6*ProteinDiffusion_vol)
PTEN_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_v)
PTENa_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_a)
PTENp2_dt = pow(2*VoxelRadius, 2)/(4*ProteinDiffusion_p2)
PIP2_dt = pow(2*VoxelRadius, 2)/(4*LipidDiffusion)
ANIO_dt = pow(2*VoxelRadius, 2)/(4*LipidDiffusion)
PIP2c_dt = pow(2*VoxelRadius, 2)/(4*ClusterDiffusion_p2)
ANIOc_dt = pow(2*VoxelRadius, 2)/(4*ClusterDiffusion_a)


#DIRP rates
Ze = 3.0/12*(nANIO_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV2*nPTENvol_ss
PTENvol_to_a = a/Ze
PTENvol_to_ac = PTENvol_to_a

Ze = 3.0/12*(nVacant_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV3*nPTENvol_ss
PTENvol_to_v = a/Ze

Ze = 3.0/12*(nPIP2_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV1*nPTENvol_ss
PTENvol_to_p2 = a/Ze
PTENvol_to_p2c = PTENvol_to_p2

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt + (nPTEN_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k32*nPTEN_ss
v_to_a = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt + (nPTEN_ss/nVacant_total)*nANIO_ss*1/ANIOc_dt
a = k32*nPTEN_ss
v_to_ac = a/Ze

Ze = (nVacant_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt
a = k23*nPTENa_ss
a_to_v = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt + (nPTENa_ss/nVacant_total)*nPIP2_ss*1/PIP2_dt
a = k21*nPTENa_ss
a_to_p2 = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt + (nPTENa_ss/nVacant_total)*nPIP2_ss*1/PIP2c_dt
a = k21*nPTENa_ss
a_to_p2c = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt + (nPTENp2_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k12*nPTENp2_ss
p2_to_a = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt + (nPTENp2_ss/nVacant_total)*nANIO_ss*1/ANIOc_dt
a = k12*nPTENp2_ss
p2_to_ac = a/Ze

#Clustering
cl_a_to_a = 1
#cl_a_to_p2 = 0
cl_p2_to_p2 = 1
#cl_p2_to_a = 03

isDeoligomerize = 0
DeoligomerizeRate = 0.1
Deoligomerize = DeoligomerizeRate
DeoligomerizePTEN = DeoligomerizeRate

#PIP3 parameters---------------------------------------------------------------
#PI3K binds at low probability to the membrane
#It binds stably on PIP3 which allows it to bind to adjacent PIP2 to phosphorylate
#This causes positive feedback in PI3K recruitment and wave formation
nPI3K_total = 500
#PI3K recruitment to membrane
PI3Kvol_to_v = 0
PI3Kvol_to_p3 = 0.1
PI3Kvol_to_p3c = 0.1
PI3Kvol_to_p2 = 0.001
PI3Kvol_to_p2c = 0.001
#PI3K transfer on membrane
PI3Kv_to_p2 = 0.001
PI3Kv_to_p2c = 0.001
PI3Kv_to_p3 = 0.1
PI3Kv_to_p3c = 0.1
#First order reactions of PI3K to vacant on membrane
PI3Kp2_to_v = 1
PI3Kp2c_to_v = 1
PI3Kp3_to_v = 1
PI3Kp3c_to_v = 1
#PI3K dissocation from membrane
PI3Kv_to_vol = 1
PI3Kp2_to_vol = 0
PI3Kp2c_to_vol = 0
PI3Kp3_to_vol = 0
PI3Kp3c_to_vol = 0

#PI3K phosphorylation of PIP2
Phosphorylate = l2

cl_p2_to_p3 = 1
cl_p3_to_p3 = 1
cl_p3_to_p2 = 1

#PTEN diffusion on PIP3
a_to_p3 = a_to_p2*1.93/4.19
a_to_p3c = a_to_p2c*1.93/4.19
p3_to_a = p2_to_a*5.43/4.66
p3_to_ac = p2_to_ac*5.43/4.66
#PTEN recruitment to PIP3
PTENvol_to_p3 = PTENvol_to_p2/5 #PTEN has reduced kon on PIP3
PTENvol_to_p3c = PTENvol_to_p2c/4
#PTEN dissiociation from PIP3
l1_PTENp3 = 0 #PTEN has increased koff on PIP3, but after dephosphorylate
#PTEN dephosphoylation of PIP3
Dephosphorylate = l2 #PTEN has increased koff on PIP3 after dephosphorylate

DeoligomerizePI3K = DeoligomerizeRate
ClusterDiffusion_p3 = ClusterDiffusion_p2
ProteinDiffusion_p3 = ProteinDiffusion_p2
#-------------------------------------------------------------------------------

#cl_p2_to_p3 = 1
#cl_p3_to_p3 = 1
#cl_p3_to_p2 = 1
#a_to_p3 = a_to_p2
#a_to_p3c = a_to_p2c
#p3_to_a = p2_to_a
#p3_to_ac = p2_to_ac
#PI3Kvol_to_v = PTENvol_to_a
#PI3Kv_to_p2 = a_to_p2
#PI3Kv_to_p2c = PI3Kv_to_p2
#l1_PTENp3 = l1
#l3_PI3K = l2
#Dephosphorylate = 3
#Phosphorylate = 3
#PTENvol_to_p3 = PTENvol_to_p2
#PTENvol_to_p3c = PTENvol_to_p2c
#DeoligomerizePI3K = 3
#ClusterDiffusion_p3 = ClusterDiffusion_p2
#ProteinDiffusion_p3 = ProteinDiffusion_p2

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
theSimulator.createEntity('Variable', 'Variable:/:PIP3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENa').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTEN').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:ANIOc').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENac').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3K').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kvol').Value = nPI3K_total
theSimulator.createEntity('Variable', 'Variable:/:PIP3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Ka').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3Kac').Value = 0
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
f.VariableReferenceList = [['_', 'Variable:/:PIP3']]
f.VariableReferenceList = [['_', 'Variable:/:PI3K']]
f.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
f.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
f.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
f.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
f.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
f.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
f.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
#f.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
f.Periodic = 0

l = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#l.VariableReferenceList = [['_', 'Variable:/:ANIO']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
#l.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
#l.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
#l.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#l.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#l.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
#l.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
l.VariableReferenceList = [['_', 'Variable:/:PI3K']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
##l.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
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
populator.VariableReferenceList = [['_', 'Variable:/:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
populator.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
populator.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#
##Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIOc')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
diffuser.D = ClusterDiffusion_a

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
diffuser.D = ClusterDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
diffuser.D = ClusterDiffusion_p3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENac']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_a

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_p3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIO')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIO']]
diffuser.D = LipidDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
diffuser.D = LipidDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3']]
diffuser.D = LipidDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = ProteinDiffusion_v

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3K']]
diffuser.D = ProteinDiffusion_v

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENa')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENa']]
diffuser.D = ProteinDiffusion_a

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
diffuser.D = ProteinDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
diffuser.D = ProteinDiffusion_p2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
diffuser.D = ProteinDiffusion_p3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
diffuser.D = ProteinDiffusion_p3

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

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENvol')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
diffuser.D = ProteinDiffusion_vol

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kvol')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
diffuser.D = ProteinDiffusion_vol
##-------------------------------------------------------------------------------
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p2_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p3_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p2_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12p3_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p3_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p2_to_a
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12p3c')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p3_to_a
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

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12p3cc')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '1']]
r.ForcedSequence = 1
r.p = p3_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.ForcedSequence = 1
r.p = a_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '1']]
r.ForcedSequence = 1
r.p = a_to_p3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.ForcedSequence = 1
r.p = a_to_p2c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21p3_c')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '1']]
r.ForcedSequence = 1
r.p = a_to_p3c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21c')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.ForcedSequence = 1
r.p = a_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21p3c')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '1']]
r.ForcedSequence = 1
r.p = a_to_p3
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

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21p3cc')
r.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '1']]
r.ForcedSequence = 1
r.p = a_to_p3c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
#r.ForcedSequence = 1
r.k = k23
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

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r31pi3k')
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
r.ForcedSequence = 1
r.p = PI3Kv_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32cpi3k')
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '1']]
r.ForcedSequence = 1
r.p = PI3Kv_to_p2c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r31pi3kp3')
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
r.ForcedSequence = 1
r.p = PI3Kv_to_p3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32cpi3kp3')
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '1']]
r.ForcedSequence = 1
r.p = PI3Kv_to_p3c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.p = PTENvol_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3', '1']]
r.p = PTENvol_to_p3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1c')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '1']]
r.p = PTENvol_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV1p3c')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '1']]
r.p = PTENvol_to_p3
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
r.p = PTENvol_to_ac
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.p = PTENvol_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3pi3k')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '1']]
r.p = PI3Kvol_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3pi3kp3')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
r.p = PI3Kvol_to_p3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3pi3kp3c')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '1']]
r.p = PI3Kvol_to_p3c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3pi3kp2')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
r.p = PI3Kvol_to_p2
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:rV3pi3kp2c')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '1']]
r.p = PI3Kvol_to_p2c
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp2v')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '1']]
r.k = PI3Kp2_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp2vol')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
r.k = PI3Kp2_to_vol
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp2cv')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '1']]
r.k = PI3Kp2c_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp2cvol')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
r.k = PI3Kp2c_to_vol
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp3v')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '1']]
r.k = PI3Kp3_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp3vol')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
r.k = PI3Kp3_to_vol
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp3cv')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '1']]
r.k = PI3Kp3c_to_v
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rPI3Kp3cvol')
r.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
r.k = PI3Kp3c_to_vol
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = l3
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3Vpi3k')
r.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
r.k = PI3Kv_to_vol
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

#Handled by phosphorylation reaction
#r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1Vp3')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp3', '-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
#r.k = l1_PTENp3
#r.LogEvent = LogEvent
#r.LogStart = 5

#r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1Vp3c')
#r.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
#r.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
#r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
#r.k = l1_PTENp3
#r.LogEvent = LogEvent
#r.LogStart = 5


#Phosphorylation-dephosphorylation----------------------------------------------
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:p1')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','1']]
binder.k = Phosphorylate

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:p2')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','1']]
binder.k = Phosphorylate

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:p3')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','1']]
binder.k = Dephosphorylate

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:p4')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','1']]
binder.k = Dephosphorylate
#-------------------------------------------------------------------------------




l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]  #0
l.VariableReferenceList = [['_', 'Variable:/:PTENp3']]  #1
l.VariableReferenceList = [['_', 'Variable:/:PTENp2c']] #2
l.VariableReferenceList = [['_', 'Variable:/:PTENp3c']] #3
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]   #4
l.VariableReferenceList = [['_', 'Variable:/:PTENac']]  #5
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]    #6
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']] #7
l.VariableReferenceList = [['_', 'Variable:/:PI3K']]    #8
l.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']] #9
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]  #10
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']] #11
l.VariableReferenceList = [['_', 'Variable:/:PIP3']]    #12
l.VariableReferenceList = [['_', 'Variable:/:PIP2']]    #13
l.VariableReferenceList = [['_', 'Variable:/:PIP3c']]   #14
l.VariableReferenceList = [['_', 'Variable:/:PIP2c']]   #15
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]  #16
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']] #17
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

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp1a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp1p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp1p3a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p2

#PTENp2 + PIP2c => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp2')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp2a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3cp3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3cp3a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p2

#PTENp2c + PIP2 => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp3p3a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p2

#PTENp2c + PIP2c => PIP2c + PTENp2c
r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp4')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p2

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp4a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p2_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp4p3')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p3

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:pp4p3a')
r.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
r.ForcedSequence = 1
r.p = cl_p3_to_p2


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

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d2p3')
react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
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

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d5p3')
react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = DeoligomerizePTEN

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d8')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = DeoligomerizePI3K

#PI3Kp3c => PI3Kp3
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d9')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = DeoligomerizePI3K
#-------------------------------------------------------------------------------

run(duration+0.1)
