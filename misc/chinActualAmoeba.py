T = 1e+6

sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = 3e-8 
s.SearchVacant = 0

sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 25e-6
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 13e-6
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:XYPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:XZPLANE').Value = 0
sim.createEntity('Variable', 'Variable:/:YZPLANE').Value = 0

sim.createEntity('System', 'System:/:Cell').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Cell:LENGTHX').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHY').Value = 20e-6
sim.createEntity('Variable', 'Variable:/Cell:LENGTHZ').Value = 11e-6
sim.createEntity('Variable', 'Variable:/Cell:VACANT')

sim.createEntity('System', 'System:/Cell:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Cell/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Cell/Surface:VACANT')


PIP2m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2m')
PIP2m.Value = 9623
PIP3m = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3m')
PIP3m.Value = 0
PIP3a = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP3a')
PIP3a.Value = 0
PTENm = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTENm')
PTENm.Value = 2412
PI3Km = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3Km')
PI3Km.Value = 24163

PIP2 = sim.createEntity('Variable', 'Variable:/Cell/Surface:PIP2')
PIP2.Value = 62858
PIP2.Name = "HD"

PI3K = sim.createEntity('Variable', 'Variable:/Cell/Surface:PI3K')
PI3K.Value = 12050
PI3K.Name = "HD"

PTEN = sim.createEntity('Variable', 'Variable:/Cell/Surface:PTEN')
PTEN.Value = 48342
PTEN.Name = "HD"

logger = sim.createEntity('VisualizationLogProcess', 'Process:/Cell/Surface:logger')
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
logger.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
logger.LogInterval = 20 

populator = sim.createEntity('MoleculePopulateProcess', 'Process:/Cell/Surface:pop')
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
populator.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP2')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m']]
diffuser.D = 1.6e-13

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m']]
diffuser.D = 1.6e-13

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePIP3a')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a']]
diffuser.D = 1.6e-13

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePTEN')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm']]
diffuser.D = 1.6e-13

diffuser = sim.createEntity('DiffusionProcess', 'Process:/Cell/Surface:diffusePI3K')
diffuser.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km']]
diffuser.D = 1.6e-13

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPIP2')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
react.k = 6.4e-1

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPTEN')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTEN', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PTENm', '1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '1']]
react.k = 3.2e-13

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:recruitPI3Ka')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '1']]
react.k = 1.6e-12

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:dimerPIP3')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a','1']]
binder.p = 0.65
#binder.k = 1.34546485292521e-13

binder = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Cell/Surface:PIP2toPIP3')
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m','1']]
binder.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km','1']]
binder.p = 0.17
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
react.k = 1.44

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePI3K')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3Km', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PI3K', '1']]
react.k = 0.32

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.32

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP3a')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP3a', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.32

react = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/Cell/Surface:dissociatePIP2')
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2m', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Cell/Surface:PIP2', '1']]
react.k = 0.0016

while getCurrentTime() < T:
  run(2)
  print getCurrentTime(),"PIP2:",PIP2.Value,"PIP2m:",PIP2m.Value,"PIP3m:",PIP3m.Value,"PIP3a:",PIP3a.Value,"PI3K:",PI3K.Value,"PTEN:",PTEN.Value,"PI3Km:",PI3Km.Value,"PTENm:",PTENm.Value
