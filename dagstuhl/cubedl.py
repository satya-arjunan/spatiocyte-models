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

theSimulator.createEntity('Variable', 'Variable:/:A').Value = 100
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 100
theSimulator.createEntity('Variable', 'Variable:/:C').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:D').Value = N

#logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
#logger.VariableReferenceList = [['_', 'Variable:/:A'], ['_', 'Variable:/:B'], ['_', 'Variable:/:C'], ['_', 'Variable:/:D']]
#logger.LogInterval = 0.01

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:B']]
populator.VariableReferenceList = [['_', 'Variable:/:D']]

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:C','1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','1']]
#binder.k = 8.48e-20
binder.p = 1

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseC')
diffuser.VariableReferenceList = [['_', 'Variable:/:C']]
diffuser.D = 10e-12

log = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
log.VariableReferenceList = [['_', 'Variable:/:A']]
log.Iterations = 100
log.LogEnd = 0.0001
log.LogInterval = 1e-6
log.FileName = "log%ddl.csv" %(N)

#life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
#life.VariableReferenceList = [['_', 'Variable:/:A']]
#life.Iterations = 1
#life.LogEnd = 10
#life.FileName = "life.csv"
#life.Verbose = 1

run(0.00015)
