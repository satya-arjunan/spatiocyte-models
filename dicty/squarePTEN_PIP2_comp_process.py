#Abbreviations
#c = cluster
#p2 = PIP2
#v = Vacant

#Reaction-driven diffusion probabilities
v_to_p2 = 1.0
p2_to_v = 0.08
p2_to_p2 = 1.0

#Reaction probabilities
NucleateCluster = 0.01
NucleateClusterPTEN = 1
ExtendCluster = 0.01
ExtendClusterPTEN = 1

#1st Order reaction rates
Deoligomerize = 1e+1
DeoligomerizePTEN = 2e+0

#Diffusion coefficients
LipidDiffusion = 1e-13
ProteinDiffusion = 1e-13


sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 10e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 2.5e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 2.5e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 2e-8
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0

theSimulator.createEntity('Variable', 'Variable:/:PIP2').Value = 2000
theSimulator.createEntity('Variable', 'Variable:/:PTEN').Value = 200
theSimulator.createEntity('Variable', 'Variable:/:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2c').Value = 0

#a = theSimulator.createEntity('Variable', 'Variable:/:PI3Kh')
#a.Name = 'HD'
#a.Value = 0

#a = theSimulator.createEntity('Variable', 'Variable:/:PTENh')
#a.Name = 'HD'
#a.Value = 0

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:Surface')
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP2']]
fil.VariableReferenceList = [['_', 'Variable:/:PTEN']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
fil.Periodic = 1

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
logger.LogInterval = 1e-1

logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
logger.VariableReferenceList = [['_', 'Variable:/:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
logger.LogInterval = 1e-1
logger.LogEnd = 9
logger.Iterations = 1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]

#Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
diffuser.D = LipidDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = ProteinDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = ProteinDiffusion
#-------------------------------------------------------------------------------

#Reaction-driven diffusion------------------------------------------------------
#PTEN to other voxels
#PTEN + PIP2 => Vacant + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PTEN + PIP2c => Vacant + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PTENp2 to other voxels
#PTENp2 + Vacant => PIP2 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2 + PIP2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r24')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2 + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r25')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2c to other voxels
#PTENp2c + Vacant => PIP2c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r28')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2c + PIP2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r31')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2c + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2
#-------------------------------------------------------------------------------

#PIP2c nucleation---------------------------------------------------------------
#PIP2 + PIP2 => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENp2 + PTENp2 => PTENp2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN
#-------------------------------------------------------------------------------

#PIP2-PIP2c extension----------------------------------------------------------
#PIP2 + PIP2c => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p2_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp2 + PTENp2c => PTENp2c + PTENp2c 
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p2_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN
#-------------------------------------------------------------------------------

#Deoligomerization--------------------------------------------------------------
#PIP2c => PIP2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d2')
react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PTENp2c => PTENp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d5')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN
#-------------------------------------------------------------------------------


import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(100)
end = time.time()
duration = end-start
print duration







