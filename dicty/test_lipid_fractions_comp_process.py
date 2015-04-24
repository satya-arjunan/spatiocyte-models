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

theSimulator.createEntity('Variable', 'Variable:/:ANIO').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PIP2').Value = 2100
theSimulator.createEntity('Variable', 'Variable:/:PIP3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTEN').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3K').Value = 200
theSimulator.createEntity('Variable', 'Variable:/:ANIOc').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PIP2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PIP3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENa').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENac').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PTENp3c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Ka').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kac').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp2c').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:PI3Kp3c').Value = 0

#a = theSimulator.createEntity('Variable', 'Variable:/:PI3Kh')
#a.Name = 'HD'
#a.Value = 0

#a = theSimulator.createEntity('Variable', 'Variable:/:PTENh')
#a.Name = 'HD'
#a.Value = 0

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:Surface')
fil.VariableReferenceList = [['_', 'Variable:/:ANIO']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP2']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP3']]
fil.VariableReferenceList = [['_', 'Variable:/:PTEN']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3K']]
fil.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
fil.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENa']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENac']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
fil.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
fil.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
fil.Filaments = 142
fil.Subunits = 123
fil.Periodic = 1

#logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#logger.VariableReferenceList = [['_', 'Variable:/:ANIO']]
#logger.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENa']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENac']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#logger.LogInterval = 1e-1

logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
logger.VariableReferenceList = [['_', 'Variable:/:ANIO']]
logger.VariableReferenceList = [['_', 'Variable:/:ANIOc']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP3']]
logger.VariableReferenceList = [['_', 'Variable:/:PIP3c']]
logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENa']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENac']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
logger.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
logger.VariableReferenceList = [['_', 'Variable:/:PI3K']]
#logger.VariableReferenceList = [['_', 'Variable:/:PTENh']]
#logger.VariableReferenceList = [['_', 'Variable:/:PI3Kh']]
logger.LogInterval = 1e-4
logger.LogEnd = 9
logger.Iterations = 50

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:ANIO']]
populator.VariableReferenceList = [['_', 'Variable:/:PIP2']]
populator.VariableReferenceList = [['_', 'Variable:/:PIP3']]
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
populator.VariableReferenceList = [['_', 'Variable:/:PI3K']]

#Diffusion----------------------------------------------------------------------
diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dANIO')
diffuser.VariableReferenceList = [['_', 'Variable:/:ANIO']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP2']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PIP3']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3K']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENa')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENa']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENac']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp2c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPTENp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTENp3c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Ka')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Ka']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kac')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kac']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp2c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3']]
diffuser.WalkReact = 1
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:dPI3Kp3c')
diffuser.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c']]
diffuser.WalkReact = 1
diffuser.D = 1e-13
#-------------------------------------------------------------------------------

#Abbreviations
#c = cluster
#p2 = PIP2
#p3 = PIP3
#a = ANIO (eg. PS)
#v = Vacant

#Reaction-driven diffusion probabilities
v_to_a = 1.0
v_to_p2 = 1.0
v_to_p3 = 1.0
a_to_v = 0.08
a_to_a = 1.0
a_to_p2 = 1.0
a_to_p3 = 1.0
p2_to_v = 0.08
p2_to_a = 1.0
p2_to_p2 = 1.0
p2_to_p3 = 1.0
p3_to_v = 0.08
p3_to_a = 1.0
p3_to_p2 = 1.0
p3_to_p3 = 1.0

#Reaction probabilities
NucleateCluster = 0.01
NucleateClusterPTEN = 1
NucleateClusterPI3K = 1
ExtendCluster = 0.01
ExtendClusterPTEN = 1
ExtendClusterPI3K = 1

#1st Order reaction rates
Deoligomerize = 0.9168e+1
DeoligomerizePTEN = 1.8337e+0
DeoligomerizePI3K = 1.8337e+0

#Reaction-driven diffusion------------------------------------------------------
#PTEN to other voxels
#PTEN + ANIO => Vacant + PTENa
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','1']]
binder.ForcedSequence = 1
binder.p = v_to_a

#PTEN + ANIOc => Vacant + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = v_to_a

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

#PTEN + PIP3 => Vacant + PTENp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3

#PTEN + PIP3c => Vacant + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3


