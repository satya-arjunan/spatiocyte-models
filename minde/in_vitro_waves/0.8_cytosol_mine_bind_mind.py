import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 100e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDm').Value = 40000
theSimulator.createEntity('Variable', 'Variable:/:MinEm').Value = 26700
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
logger.LogInterval = 1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:MinDm']]
populator.VariableReferenceList = [['_', 'Variable:/:MinEm']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDm']]
diffuser.D = 9e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinEm']]
diffuser.D = 3.6e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
diffuser.D = 9e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
diffuser.D = 9e-13


#Reactions
# kD
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1')
binder.VariableReferenceList = [['_', 'Variable:/:MinD','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','1']]
binder.k = 0.25e-4

# kde
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
binder.p = 1 #0.36

# kde
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
binder.p = 1 #0.36

# kdE
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
binder.k = 0.0051e-25

# kdE
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
binder.k = 0.0051e-25

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinD','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.k = 100000

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r7')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinE','1']]
binder.k = 0.3


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
