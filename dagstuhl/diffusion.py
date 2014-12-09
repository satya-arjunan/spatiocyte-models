sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 0.5e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 50e-9
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 50e-9
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 50e-9
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 1
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 1
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 1

theSimulator.createEntity('Variable', 'Variable:/:A').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:C').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:D').Value = N
theSimulator.createEntity('Variable', 'Variable:/:T').Value = 100

#logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#logger.VariableReferenceList = [['_', 'Variable:/:A'], ['_', 'Variable:/:B'], ['_', 'Variable:/:C'], ['_', 'Variable:/:D']]
#logger.LogInterval = 0.01

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:B']]
populator.VariableReferenceList = [['_', 'Variable:/:D']]
populator.VariableReferenceList = [['_', 'Variable:/:T']]

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:C','1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','1']]
#binder.k = 8.48e-20
binder.p = 1

diffuser = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/:diffuseT')
diffuser.VariableReferenceList = [['_', 'Variable:/:T']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/:diffuseC')
diffuser.VariableReferenceList = [['_', 'Variable:/:C']]
diffuser.D = 10e-12

#log = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
#log.VariableReferenceList = [['_', 'Variable:/:A']]
#log.Iterations = 1000
#log.LogEnd = 0.0001
#log.LogInterval = 1e-6
#log.FileName = "log%dk.csv" %(N)

log = theSimulator.createEntity('IteratingLogProcess', 'Process:/:msd')
log.VariableReferenceList = [['_', 'Variable:/:T']]
log.Iterations = 1
log.LogEnd = 0.1
log.LogInterval = 1e-6
log.Diffusion = 1
log.FileName = "log%dmsd.csv" %(N)

#life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
#life.VariableReferenceList = [['_', 'Variable:/:A']]
#life.Iterations = 1
#life.LogEnd = 10
#life.FileName = "life.csv"
#life.Verbose = 1

run(0.1005)
