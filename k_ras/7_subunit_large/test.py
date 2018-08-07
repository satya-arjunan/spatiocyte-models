sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.74e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-7*10
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-7*10
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 3

# Create the surface compartment:
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')

theSimulator.createEntity('Variable', 'Variable:/Surface:PS').Value = 450*100
theSimulator.createEntity('Variable', 'Variable:/Surface:PSs').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PS_RAS').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PSs_RAS').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:RAS').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:RAS').Value = 6*100
theSimulator.createEntity('Variable', 'Variable:/Surface:Vacant')

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:RAS']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PS']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PSs']]
logger.LogInterval = 1e-3
logger.MultiscaleStructure = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PS']]
populator.VariableReferenceList = [['_', 'Variable:/:RAS']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop2')
populator.VariableReferenceList = [['_', 'Variable:/Surface:RAS']]
populator.UniformLengthY = 0.99
populator.UniformLengthZ = 0.99

#react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:adsorp')
#react.VariableReferenceList = [['_', 'Variable:/:RAS', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
#react.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '1']]
#react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactRAS_PS')
react.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '1']]
react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dissocPS_RAS')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Lipid', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '1']]
react.p = 0.1


#AA: PSx + PSx => 2 reactions
react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reactAA')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.p = 0.1

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reactAAs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.p = 0.1

#AB: PSx + PSx_RAS => 3 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.p = 0.4

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactABs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.p = 0.4

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAsB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.p = 0.4


#BB: PSx_RAS + PSx_RAS => 2 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.p = 0.4

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBBs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
react.p = 0.4

#First order reactions (deoligomerizations)
react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocPSsLip')
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
#reduce this to increase cluster size
react.k = 6e+4

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocRASPSs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
#reduce this to increase cluster size
react.k = 3e+4

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenRAS')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:RAS']]
diffuser.Interval = 9e-8
#higher propensity means protein can escape raft easily
diffuser.Propensity = 2.5
#diffuser.Propensity = 1
diffuser.Origins = 1

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePS')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PS']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePS_RAS')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '-1']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePSs')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PSs']]
diffuser.D = 0

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePSs_RAS')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '-1']]
diffuser.D = 0

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiRAS_PSs')
multi.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '1']]

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiRAS_PS')
multi.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PS', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:RAS', '1']]

iterator = theSimulator.createEntity('CoordinateLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/Surface:RAS']]
iterator.LogInterval = 1e-3
iterator.LogEnd = 9

fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:filam')
fil.VariableReferenceList = [['_', 'Variable:/Surface:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:RAS']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PS_RAS', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PSs_RAS', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PS', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PSs', '1']]
fil.Length = 1e-7
fil.Width = 1e-7
#fil.Filaments = 4
fil.SubunitRadius = 1.74e-9
fil.SubunitAngle = 0
fil.DiffuseRadius = 0.436e-9
fil.LipidRadius = 0.436e-9
fil.Periodic = 1
fil.RegularLattice = 1

import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(10)
end = time.time()
duration = end-start
print duration
