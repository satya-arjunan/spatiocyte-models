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
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 10
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 1000
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:B']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:B']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 1e-12

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/:A']]

run(1)
