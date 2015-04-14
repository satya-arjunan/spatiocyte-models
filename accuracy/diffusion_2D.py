import math
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.5e-9

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

theSimulator.createEntity('Variable', 'Variable:/:A').Value = 1

#logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
#logger.VariableReferenceList = [['_', 'Variable:/:A']]
#logger.LogInterval = 1e-2;

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 7.2e-14
diffuser.Origins = 1

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/:A']]
iterator.Iterations = 10000
iterator.LogEnd = 20
iterator.LogInterval = 1
iterator.Diffusion = 1
iterator.FileName = "diffusion_2D.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/:A']]
fil.Periodic = 1
fil.RegularLattice = 1

run(21)


