
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
nPIP2_frac = 0.03 # 3%

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

#Diffusion rates
VolumeDiffusion = 0.9e-12
LipidDiffusion = D2
ClusterDiffusion = D1
D_PTENvol = VolumeDiffusion
D_PI3Kvol = VolumeDiffusion
D_ANIO = LipidDiffusion
D_PIP2 = LipidDiffusion
D_PIP3 = LipidDiffusion
D_ANIOc = ClusterDiffusion
D_PIP2c = ClusterDiffusion
D_PIP3c = ClusterDiffusion
D_PTENv = D3
D_PI3Kv = D3
DW_PTENa = D2
DW_PTENac = D2
DW_PTENp2 = D1
DW_PTENp2c = D1
DW_PTENp3 = D2
DW_PTENp3c = D2
DW_PI3Ka = D2
DW_PI3Kac = D2
DW_PI3Kp2 = D2
DW_PI3Kp2c = D2
DW_PI3Kp3 = D1
DW_PI3Kp3c = D1


#diffusion step interval
PTENvol_dt = pow(2*VoxelRadius, 2)/(6*D_PTENvol)
PTEN_dt = pow(2*VoxelRadius, 2)/(4*D_PTENv)
PTENa_dt = pow(2*VoxelRadius, 2)/(4*DW_PTENa)
PTENp2_dt = pow(2*VoxelRadius, 2)/(4*DW_PTENp2)
PIP2_dt = pow(2*VoxelRadius, 2)/(4*D_PIP2)
ANIO_dt = pow(2*VoxelRadius, 2)/(4*D_ANIO)
PIP2c_dt = pow(2*VoxelRadius, 2)/(4*D_PIP2c)
ANIOc_dt = pow(2*VoxelRadius, 2)/(4*D_ANIOc)


