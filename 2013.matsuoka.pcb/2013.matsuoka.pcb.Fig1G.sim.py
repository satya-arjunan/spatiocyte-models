sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.5e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-7
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 3

# Create the surface compartment:
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')

theSimulator.createEntity('Variable', 'Variable:/Surface:MinD').Value = 1

#logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#logger.VariableReferenceList = [['_', 'Variable:/:Vacant']]
#logger.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
#logger.LogInterval = 1e-2;
#logger.MultiscaleStructure = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenMinD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
diffuser.D = 7.2e-14
diffuser.Origins = 1

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
iterator.Iterations = 1
iterator.LogEnd = 7
iterator.LogStart = 2.033
iterator.LogInterval = 33e-3
iterator.FrameDisplacement = 1
iterator.FileName = "2013.matsuoka.pcb.Fig1G.sim.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
fil.Length = 1e-7
fil.Width = 1e-7
fil.Autofit = 1
#fil.Filaments = 4
fil.SubunitRadius = 0.4e-9
fil.SubunitAngle = 0
fil.DiffuseRadius = 0.4e-9
fil.LipidRadius = 0.4e-9
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


