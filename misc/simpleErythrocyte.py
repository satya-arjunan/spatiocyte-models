sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 4.4e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:SHAPE').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 4e-9 #1e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 4e-7 #1e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 4e-7 #1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4

theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')
theSimulator.createEntity('Variable', 'Variable:/Surface:Edge').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:Vertex').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:Spectrin').Value = 483
theSimulator.createEntity('Variable', 'Variable:/Surface:Band3').Value = 56
theSimulator.createEntity('Variable', 'Variable:/Surface:freeBand3').Value = 0

log = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
log.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin']]
log.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]
log.VariableReferenceList = [['_', 'Variable:/Surface:freeBand3']]
log.VariableReferenceList = [['_', 'Variable:/Surface:Edge']]
log.VariableReferenceList = [['_', 'Variable:/Surface:Vertex']]
log.LogInterval = 0.01

# Must put the ErythrocyteProcess under the :/Surface: compartment
ery = theSimulator.createEntity('ErythrocyteProcess', 'Process:/Surface:spec')
ery.VariableReferenceList = [['_', 'Variable:/Surface:Edge', '-1']]
ery.VariableReferenceList = [['_', 'Variable:/Surface:Vertex', '-2']]
ery.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin', '1']]
ery.VariableReferenceList = [['_', 'Variable:/Surface:Band3', '2']]
ery.EdgeLength = 100e-9

dis = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:removeBand3')
dis.VariableReferenceList = [['_', 'Variable:/Surface:Band3', '-1']]
dis.VariableReferenceList = [['_', 'Variable:/Surface:freeBand3', '1']]
dis.k = 100

pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
pop.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin']]
pop.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffFreeBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:freeBand3']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffSpectrin')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin']]
dif.D = 1e-14

run(10)