#Parameter calculations---------------------------------------------------------
#DIRP rates
Ze = 3.0/12*(nANIO_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV2*nPTENvol_ss
pV2 = a/Ze

Ze = 3.0/12*(nVacant_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV3*nPTENvol_ss
pV3 = a/Ze

Ze = 3.0/12*(nPIP2_ss/nVacant_total*nInterface/nVolumeVacant)*nPTENvol_ss*1/PTENvol_dt
a = kV1*nPTENvol_ss
pV1 = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt + (nPTEN_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k32*nPTEN_ss
p32 = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTEN_ss*1/PTEN_dt + (nPTEN_ss/nVacant_total)*nANIO_ss*1/ANIOc_dt
a = k32*nPTEN_ss
p32c = a/Ze

Ze = (nVacant_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt
a = k23*nPTENa_ss
p23 = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt + (nPTENa_ss/nVacant_total)*nPIP2_ss*1/PIP2_dt
a = k21*nPTENa_ss
p21 = a/Ze

Ze = (nPIP2_ss/nVacant_total)*nPTENa_ss*1/PTENa_dt + (nPTENa_ss/nVacant_total)*nPIP2_ss*1/PIP2c_dt
a = k21*nPTENa_ss
p21c = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt + (nPTENp2_ss/nVacant_total)*nANIO_ss*1/ANIO_dt
a = k12*nPTENp2_ss
p12 = a/Ze

Ze = (nANIO_ss/nVacant_total)*nPTENp2_ss*1/PTENp2_dt + (nPTENp2_ss/nVacant_total)*nANIO_ss*1/ANIOc_dt
a = k12*nPTENp2_ss
p12c = a/Ze

#-------------------------------------------------------------------------------
nPI3K_total = 0

#Membrane recruitment first order rates
PTENvol_to_v = pV3
PTENvol_to_a = pV3
PTENvol_to_ac = pV2*1.5
PTENvol_to_p2 = pV3
PTENvol_to_p2c = pV1*1.5
PTENvol_to_p3 = pV3 #PIP3 reduces PTEN kon, try pV3 if want lower
PTENvol_to_p3c = pV2 #PIP3 reduces PTEN kon, try pV3 if want lower

PI3Kvol_to_v = pV3
PI3Kvol_to_a = pV2
PI3Kvol_to_ac = pV2
PI3Kvol_to_p2 = pV2
PI3Kvol_to_p2c = pV2
PI3Kvol_to_p3 = pV1
PI3Kvol_to_p3c = pV1

#Membrane dissociation first order rates
PTENv_to_vol = l3
PTENa_to_vol = l3
PTENac_to_vol = l2
PTENp2_to_vol = l1*10
PTENp2c_to_vol = l1
PTENp3_to_vol = 0.0 #handled by dephosphorylatio
PTENp3c_to_vol = 0.0 #handled by dephosphorylation

PI3Kv_to_vol = l3
PI3Ka_to_vol = l2
PI3Kac_to_vol = l2
PI3Kp2_to_vol = 0.0 #handled by phosphorylation
PI3Kp2c_to_vol = 0.0 #handled by phosphorylation
PI3Kp3_to_vol = l1
PI3Kp3c_to_vol = l1

#print "pV3:", pV3, "pV2:", pV2, "pV1:", pV1, "l3:", l3, "l2:", l2, "l1:", l1 
#print "p32:", p32, "p32c:", p32c, "p21:", p21, "p21c:", p21c, "p12:", p12, "p12c:", p12c

#pV3: 0.00108386622082 pV2: 0.0477087890453 pV1: 0.108928804711 l3: 13.919 l2: 4.708 l1: 0.01
#p32: 3.38340700042e-05 p32c: 3.9025541063e-05 p21: 0.0641031708302 p21c: 0.104516039397 p12: 0.0197566801631 p12c: 0.0534592522061

#Phosphorylation-dephosphorylation
Phosphorylate = 3.0
Dephosphorylate = 3.0

#First order state transition rates
PTENa_to_PTENv = k23
PTENac_to_PTENv = k23
PTENp3_to_PTENv = k23
PTENp3c_to_PTENv = k23

#Reaction-driven state transition of PTEN on membrane
PTENv_to_a = p32
PTENv_to_ac = p32c
PTENv_to_p2 = 0.0
PTENv_to_p2c = 0.0
PTENv_to_p3 = PTENv_to_a
PTENv_to_p3c = PTENv_to_ac

PTENa_to_v = 0.01 #maintain diffusion coefficient by swapping with vacant
PTENa_to_a = 1.0
PTENa_to_ac = 1.0
PTENa_to_p2 = p21
PTENa_to_p2c = p21c
PTENa_to_p3 = 1.0
PTENa_to_p3c = 1.0

PTENac_to_v = 0.01 #maintain diffusion coefficient by swapping with vacant
PTENac_to_a = 1.0
PTENac_to_ac = 1.0
PTENac_to_p2 = p21
PTENac_to_p2c = p21c
PTENac_to_p3 = 1.0
PTENac_to_p3c = 1.0

PTENp2_to_v = 0.01 #maintain diffusion coefficient by swapping with vacant
PTENp2_to_a = p12
PTENp2_to_ac = p12c
PTENp2_to_p2 = 1.0
PTENp2_to_p2c = 1.0
PTENp2_to_p3 = p12
PTENp2_to_p3c = p12

PTENp2c_to_v = 0.01 #maintain diffusion coefficient by swapping with vacant
PTENp2c_to_a = p12
PTENp2c_to_ac = p12c
PTENp2c_to_p2 = 1.0
PTENp2c_to_p2c = 1.0
PTENp2c_to_p3 = p12
PTENp2c_to_p3c = p12c

PTENp3_swap_v = 0
PTENp3_to_v = 0
PTENp3_to_a = 1.0
PTENp3_to_ac = 1.0
PTENp3_to_p2 = p21
PTENp3_to_p2c = p21c
PTENp3_to_p3 = 1.0
PTENp3_to_p3c = 1.0

PTENp3c_to_v = 0
PTENp3c_to_a = 0
PTENp3c_to_ac = 0
PTENp3c_to_p2 = 0
PTENp3c_to_p2c = 0
PTENp3c_to_p3 = 0
PTENp3c_to_p3c = 0

#Reaction-driven state transition of PI3K on membrane
PI3Kv_to_a = 0.0
PI3Kv_to_ac = 0.0
PI3Kv_to_p2 = 0.0
PI3Kv_to_p2c = 0.0
PI3Kv_to_p3 = 0.0
PI3Kv_to_p3c = 0.0

PI3Ka_to_v = 0.0
PI3Ka_to_a = 0.0
PI3Ka_to_ac = 0.0
PI3Ka_to_p2 = 0.0
PI3Ka_to_p2c = 0.0
PI3Ka_to_p3 = 0.0
PI3Ka_to_p3c = 0.0

PI3Kac_to_v = 0.0
PI3Kac_to_a = 0.0
PI3Kac_to_ac = 0.0
PI3Kac_to_p2 = 0.0
PI3Kac_to_p2c = 0.0
PI3Kac_to_p3 = 0.0
PI3Kac_to_p3c = 0.0

PI3Kp2_to_v = 0.0
PI3Kp2_to_a = 0.0
PI3Kp2_to_ac = 0.0
PI3Kp2_to_p2 = 0.0
PI3Kp2_to_p2c = 0.0
PI3Kp2_to_p3 = 0.0
PI3Kp2_to_p3c = 0.0

PI3Kp2c_to_v = 0.0
PI3Kp2c_to_a = 0.0
PI3Kp2c_to_ac = 0.0
PI3Kp2c_to_p2 = 0.0
PI3Kp2c_to_p2c = 0.0
PI3Kp2c_to_p3 = 0.0
PI3Kp2c_to_p3c = 0.0

PI3Kp3_to_v = 0.0
PI3Kp3_to_a = 0.0
PI3Kp3_to_ac = 0.0
PI3Kp3_to_p2 = 0.0
PI3Kp3_to_p2c = 0.0
PI3Kp3_to_p3 = 0.0
PI3Kp3_to_p3c = 0.0

PI3Kp3c_to_v = 0.0
PI3Kp3c_to_a = 0.0
PI3Kp3c_to_ac = 0.0
PI3Kp3c_to_p2 = 0.0
PI3Kp3c_to_p2c = 0.0
PI3Kp3c_to_p3 = 0.0
PI3Kp3c_to_p3c = 0.0

#Deoligomerization first order rates
isDeoligomerize = 0
kd = 3
Deoligomerize_ANIOc = kd
Deoligomerize_PIP2c = kd
Deoligomerize_PIP3c = kd
Deoligomerize_PTENac = kd
Deoligomerize_PTENp2c = kd
Deoligomerize_PTENp3c = kd
Deoligomerize_PI3Kac = kd
Deoligomerize_PI3Kp2c = kd
Deoligomerize_PI3Kp3c = kd

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
theSimulator.createEntity('Variable', 'Variable:/:PI3Ka').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kac').Value = 0

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
f.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
f.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
f.Periodic = 0

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
l.VariableReferenceList = [['_', 'Variable:/:PIP3']]
l.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
l.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
l.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
l.VariableReferenceList = [['_', 'Variable:/:PI3K']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
l.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
l.LogInterval = 1e-1

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
l.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]   #18
l.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]  #19
l.LogInterval = 1e-1
l.LogEnd = duration
l.Iterations = Iterations
l.FileName = FileName


populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:ANIO']]
populator.VariableReferenceList = [['_', 'Variable:/:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
populator.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
populator.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#

#Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENvol')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
diffuser.D = D_PTENvol

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kvol')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
diffuser.D = D_PI3Kvol

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIO')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIO']]
diffuser.D = D_ANIO

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
diffuser.D = D_PIP2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3']]
diffuser.D = D_PIP3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIOc')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
diffuser.D = D_ANIOc

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
diffuser.D = D_PIP2c

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
diffuser.D = D_PIP3c

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = D_PTENv

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3K']]
diffuser.D = D_PI3Kv

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENa')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENa']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENa

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENac']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENac

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENp2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENp2c

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENp3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
diffuser.WalkReact = 1
diffuser.D = DW_PTENp3c

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Ka')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Ka

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Kac

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Kp2

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Kp2c

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Kp3

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
diffuser.WalkReact = 1
diffuser.D = DW_PI3Kp3c
#-------------------------------------------------------------------------------

#Membrane recruitment-----------------------------------------------------------
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v1')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.p = PTENvol_to_v

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','1']]
binder.p = PTENvol_to_a

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v3')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.p = PTENvol_to_ac

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v4')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','1']]
binder.p = PTENvol_to_p2

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v5')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.p = PTENvol_to_p2c

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v6')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','1']]
binder.p = PTENvol_to_p3

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v7')
binder.VariableReferenceList = [['_', 'Variable:/:PTENvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.p = PTENvol_to_p3c

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v8')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.p = PI3Kvol_to_v

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v9')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','1']]
binder.p = PI3Kvol_to_a

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v10')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.p = PI3Kvol_to_ac

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v11')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','1']]
binder.p = PI3Kvol_to_p2

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v12')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.p = PI3Kvol_to_p2c

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v13')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','1']]
binder.p = PI3Kvol_to_p3

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:v14')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kvol','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.p = PI3Kvol_to_p3c
#-------------------------------------------------------------------------------

