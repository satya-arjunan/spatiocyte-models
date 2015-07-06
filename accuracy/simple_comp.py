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
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 5000
theSimulator.createEntity('Variable', 'Variable:/:C').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:B']]
logger.VariableReferenceList = [['_', 'Variable:/:C']]
logger.VariableReferenceList = [['_', 'Variable:/:Interface']]
logger.LogInterval = 0.0001

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:popB')
populator.VariableReferenceList = [['_', 'Variable:/:B']]
populator.OriginZ = 1
populator.UniformRadiusZ = 0.05


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 1e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.D = 1e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseC')
diffuser.VariableReferenceList = [['_', 'Variable:/:C']]
diffuser.D = 0


fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/:A']]
fil.VariableReferenceList = [['_', 'Variable:/:C']]
fil.PlaneXY = 1
fil.PlaneXZ = 0
fil.PlaneYZ = 0
#fil.OriginX = -1.1
#fil.OriginY = -0.3
#fil.OriginZ = -0.3
#fil.RotateZ = 0.3
#fil.RotateY = 0.3

#fil.OriginZ = -1.05
#fil.RotateY = 0.3
#fil.OriginY = -1

run(0.05)
