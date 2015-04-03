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
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTENc').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PTEN').Value = 300
theSimulator.createEntity('Variable', 'Variable:/Surface:PIP2c').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTENc']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PTEN']]
logger.LogInterval = 1e-3

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

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = 1


binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction5')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction6')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = 1


binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction7')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction8')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTEN','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.ForcedSequence = 1
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction9')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = 0.01

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction10')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = 0.01

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction11')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c','1']]
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction12')
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENp','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:PTENc','1']]
binder.p = 1

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:reaction13')
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2c', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PIP2', '1']]
react.Deoligomerize = 6
react.Rates = [8, 5, 2, 1, 0.1, 0.01]

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:reaction14')
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENc', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PTENp', '1']]
react.Deoligomerize = 6
react.Rates = [8, 5, 2, 1, 0.1, 0.01]

run(100)
