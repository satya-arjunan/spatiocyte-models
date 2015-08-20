import math
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.5e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

theSimulator.createEntity('Variable', 'Variable:/:PTEN').Value = 1

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
logger.VariableReferenceList = [['_', 'Variable:/:PTEN']]
logger.LogInterval = 1e-2;

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:PTEN']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffA')
diffuser.VariableReferenceList = [['_', 'Variable:/:PTEN']]
diffuser.D = 7.2e-14
diffuser.Origins = 1

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/:PTEN']]
iterator.Iterations = 1
iterator.LogEnd = 7
iterator.LogStart = 2.033
iterator.LogInterval = 33e-3
iterator.FrameDisplacement = 1
iterator.FileName = "2013.matsuoka.pcb.Fig1G.sim.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:PTEN']]
fil.PlaneYZ = 1
fil.RotateY = math.pi/3
fil.RotateX = math.pi/3
fil.RotateZ = math.pi/3
fil.SubunitRadius = 0.4e-9
fil.DiffuseRadius = 0.4e-9
fil.Periodic = 1
fil.RegularLattice = 1

import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(8)
end = time.time()
duration = end-start
print duration


