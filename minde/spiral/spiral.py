import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 100e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 200e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 200e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDm').Value = 50000*4
theSimulator.createEntity('Variable', 'Variable:/:MinEm').Value = 30000*4
theSimulator.createEntity('Variable', 'Variable:/:MinDEm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDEEm').Value = 0
s = theSimulator.createEntity('Variable', 'Variable:/:MinD')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:MinE')
s.Value = 0
s.Name = "HD"

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:MinDm']]
logger.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
logger.LogInterval = 10

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:MinDm']]
populator.VariableReferenceList = [['_', 'Variable:/:MinEm']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDm']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinEm']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
diffuser.D = 1e-13

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/:MinD','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','1']]
binder.k = 5e-8

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.k = 5e-10

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
binder.p = 1

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
binder.p = 1

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinD','1']]
binder.k = 10000

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinE','1']]
binder.k = 0.01


#logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
#logger.VariableReferenceList = [['_', 'Variable:/:sA']]
#logger.LogInterval = 1
#logger.LogEnd = 200
#logger.Iterations = 250
#logger.FileName = "IterateLogXY.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:Membrane')
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinEm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
fil.PlaneXY = 1

run(200001)
