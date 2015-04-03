sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 10e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 2.5e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 2.5e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4

# Create the surface compartment:
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2').Value = 2000
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTEN').Value = 200
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENc').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENc']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
logger.LogInterval = 1e-1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTENp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTENc')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENc']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
diffuser.D = 1e-13

Vac2PIP = 1.0
PIP2Vac = 0.08
PIP2PIP = 1.0
NucleateCluster = 0.01
NucleateClusterPTEN = 1
ExtendCluster = 0.01
ExtendClusterPTEN = 1



binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = PIP2Vac

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP



binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = PIP2Vac

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP



binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = Vac2PIP

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r8')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = Vac2PIP



binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r9')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = NucleateCluster

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r10')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = NucleateClusterPTEN

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = NucleateClusterPTEN



binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r11')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = ExtendCluster

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r13')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = ExtendClusterPTEN

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r14')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = ExtendClusterPTEN


react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r15')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+1

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r16')
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENc', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 2e+0

run(100)
