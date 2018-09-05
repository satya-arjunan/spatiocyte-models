import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 5e-9
sim.SearchVacant = 0

MinD = 30000.0*16

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 5e-6*4
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 5e-6*4
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 5e-8
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDm').Value = MinD
theSimulator.createEntity('Variable', 'Variable:/:MinEm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDEm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDEEm').Value = 0
s = theSimulator.createEntity('Variable', 'Variable:/:MinD')
s.Value = 0
s.Name = "HD"

s = theSimulator.createEntity('Variable', 'Variable:/:MinE')
s.Value = MinD*10
s.Name = "HD"

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:MinDm']]
logger.VariableReferenceList = [['_', 'Variable:/:MinEm']]
logger.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
logger.LogInterval = 0.1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:MinDm']]
populator.VariableReferenceList = [['_', 'Variable:/:MinEm']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDm']]
diffuser.D = 2.25e-15

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinEm']]
diffuser.D = 9e-15

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
diffuser.D = 2.25e-15

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEEm')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
diffuser.D = 2.25e-15


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
binder.p = 0.5 #0.36

# kde
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
binder.p = 0.5 #0.36

# kdE
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
binder.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
binder.k = 2.5e-25

# kdE
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r5')
binder.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
binder.k = 2.5e-25

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r6')
binder.VariableReferenceList = [['_', 'Variable:/:MinDEEm','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinD','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
binder.k = 10000000

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
