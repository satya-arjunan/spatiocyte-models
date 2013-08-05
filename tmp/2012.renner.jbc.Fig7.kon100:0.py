sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.74e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1.115e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1.115e-7
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 3

# Create the surface compartment:
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDatp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDD').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDadp').Value = 0

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
logger.LogInterval = 1
logger.MultiscaleStructure = 1

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop2')
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:konMinDatp')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '1']]
react.k = 1.70e+14

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:koffMinDatp')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.k = 0.1667

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:koffMinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.k = 0.1667

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:dissociateMinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '1']]
react.k = 0.005 #2x loose since 2ATP -> 2ADP

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dimerizeMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]
react.p = 0.00001

diff = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffMinDatp')
diff.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
diff.D = 1e-13

diff = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffMinDadp')
diff.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
diff.D = 1e-13

diff = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffMinDD')
diff.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
diff.D = 1e-13

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
iterator.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
iterator.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
iterator.Iterations = 1
iterator.LogEnd = 1000
iterator.LogStart = 10
iterator.LogInterval = 1

#life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
#life.VariableReferenceList = [['_', 'Variable:/Surface:MinD', '-1']]
#life.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
#life.Iterations = 1
#life.LogEnd = 9.99
#life.FileName = "LifetimeLogMinDKon.csv"

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
fil.SubunitRadius = 2.81e-9
fil.SubunitAngle = 0
#fil.DiffuseRadius = 0.436e-9
fil.DiffuseRadius = 2.81e-9
#fil.LipidRadius = 0.436e-9
fil.LipidRadius = 2.81e-9
fil.Periodic = 1
fil.RegularLattice = 1

import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(1001)
end = time.time()
duration = end-start
print duration