#Membrane dissociation----------------------------------------------------------
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd1')
react.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
react.k = PTENv_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd2')
react.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
react.k = PTENa_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd3')
react.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
react.k = PTENac_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd4')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
react.k = PTENp2_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd5')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
react.k = PTENp2c_to_vol

#Handled by dephosphorylation reaction
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd6')
#react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
#react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
#react.k = PTENp3_to_vol

#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd7')
#react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
#react.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
#react.k = PTENp3c_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd8')
react.VariableReferenceList = [['_', 'Variable:/:PI3K', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
react.k = PI3Kv_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd9')
react.VariableReferenceList = [['_', 'Variable:/:PI3Ka', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
react.k = PI3Ka_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd10')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
react.k = PI3Kac_to_vol

#Handled by Phosphorylation reaction
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd11')
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
#react.k = PI3Kp2_to_vol
#
#react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd12')
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '1']]
#react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
#react.k = PI3Kp2c_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd13')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
react.k = PI3Kp3_to_vol

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:vd14')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kvol', '1']]
react.k = PI3Kp3_to_vol
#-------------------------------------------------------------------------------

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


#First-order state transitions--------------------------------------------------
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:tPTENa_to_PTENv')
react.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
react.SearchVacant = 1
react.k = PTENa_to_PTENv

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:tPTENac_to_PTENv')
react.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
react.SearchVacant = 1
react.k = PTENac_to_PTENv

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:tPTENp3_to_PTENv')
react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
react.SearchVacant = 1
react.k = PTENp3_to_PTENv

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:tPTENp3c_to_PTENv')
react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '1']]
react.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
react.SearchVacant = 1
react.k = PTENp3c_to_PTENv
#-------------------------------------------------------------------------------

