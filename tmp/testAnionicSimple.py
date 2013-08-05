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

theSimulator.createEntity('Variable', 'Variable:/Surface:PG').Value = 7524
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PG_MinDD').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs_MinDD').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDD').Value = 0


populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PG']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop2')
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:koffMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '0']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '0']]
react.k = 500
#react.Rates = [1, 0.1, 0.1]
react.Rates = [0.5, 0.1, 0.1]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:konMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '0']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '0']]
react.k = 4.04e+18
#react.Rates = [0.01, 1, 1]
react.Rates = [1, 1, 1]


react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactMinDD_PG')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dissocPG_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Lipid', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
react.p = 1


#AA: PGx + PGx => 2 reactions
react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reactAA')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.p = 0.1

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reactAAs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.p = 0.1


#AB: PGx + PGx_MinDD => 3 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAB_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactABs_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAsB_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.p = 0.1


#BB: PGx_MinDD + PGx_MinDD => 2 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBB_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBBs_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
react.p = 0.1


#First order reactions (deoligomerizations)
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocPGsLip')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+5


react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocMinDD_PGs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+5


multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDD_PGs')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDD_PG')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenMinDD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
#diffuser.Interval = 5e-6
#diffuser.Propensity = 1e+1
diffuser.D = 1e-12
diffuser.MoleculeRadius = 3.61e-9



diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePG_MinDD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
diffuser.D = 10e-12



diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePGs_MinDD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
diffuser.D = 0


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePG')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PG']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePGs')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PGs']]
diffuser.D = 0


fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
fil.Length = 1e-7
fil.Width = 1e-7
#fil.Filaments = 4
fil.SubunitRadius = 2.81e-9
fil.SubunitAngle = 0
fil.DiffuseRadius = 0.436e-9
fil.LipidRadius = 0.436e-9
fil.Periodic = 1
fil.RegularLattice = 1

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs']]
logger.LogInterval = 1e-4
logger.MultiscaleStructure = 1

life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
life.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
life.Iterations = 1
life.LogEnd = 0.09
life.FileName = "LifetimeLogMinDKon.csv"
life.Verbose = 1

import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(10)
end = time.time()
duration = end-start
print duration
