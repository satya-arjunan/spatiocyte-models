import math

sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 200e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 5

# Create the surface compartment:
s = theSimulator.createEntity('Variable', 'Variable:/:sA')
s.Value = 0
#s.Name = "HD"
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 10000

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:sA']]
logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
logger.LogInterval = 0.01

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:sA']]

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:Vacant','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:sA','1']]
binder.p = 1

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 1e-12

logger = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
logger.VariableReferenceList = [['_', 'Variable:/:sA']]
logger.LogInterval = 1
logger.LogEnd = 2
logger.Iterations = 1
logger.FileName = "IterateLogYZoff.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:sA']]
fil.OriginX = -1
fil.OriginY = 0
fil.OriginZ = 0
fil.RotateX = 0
fil.RotateY = 0
fil.RotateZ = 0
fil.Length = 100e-6
fil.Width = 100e-6
fil.Autofit = 0
fil.SubunitRadius = 200e-9
fil.SubunitAngle = 0
fil.DiffuseRadius = 200e-9
fil.Periodic = 1
fil.RegularLattice = 1


run(10)
