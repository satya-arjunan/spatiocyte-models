
sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 6e-8 
s.SearchVacant = 0
s.RemoveSurfaceBias = 1

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 0

sim.createEntity('System', 'System:/:Cell').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHZ').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:VACANT')

sim.createEntity('System', 'System:/Cell:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Cell/Surface:VACANT')
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2m').Value = 1872
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3m').Value = 0
sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3a').Value = 0
sim.createEntity('Variable', 'Variable:/Cell/Surface:PTENm').Value = 469
sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3Km').Value = 4701

PIP2 = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2')
PIP2.Value = 12229
PIP2.Name = "HD"

PI3K = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3K')
PI3K.Value = 14066
PI3K.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
PTEN.Value = 9404
PTEN.Name = "HD"

logger = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Surface:logger')
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
logger.LogInterval = 20

populator = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Surface:pop')
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
diffuser.D = 1e-14

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
diffuser.D = 1e-14

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3a')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
diffuser.D = 1e-14

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
diffuser.D = 1e-14

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
diffuser.D = 1e-14

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPIP2')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
react.k = 4e-2

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
react.k = 2e-14

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3Ka')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
react.k = 1e-13

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:dimerPIP3')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
binder.p = 0.8
#binder.k = 1.34546485292521e-13

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP2toPIP3')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','1']]
binder.p = 0.15
#binder.k = 7.0378161537626373e-14

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3toPIP2')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','1']]
binder.p = 1
#binder.k = 4.1398918551544924e-13

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP3atoPIP2')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm','1']]
binder.p = 1
#binder.k = 4.1398918551544924e-13  

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePTEN')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '1']]
react.k = 0.09

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePI3K')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '1']]
react.k = 0.02

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.02

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3a')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.02

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP2')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.0001

run(1e+6)
