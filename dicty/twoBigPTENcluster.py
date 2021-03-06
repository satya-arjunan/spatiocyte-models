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
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2').Value = 1000 
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTEN').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PI3K').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PI3Kp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PI3Kp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PI3Kp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PI3Kp3c').Value = 0

a = theSimulator.createEntity('Variable', 'Variable:/Surface:PI3Kh')
a.Name = 'HD'
a.Value = 1000

a = theSimulator.createEntity('Variable', 'Variable:/Surface:PTENh')
a.Name = 'HD'
a.Value = 1000



logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3K']]
logger.LogInterval = 1e-1

logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENh']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:PI3K']]
logger.LogInterval = 1e-1
logger.LogEnd = 999

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PI3K']]

#Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PIP3']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PI3K']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13
#-------------------------------------------------------------------------------

#Abbreviations
#c = cluster
#p2 = PIP2
#p3 = PIP3
#v = VACANT

#Reaction-driven diffusion probabilities
v_to_p2 = 1.0
v_to_p3 = 1.0
p2_to_v = 0.08
p2_to_p2 = 1.0
p2_to_p3 = 1.0
p3_to_v = 0.08
p3_to_p2 = 1.0
p3_to_p3 = 1.0

#Reaction probabilities
NucleateCluster = 0.01
NucleateClusterPTEN = 1
NucleateClusterPI3K = 1
ExtendCluster = 0.01
ExtendClusterPTEN = 1
ExtendClusterPI3K = 1
Deoligomerize = 1e+1
DeoligomerizePTEN = 2e+0
DeoligomerizePI3K = 2e+0
PhosphorylatePIP2 = 1
DephosphorylatePIP3 = 1

#Membrane association reactions------------------------------------------------
a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:a1')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
a.k = 1e-2

a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:a2')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
a.k = 1e-1

a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:a3')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
a.k = 1e-1
#-------------------------------------------------------------------------------

#Membrane dissociation reactions------------------------------------------------
#Enhanced PTEN koff by PIP3
a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d1')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','1']]
a.k = 1

#Enhanced PTEN koff by PIP3
a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d2')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','1']]
a.k = 1

#Highest PTEN koff by neutral VACANT lipids
a = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d3')
a.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
a.VariableReferenceList = [['_', 'Variable:/Surface:PTENh','1']]
a.k = 1
#-------------------------------------------------------------------------------

#Reaction-driven diffusion------------------------------------------------------
#PTEN to other voxels
#PTEN + PIP2 => VACANT + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PTEN + PIP2c => VACANT + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PTEN + PIP3 => VACANT + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3

#PTEN + PIP3c => VACANT + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3


#PTENp2 to other voxels
#PTENp2 + VACANT => PIP2 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2 + PIP2 => PIP2 + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2 + PIP2c => PIP2 + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2 + PIP3 => PIP2 + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r8')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PTENp2 + PIP3c => PIP2 + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r9')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PTENp2c to other voxels
#PTENp2c + VACANT => PIP2c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r10')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2c + PIP2 => PIP2c + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r11')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2c + PIP2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PTENp2c + PIP3 => PIP2c + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r13')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PTENp3c + PIP2c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r14')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PTENp3 to other voxels
#PTENp3 + VACANT => PIP3 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r15')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PTENp3 + PIP2 => PIP3 + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r16')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3 + PIP2c => PIP3 + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r17')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3 + PIP3 => PIP3 + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r18')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PTENp3 + PIP3c => PIP3 + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r19')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3


#PTENp3c to other voxels
#PTENp3c + VACANT => PIP3c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r20')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PTENp3c + PIP2 => PIP3c + PTENp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp2c + PIP3c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r22')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3c + PIP3 => PIP3c + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r23')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PTENp3c + PIP3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r24')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3
#-------------------------------------------------------------------------------

#Reaction-driven diffusion------------------------------------------------------
#PI3K to other voxels
#PI3K + PIP2 => VACANT + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PI3K + PIP2c => VACANT + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PI3K + PIP3 => VACANT + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3

#PI3K + PIP3c => VACANT + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3


#PI3Kp2 to other voxels
#PI3Kp2 + VACANT => PIP2 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri5')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PI3Kp2 + PIP2 => PIP2 + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri6')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2 + PIP2c => PIP2 + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri7')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2 + PIP3 => PIP2 + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri8')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PI3Kp2 + PIP3c => PIP2 + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri9')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PI3Kp2c to other voxels
#PI3Kp2c + VACANT => PIP2c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri10')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PI3Kp2c + PIP2 => PIP2c + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri11')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2c + PIP2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri12')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2c + PIP3 => PIP2c + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri13')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PI3Kp3c + PIP2c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri14')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PI3Kp3 to other voxels
#PI3Kp3 + VACANT => PIP3 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri15')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PI3Kp3 + PIP2 => PIP3 + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri16')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3 + PIP2c => PIP3 + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri17')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3 + PIP3 => PIP3 + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri18')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PI3Kp3 + PIP3c => PIP3 + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri19')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3