#Reaction-driven diffusion------------------------------------------------------
#PTEN to other voxels
#PTEN + ANIO => Vacant + PTENa
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_a

#PTEN + ANIOc => Vacant + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_ac

#PTEN + PIP2 => Vacant + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_p2

#PTEN + PIP2c => Vacant + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_p2c

#PTEN + PIP3 => Vacant + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_p3

#PTEN + PIP3c => Vacant + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENv_to_p3c


#PTENa to other voxels
#PTENa + Vacant => ANIO + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_v

#PTENa + ANIO => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r8')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_a

#PTENa + ANIOc => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r9')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_ac

#PTENa + PIP2 => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r10')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_p2

#PTENa + PIP2c => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r11')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_p2c

#PTENa + PIP3 => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_p3

#PTENa + PIP3c => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r13')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENa_to_p3c


#PTENac to other voxels
#PTENac + Vacant => ANIOc + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r14')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_v

#PTENac + ANIO => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r15')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_a

#PTENac + ANIOc => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r16')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_ac

#PTENac + PIP2 => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r17')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_p2

#PTENac + PIP2c => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r18')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_p2c

#PTENac + PIP3 => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r19')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_p3

#PTENac + PIP3c => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r20')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENac_to_p3c


#PTENp2 to other voxels
#PTENp2 + Vacant => PIP2 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_v

#PTENp2 + ANIO => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r22')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_a

#PTENp2 + ANIOc => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r23')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_ac

#PTENp2 + PIP2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r24')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_p2

#PTENp2 + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r25')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_p2c

#PTENp2 + PIP3 => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r26')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_p3

#PTENp2 + PIP3c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r27')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2_to_p3c


#PTENp2c to other voxels
#PTENp2c + Vacant => PIP2c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r28')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_v

#PTENp2c + ANIO => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r29')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_a

#PTENp2c + ANIOc => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r30')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_ac

#PTENp2c + PIP2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r31')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_p2

#PTENp2c + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_p2c

#PTENp2c + PIP3 => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r33')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_p3

#PTENp2c + PIP3c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r34')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp2c_to_p3c


#PTENp3 to other voxels
#PTENp3 + Vacant => PIP3 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r35swap')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_swap_v

#binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r35')
#binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
#binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
#binder.VariableReferenceList = [['_', 'Variable:/:PIP3','1']]
#binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
#binder.ForcedSequence = 1
#binder.p = PTENp3_to_v

#PTENp3 + ANIO => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r36')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_a

#PTENp3 + ANIOc => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r37')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_ac

#PTENp3 + PIP2 => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r38')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_p2

#PTENp3 + PIP2c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r39')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_p2c

#PTENp3 + PIP3 => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r40')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_p3

#PTENp3 + PIP3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r41')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3_to_p3c


#PTENp3c to other voxels
#PTENp3c + Vacant => PIP3c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r42')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_v

#PTENp3c + ANIO => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r43')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_a

#PTENp3c + ANIOc => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r44')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_ac

#PTENp3c + PIP2 => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r45')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_p2

#PTENp3c + PIP2c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r46')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_p2c

#PTENp3c + PIP3 => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r47')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_p3

