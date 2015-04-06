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
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2').Value = 2000
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTEN').Value = 200
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp2c').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
logger.LogInterval = 1e-1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
diffuser.D = 1e-13

#Reaction-driven diffusion probabilities
Vac2PIP = 1.0
PIP2Vac = 0.08
PIP2PIP = 1.0

#Reaction probabilities
NucleateCluster = 0.01
NucleateClusterPTEN = 1
ExtendCluster = 0.01
ExtendClusterPTEN = 1


#Reaction-driven diffusion--------------------------------------------------------------
#PTEN to other voxels
#PTEN + PIP2 => VACANT + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = Vac2PIP

#PTEN + PIP2c => VACANT + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r8')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = Vac2PIP


#PTENp2 to other voxels
#PTENp2 + VACANT => PIP2 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = PIP2Vac

#PTENp2 + PIP2 => PIP2 + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP

#PTENp2 + PIP2c => PIP2 + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP


#PTENp2c to other voxels
#PTENp2c + VACANT => PIP2c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = PIP2Vac

#PTENp2c + PIP2 => PIP2c + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP

#PTENp2c + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = PIP2PIP
#---------------------------------------------------------------------------------------


#PIP2c nucleation-----------------------------------------------------------------------
#PIP2 + PIP2 => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r9')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = NucleateCluster

#PTENp2 + PTENp2 => PTENp2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r10')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.p = NucleateClusterPTEN

#PIP2 + PTENp2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.p = NucleateClusterPTEN
#---------------------------------------------------------------------------------------


#PIP2c extension------------------------------------------------------------------------
#PIP2 + PIP2c => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r11')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = ExtendCluster

#PIP2 + PTENp2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r14')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.p = ExtendClusterPTEN

#PTENp2 + PIP2c => PTENp2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r13')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.p = ExtendClusterPTEN
#---------------------------------------------------------------------------------------

#Deoligomerization----------------------------------------------------------------------
#PIP2c -> PIP2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r15')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+1

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r16')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+1

#PTENp2c -> PTENp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r16')
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 2e+0
#---------------------------------------------------------------------------------------

run(100)
