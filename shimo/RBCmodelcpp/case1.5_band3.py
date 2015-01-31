sim = theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = 3.62e-9
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 8.9e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:VACANT').Value = 0

theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT').Value = 0

GFP = theSimulator.createEntity('Variable', 'Variable:/Surface:GFP')
GFP.Value = 0
Band3 = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3')
Band3.Value = 5

tagger = theSimulator.createEntity('TagProcess', 'Process:/:tagger')
tagger.VariableReferenceList = [['_', 'Variable:/Surface:GFP', '-1' ]]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:Band3', '5' ]]

pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
pop.VariableReferenceList = [['_', 'Variable:/Surface:Band3'   ]]

#log = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:log')
#log.VariableReferenceList = [['_', 'Variable:/Surface:Band3'],
#                             ['_', 'Variable:/Surface:GFP']]

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]
dif.D = 1.0e-14

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/Surface:GFP']]
iterator.Iterations = 1000
iterator.LogEnd = 100
iterator.LogStart = 1
iterator.LogInterval = 0.05
iterator.Diffusion = 1
iterator.FileName = "case1.5_band3.csv"

run(101)
