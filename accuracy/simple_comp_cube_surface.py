import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 10e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 2e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 3e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5


theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')

theSimulator.createEntity('Variable', 'Variable:/Surface:A').Value = 10
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 5000

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:VACANT']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:A']]
logger.VariableReferenceList = [['_', 'Variable:/:B']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:A']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:popB')
populator.VariableReferenceList = [['_', 'Variable:/:B']]
populator.OriginZ = 1
populator.UniformRadiusZ = 0.05


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:A']]
diffuser.D = 1e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.D = 1e-12

run(0.05)