#PI3Kp3c to other voxels
#PI3Kp3c + VACANT => PIP3c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri20')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PI3Kp3c + PIP2 => PIP3c + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri21')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp2c + PIP3c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri22')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3c + PIP3 => PIP3c + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri23')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PI3Kp3c + PIP3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri24')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3
#-------------------------------------------------------------------------------

#PIP2c nucleation---------------------------------------------------------------
#PIP2 + PIP2 => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r25')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PIP2 + PTENp2 => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r26')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PIP2 + PI3Kp2 => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri26')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#PTENp2 + PTENp2 => PTENp2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r27')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Kp2 + PI3Kp2 => PI3Kp2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri27')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp2 => PTENp2c + PI3Kp2c
#-------------------------------------------------------------------------------

#PIP3c nucleation---------------------------------------------------------------
#PIP3 + PIP3 => PIP3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r28')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PIP3 + PTENp3 => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r29')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PIP3 + PI3Kp3 => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri29')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#PTENp3 + PTENp3 => PTENp3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r30')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Kp3 + PI3Kp3 => PI3Kp3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri30')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp3 => PTENp3c + PI3Kp3c
#-------------------------------------------------------------------------------

#PIP2c-PIP3c nucleation---------------------------------------------------------
#PIP2 + PIP3 => PIP2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r31')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PIP2 + PTENp3 => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r32')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PIP2 + PI3Kp3 => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri32')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#PTENp2 + PIP3 => PTENp2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r33')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PTENp2 + PTENp3 => PTENp2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r34')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Kp2 + PIP3 => PI3Kp2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri33')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#PI3Kp2 + PI3Kp3 => PI3Kp2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri34')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PI3Kp2 + PTENp3 => PI3Kp2c + PTENp3c
#PTENp2 + PI3Kp3 => PTENp2c + PI3Kp3c
#-------------------------------------------------------------------------------

#PIP2c-PIP2c extension----------------------------------------------------------
#PIP2 + PIP2c => PIP2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r35')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PIP2 + PTENp2c => PIP2c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r36')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp2 + PIP2c => PTENp2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r37')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PIP2 + PI3Kp2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri36')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp2 + PIP2c => PI3Kp2c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri37')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp2c => PTENp2c + PI3Kp2c
#PI3Kp2 + PTENp2c => PI3Kp2c + PTENp2c
#-------------------------------------------------------------------------------

#PIP3c-PIP3c extension----------------------------------------------------------
#PIP3 + PIP3c => PIP3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r38')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PIP3 + PTENp3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r39')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp3 + PIP3c => PTENp3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r40')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PIP3 + PI3Kp3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri39')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp3 + PIP3c => PI3Kp3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri40')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp3c => PTENp3c + PI3Kp3c
#PI3Kp3 + PTENp3c => PI3Kp3c + PTENp3c
#-------------------------------------------------------------------------------

#PIP2c-PIP3c extension----------------------------------------------------------
#PIP2 + PIP3c => PIP2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r41')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PIP2 + PTENp3c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r42')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp2 + PIP3c => PTENp2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r43')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp2 + PTENp3c => PTENp2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r44')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PIP2 + PI3Kp3c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri42')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp2 + PIP3c => PI3Kp2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri43')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp2 + PI3Kp3c => PI3Kp2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri44')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp3c => PTENp2c + PI3Kp3c
#PI3Kp2 + PTENp3c => PI3Kp2c + PTENp3c
#-------------------------------------------------------------------------------

#PIP3c-PIP2c extension----------------------------------------------------------
#PIP3 + PIP2c => PIP3c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r45')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PIP3 + PTENp2c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r46')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp3 + PIP2c => PTENp3c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r47')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PTENp3 + PTENp2c => PTENp3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r48')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PIP3 + PI3Kp2c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri46')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp3 + PIP2c => PI3Kp3c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri47')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#PI3Kp3 + PI3Kp2c => PI3Kp3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ri48')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp2c => PTENp3c + PI3Kp2c
#PI3Kp3 + PTENp2c => PI3Kp3c + PTENp2c
#-------------------------------------------------------------------------------

#Deoligomerization--------------------------------------------------------------
#PIP2c => PIP2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r49')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PIP3c => PIP3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r50')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PTENp2c => PTENp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r51')
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PTENp3c => PTENp3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:r52')
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PI3Kp2c => PI3Kp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:ri51')
react.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePI3K

#PI3Kp3c => PI3Kp3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:ri52')
react.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PI3Kp3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePI3K
#-------------------------------------------------------------------------------


run(1000)
