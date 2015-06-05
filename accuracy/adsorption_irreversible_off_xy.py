import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 100e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 20e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 20e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 20e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 1000
theSimulator.createEntity('Variable', 'Variable:/:sA').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:sA']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:sA']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 1e-12

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:sA']]
fil.PlaneXY = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:sA','1']]
binder.p = 0.6

logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
logger.VariableReferenceList = [['_', 'Variable:/:sA']]
logger.LogInterval = 1
logger.LogEnd = 20
logger.Iterations = 1
logger.FileName = "IterateLogOffXY.csv"

run(21)