#PTENp3c + PIP3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r48')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = PTENp3c_to_p3c
#-------------------------------------------------------------------------------

#Reaction-driven diffusion------------------------------------------------------
#PI3K to other voxels
#PI3K + ANIO => Vacant + PI3Ka
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir1')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_a

#PI3K + ANIOc => Vacant + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir2')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_ac

#PI3K + PIP2 => Vacant + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_p2

#PI3K + PIP2c => Vacant + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir4')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_p2c

#PI3K + PIP3 => Vacant + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir5')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_p3

#PI3K + PIP3c => Vacant + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir6')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kv_to_p3c


#PI3Ka to other voxels
#PI3Ka + Vacant => ANIO + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir7')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_v

#PI3Ka + ANIO => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir8')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_a

#PI3Ka + ANIOc => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir9')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_ac

#PI3Ka + PIP2 => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir10')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_p2

#PI3Ka + PIP2c => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir11')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_p2c

#PI3Ka + PIP3 => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir12')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_p3

#PI3Ka + PIP3c => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir13')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Ka_to_p3c


#PI3Kac to other voxels
#PI3Kac + Vacant => ANIOc + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir14')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_v

#PI3Kac + ANIO => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir15')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_a

#PI3Kac + ANIOc => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir16')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_ac

#PI3Kac + PIP2 => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir17')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_p2

#PI3Kac + PIP2c => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir18')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_p2c

#PI3Kac + PIP3 => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir19')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_p3

#PI3Kac + PIP3c => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir20')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kac_to_p3c


#PI3Kp2 to other voxels
#PI3Kp2 + Vacant => PIP2 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir21')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_v

#PI3Kp2 + ANIO => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir22')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_a

#PI3Kp2 + ANIOc => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir23')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_ac

#PI3Kp2 + PIP2 => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir24')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p2

#PI3Kp2 + PIP2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir25')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p2c

#PI3Kp2 + PIP3 => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir26')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p3

#PI3Kp2 + PIP3c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir27')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p3c


#PI3Kp2c to other voxels
#PI3Kp2c + Vacant => PIP2c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir28')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2c_to_v

#PI3Kp2c + ANIO => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir29')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2c_to_a

#PI3Kp2c + ANIOc => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir30')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_ac

#PI3Kp2c + PIP2 => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir31')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p2

#PI3Kp2c + PIP2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir32')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p2c

#PI3Kp2c + PIP3 => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir33')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p3

#PI3Kp2c + PIP3c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir34')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp2_to_p3c


#PI3Kp3 to other voxels
#PI3Kp3 + Vacant => PIP3 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir35')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_v

#PI3Kp3 + ANIO => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir36')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_a

#PI3Kp3 + ANIOc => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir37')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_ac

#PI3Kp3 + PIP2 => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir38')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_p2

#PI3Kp3 + PIP2c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir39')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_p2c

#PI3Kp3 + PIP3 => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir40')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_p3

#PI3Kp3 + PIP3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir41')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_p3c


#PI3Kp3c to other voxels
#PI3Kp3c + Vacant => PIP3c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir42')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_v

#PI3Kp3c + ANIO => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir43')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_a

#PI3Kp3c + ANIOc => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir44')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_ac

#PI3Kp3c + PIP2 => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir45')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_p2

#PI3Kp3c + PIP2c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir46')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_p2c

#PI3Kp3c + PIP3 => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir47')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3c_to_p3

#PI3Kp3c + PIP3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir48')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = PI3Kp3_to_p3c
#-------------------------------------------------------------------------------


#Deoligomerization--------------------------------------------------------------
#ANIOc => ANIO
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d1')
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_ANIOc

#PIP2c => PIP2
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d2')
react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PIP2c

#PIP3c => PIP3
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d3')
react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PIP3c

#PTENac => PTENa
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d4')
react.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PTENac

#PTENp2c => PTENp2
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d5')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PTENp2c

#PTENp3c => PTENp3
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d6')
react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PTENp3c

#PI3Kac => PI3Ka
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d7')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Ka', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PI3Kac

#PI3Kp2c => PI3Kp2
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d8')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PI3Kp2c

#PI3Kp3c => PI3Kp3
react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d9')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
react.Deoligomerize = isDeoligomerize
react.SearchVacant = 1
react.k = Deoligomerize_PI3Kp3c
#-------------------------------------------------------------------------------
run(duration+0.1)
