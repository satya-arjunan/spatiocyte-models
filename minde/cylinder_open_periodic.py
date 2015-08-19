import math 
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 1e-8 
sim.SearchVacant = 1

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 4.5e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 0.96e-6
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 1
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:MinDatp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDadp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinEE').Value = 0

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinDatp')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDatp']]
diffuser.D = 16e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinDadp')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinDadp']]
diffuser.D = 16e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinE')
diffuser.VariableReferenceList = [['_', 'Variable:/:MinEE']]
diffuser.D = 10e-12

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinEE']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDEED']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
logger.LogInterval = 0.5

pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
pop.VariableReferenceList = [['_', 'Variable:/:MinDatp']]
pop.VariableReferenceList = [['_', 'Variable:/:MinDadp']]
pop.VariableReferenceList = [['_', 'Variable:/:MinEE']]
pop.VariableReferenceList = [['_', 'Variable:/Surface:MinEE']]
pop.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE']]
pop.VariableReferenceList = [['_', 'Variable:/Surface:MinDEED']]
pop.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]


theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')
theSimulator.createEntity('Variable', 'Variable:/Surface:MinD').Value = 2600
theSimulator.createEntity('Variable', 'Variable:/Surface:MinEE').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDEE').Value = 1400
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDEED').Value = 0

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinD']]
diffuser.D = 0.02e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinEE')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinEE']]
diffuser.D = 0.02e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinDEE')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE']]
diffuser.D = 0.02e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseMinDEED')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDEED']]
diffuser.D = 0.02e-12

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r1')
r.VariableReferenceList = [['_', 'Variable:/Surface:VACANT','-1']]
r.VariableReferenceList = [['_', 'Variable:/:MinDatp','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','1']]
r.k = 2.2e-8

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r2')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/:MinDatp','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','1']]
r.k = 3e-20

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/:MinEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE','1']]
r.k = 5e-19

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinEE','1']]
r.VariableReferenceList = [['_', 'Variable:/:MinDatp','1']]
r.k = 1

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r5')
r.VariableReferenceList = [['_', 'Variable:/:MinDadp','-1']]
r.VariableReferenceList = [['_', 'Variable:/:MinDatp','1']]
r.k = 5

r = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r6')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinD','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEED','1']]
r.k = 5e-15

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r7')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEED','-1']]
r.VariableReferenceList = [['_', 'Variable:/Surface:MinDEE','1']]
r.VariableReferenceList = [['_', 'Variable:/:MinDadp','1']]
r.k = 1

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r8')
r.VariableReferenceList = [['_', 'Variable:/Surface:MinEE','-1']]
r.VariableReferenceList = [['_', 'Variable:/:MinEE','1']]
r.k = 0.83

run(3000)
