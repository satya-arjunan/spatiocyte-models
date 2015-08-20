#Simulation
LogTime = 0.5
RunTime = 0.51

import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 10e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 7e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 7e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 2e-8
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 14140
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 0

a = theSimulator.createEntity('Variable', 'Variable:/:Bh')
a.Name = 'HD'
a.Value = 980

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:snrp1')
react.VariableReferenceList = [['_', 'Variable:/:Bh', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:B', '1']]
react.SearchVacant = 1
react.k = 1e-4

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:snrp2')
react.VariableReferenceList = [['_', 'Variable:/:B', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Bh', '1']]
react.k = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:B']]
logger.LogInterval = 1e-1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:B']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 0

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.Origins = 1
diffuser.D = 0.69e-12

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:A','1']]
binder.VariableReferenceList = [['_', 'Variable:/:Bh','1']]
binder.p = 1

life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
life.VariableReferenceList = [['_', 'Variable:/:B']]
life.Iterations = 1
life.LogEnd = LogTime
life.FileName = "dirp.csv"
life.Verbose = 1

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:A']]
fil.VariableReferenceList = [['_', 'Variable:/:B']]
fil.Periodic = 1

run(RunTime)