#PTENa to other voxels
#PTENa + Vacant => ANIO + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = a_to_v

#PTENa + ANIO => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r8')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PTENa + ANIOc => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r9')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PTENa + PIP2 => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r10')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PTENa + PIP2c => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r11')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PTENa + PIP3 => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r12')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3

#PTENa + PIP3c => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r13')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3


#PTENac to other voxels
#PTENac + Vacant => ANIOc + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r14')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = a_to_v

#PTENac + ANIO => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r15')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PTENac + ANIOc => ANIOc + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r16')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PTENac + PIP2 => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r17')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PTENac + PIP2c => ANIOc + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r18')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PTENac + PIP3 => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r19')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3

#PTENac + PIP3c => ANIOc + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r20')
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3


#PTENp2 to other voxels
#PTENp2 + Vacant => PIP2 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r21')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2 + ANIO => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r22')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PTENp2 + ANIOc => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r23')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

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

#PTENp2 + PIP3 => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r26')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PTENp2 + PIP3c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r27')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PTENp2c to other voxels
#PTENp2c + Vacant => PIP2c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r28')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PTENp2c + ANIO => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r29')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PTENp2c + ANIOc => PIP2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r30')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

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

#PTENp2c + PIP3 => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r33')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PTENp2c + PIP3c => PIP2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r34')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PTENp3 to other voxels
#PTENp3 + Vacant => PIP3 + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r35')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PTENp3 + ANIO => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r36')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PTENp3 + ANIOc => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r37')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PTENp3 + PIP2 => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r38')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3 + PIP2c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r39')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3 + PIP3 => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r40')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PTENp3 + PIP3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r41')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3


#PTENp3c to other voxels
#PTENp3c + Vacant => PIP3c + PTEN
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r42')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTEN','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PTENp3c + ANIO => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r43')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PTENp3c + ANIOc => PIP3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r44')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PTENp3c + PIP2 => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r45')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3c + PIP2c => PIP3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r46')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PTENp3c + PIP3 => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r47')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PTENp3c + PIP3c => PIP3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r48')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3
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
binder.p = v_to_a

#PI3K + ANIOc => Vacant + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir2')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = v_to_a

#PI3K + PIP2 => Vacant + PI3Kp2
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PI3K + PIP2c => Vacant + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir4')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p2

#PI3K + PIP3 => Vacant + PI3Kp3
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir5')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3

#PI3K + PIP3c => Vacant + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir6')
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = v_to_p3


#PI3Ka to other voxels
#PI3Ka + Vacant => ANIO + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir7')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = a_to_v

#PI3Ka + ANIO => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir8')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PI3Ka + ANIOc => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir9')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PI3Ka + PIP2 => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir10')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PI3Ka + PIP2c => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir11')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PI3Ka + PIP3 => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir12')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3

#PI3Ka + PIP3c => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir13')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3


#PI3Kac to other voxels
#PI3Kac + Vacant => ANIOc + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir14')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = a_to_v

#PI3Kac + ANIO => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir15')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PI3Kac + ANIOc => ANIOc + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir16')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = a_to_a

#PI3Kac + PIP2 => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir17')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PI3Kac + PIP2c => ANIOc + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir18')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p2

#PI3Kac + PIP3 => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir19')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3

#PI3Kac + PIP3c => ANIOc + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir20')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = a_to_p3


#PI3Kp2 to other voxels
#PI3Kp2 + Vacant => PIP2 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir21')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PI3Kp2 + ANIO => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir22')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PI3Kp2 + ANIOc => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir23')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PI3Kp2 + PIP2 => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir24')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2 + PIP2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir25')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2 + PIP3 => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir26')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PI3Kp2 + PIP3c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir27')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PI3Kp2c to other voxels
#PI3Kp2c + Vacant => PIP2c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir28')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p2_to_v

#PI3Kp2c + ANIO => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir29')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PI3Kp2c + ANIOc => PIP2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir30')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p2_to_a

#PI3Kp2c + PIP2 => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir31')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2c + PIP2c => PIP2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir32')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p2

#PI3Kp2c + PIP3 => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir33')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3

#PI3Kp2c + PIP3c => PIP2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir34')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p2_to_p3


