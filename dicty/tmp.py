duration = 1000
LogEvent = 0
LengthX = 4.5e-6
LengthY = 1.35e-6
LengthZ = 0.26e-6

#Initial values
nPTEN_total = 500
nPIP2_total = 350 # 3%
nANIO_total = 1732 # 10%

PTENvol_frac = 0.5
PTENp2_frac = 0.479
PTENa_frac = 0.48

nPTENvol_ss = PTENvol_frac*nPTEN_total
nPIP2_ss = nPIP2_total-PTENp2_frac*(nPTEN_total-nPTENvol_ss)
nANIO_ss = nANIO_total-PTENa_frac*(nPTEN_total-nPTENvol_ss)
Volume = LengthX*LengthY*LengthZ

#Diffusion coefficients
#LipidDiffusion = 0.5e-12
#ProteinDiffusion_a = 0.133e-12
#ProteinDiffusion_p3 = 0.133e-12
#ProteinDiffusion_p2 = 0.035e-12
#ProteinDiffusion_v = 0.693e-12
#ProteinDiffusion_vol = 16e-12

LipidDiffusion = 0
ProteinDiffusion_a = 0
ProteinDiffusion_p3 = 0
ProteinDiffusion_p2 = 0
ProteinDiffusion_v = 0
ProteinDiffusion_vol = 0


sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 10e-9 
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

#s = theSimulator.createEntity('Variable', 'Variable:/:PI3Kvol')
#s.Value = 0
#s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTEN')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PIP2')
s.Value = nPIP2_total
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:PTENp2')
s.Value = 0
s.Name = "HD"

theSimulator.createEntity('Variable', 'Variable:/:ANIO').Value = nANIO_total
theSimulator.createEntity('Variable', 'Variable:/:PTENa').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PIP3').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PI3K').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:ANIOc').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PIP2c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PIP3c').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PTENac').Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:PTENp2c').Value = 0
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
#f.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#f.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#f.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#f.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
#f.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
#f.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#f.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
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
#l.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
##l.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#l.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
##l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
##l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENac']]
##l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#l.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
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
#populator.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#populator.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#populator.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
#populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#populator.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
#populator.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#
##Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIO')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIO']]
diffuser.D = LipidDiffusion
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#diffuser.D = LipidDiffusion
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#diffuser.D = LipidDiffusion
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#diffuser.D = ProteinDiffusion_v
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#diffuser.D = ProteinDiffusion_v
#
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENa')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENa']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion_a
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENac')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_a
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p2
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#diffuser.WalkReact = 1
#diffuser.D = ProteinDiffusion_p2
#
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
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENvol')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
#diffuser.D = ProteinDiffusion_vol
#
#diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kvol')
#diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kvol']]
#diffuser.D = ProteinDiffusion_vol
##-------------------------------------------------------------------------------



r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 6.289/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 0.036
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = 2.896/nPIP2_ss*Volume
r.LogEvent = 1
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 3.995
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = 0.406
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 0.029/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 12.525
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PIP2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = 1.63959/nPIP2_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:ANIO', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 0.48894/nANIO_ss*Volume
r.LogEvent = LogEvent
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = 0.31983
r.LogEvent = LogEvent
r.LogStart = 5

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
l.VariableReferenceList = [['_', 'Variable:/:PIP2']]
l.LogInterval = 5e-1
l.LogEnd = duration
l.Iterations = 1

run(duration+0.1)