#PI3Kp3 to other voxels
#PI3Kp3 + Vacant => PIP3 + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir35')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PI3Kp3 + ANIO => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir36')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PI3Kp3 + ANIOc => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir37')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PI3Kp3 + PIP2 => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir38')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3 + PIP2c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir39')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3 + PIP3 => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir40')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PI3Kp3 + PIP3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir41')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3


#PI3Kp3c to other voxels
#PI3Kp3c + Vacant => PIP3c + PI3K
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir42')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3K','1']]
binder.ForcedSequence = 1
binder.p = p3_to_v

#PI3Kp3c + ANIO => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir43')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PI3Kp3c + ANIOc => PIP3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir44')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = p3_to_a

#PI3Kp3c + PIP2 => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir45')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3c + PIP2c => PIP3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir46')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p2

#PI3Kp3c + PIP3 => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir47')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3

#PI3Kp3c + PIP3c => PIP3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ir48')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = p3_to_p3
#-------------------------------------------------------------------------------



#ANIOc nucleation---------------------------------------------------------------
#ANIO + ANIO => ANIOc + ANIOc
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:na_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENa + PTENa => PTENac + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:na_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Ka + PI3Ka => PI3Kac + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:na_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PTENa + PI3Ka => PTENac + PI3Kac
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

#PI3Kp2 + PI3Kp2 => PI3Kp2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp2 => PTENp2c + PI3Kp2c
#-------------------------------------------------------------------------------

#PIP3c nucleation---------------------------------------------------------------
#PIP3 + PIP3 => PIP3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np3_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENp3 + PTENp3 => PTENp3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Kp3 + PI3Kp3 => PI3Kp3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp3 => PTENp3c + PI3Kp3c
#-------------------------------------------------------------------------------

#ANIOc-PIP2c nucleation---------------------------------------------------------
#ANIO + PIP2 => ANIOc + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap2_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENa + PTENp2 => PTENac + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap2_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Ka + PI3Kp2 => PI3Kac + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap2_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PI3Ka + PTENp2 => PI3Kac + PTENp2c
#PTENa + PI3Kp2 => PTENac + PI3Kp2c
#-------------------------------------------------------------------------------

#ANIOc-PIP3c nucleation---------------------------------------------------------
#ANIO + PIP3 => ANIOc + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap3_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENa + PTENp3 => PTENac + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Ka + PI3Kp3 => PI3Kac + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:nap3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PI3Ka + PTENp3 => PI3Kac + PTENp3c
#PTENa + PI3Kp3 => PTENac + PI3Kp3c
#-------------------------------------------------------------------------------

#PIP2c-PIP3c nucleation---------------------------------------------------------
#PIP2 + PIP3 => PIP2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2p3_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateCluster

#PTENp2 + PTENp3 => PTENp2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2p3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPTEN

#PI3Kp2 + PI3Kp3 => PI3Kp2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:np2p3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = NucleateClusterPI3K

#Not implemented:
#PI3Kp2 + PTENp3 => PI3Kp2c + PTENp3c
#PTENp2 + PI3Kp3 => PTENp2c + PI3Kp3c
#-------------------------------------------------------------------------------


#ANIO-ANIOc extension----------------------------------------------------------
#ANIO + ANIOc => ANIOc + ANIOc
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eaa_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENa + PTENac => PTENac + PTENac 
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eaa_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Ka + PI3Kac => PI3Kac + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eaa_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENa + PI3Kac => PTENac + PI3Kac
#PI3Ka + PTENac => PI3Kac + PTENac
#-------------------------------------------------------------------------------

#ANIO-PIP2c extension----------------------------------------------------------
#ANIO + PIP2c => ANIOc + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap2_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENa + PTENp2c => PTENac + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap2_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Ka + PI3Kp2c => PI3Kac + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap2_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENa + PI3Kp2c => PTENac + PI3Kp2c
#PI3Ka + PTENp2c => PI3Kac + PTENp2c
#-------------------------------------------------------------------------------

#ANIO-PIP3c extension----------------------------------------------------------
#ANIO + PIP3c => ANIOc + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap3_1')
binder.VariableReferenceList = [['_', 'Variable:/:ANIO','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENa + PTENp3c => PTENac + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENa','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Ka + PI3Kp3c => PI3Kac + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:eap3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Ka','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENa + PI3Kp3c => PTENac + PI3Kp3c
#PI3Ka + PTENp3c => PI3Kac + PTENp3c
#-------------------------------------------------------------------------------


#PIP2-ANIOc extension----------------------------------------------------------
#PIP2 + ANIOc => PIP2c + ANIOc
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2a_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp2 + PTENac => PTENp2c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2a_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Kp2 + PI3Kac => PI3Kp2c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2a_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp2 + PI3Kac => PTENp2c + PI3Kac
#PI3Kp2 + PTENac => PI3Kp2c + PTENac
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

#PI3Kp2 + PI3Kp2c => PI3Kp2c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p2_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp2c => PTENp2c + PI3Kp2c
#PI3Kp2 + PTENp2c => PI3Kp2c + PTENp2c
#-------------------------------------------------------------------------------

#PIP2-PIP3c extension----------------------------------------------------------
#PIP2 + PIP3c => PIP2c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p3_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp2 + PTENp3c => PTENp2c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Kp2 + PI3Kp3c => PI3Kp2c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep2p3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp2 + PI3Kp3c => PTENp2c + PI3Kp3c
#PI3Kp2 + PTENp3c => PI3Kp2c + PTENp3c
#-------------------------------------------------------------------------------


#PIP3-ANIOc extension----------------------------------------------------------
#PIP3 + ANIOc => PIP3c + ANIOc
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3a_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:ANIOc','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp3 + PTENac => PTENp3c + PTENac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3a_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Kp3 + PI3Kac => PI3Kp3c + PI3Kac
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3a_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kac','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp3 + PI3Kac => PTENp3c + PI3Kac
#PI3Kp3 + PTENac => PI3Kp3c + PTENac
#-------------------------------------------------------------------------------

#PIP3-PIP2c extension----------------------------------------------------------
#PIP3 + PIP2c => PIP3c + PIP2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p2_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp3 + PTENp2c => PTENp3c + PTENp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p2_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Kp3 + PI3Kp2c => PI3Kp3c + PI3Kp2c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p2_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp2c => PTENp3c + PI3Kp2c
#PI3Kp3 + PTENp2c => PI3Kp3c + PTENp2c
#-------------------------------------------------------------------------------

#PIP3-PIP3c extension----------------------------------------------------------
#PIP3 + PIP3c => PIP3c + PIP3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p3_1')
binder.VariableReferenceList = [['_', 'Variable:/:PIP3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PIP3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendCluster

#PTENp3 + PTENp3c => PTENp3c + PTENp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p3_2')
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PTENp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPTEN

#PI3Kp3 + PI3Kp3c => PI3Kp3c + PI3Kp3c
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:ep3p3_3')
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c','1']]
binder.ForcedSequence = 1
binder.p = ExtendClusterPI3K

#Not implemented:
#PTENp3 + PI3Kp3c => PTENp3c + PI3Kp3c
#PI3Kp3 + PTENp3c => PI3Kp3c + PTENp3c
#-------------------------------------------------------------------------------



#Deoligomerization--------------------------------------------------------------
#ANIOc => ANIO
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d1')
react.VariableReferenceList = [['_', 'Variable:/:ANIOc', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:ANIO', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PIP2c => PIP2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d2')
react.VariableReferenceList = [['_', 'Variable:/:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PIP3c => PIP3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d3')
react.VariableReferenceList = [['_', 'Variable:/:PIP3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PIP3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = Deoligomerize

#PTENac => PTENa
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d4')
react.VariableReferenceList = [['_', 'Variable:/:PTENac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PTENp2c => PTENp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d5')
react.VariableReferenceList = [['_', 'Variable:/:PTENp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PTENp3c => PTENp3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d6')
react.VariableReferenceList = [['_', 'Variable:/:PTENp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PTENp3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePTEN

#PI3Kac => PI3Ka
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d7')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kac', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Ka', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePI3K

#PI3Kp2c => PI3Kp2
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d8')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp2', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePI3K

#PI3Kp3c => PI3Kp3
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:d9')
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:PI3Kp3', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = DeoligomerizePI3K
#-------------------------------------------------------------------------------


run(10)






