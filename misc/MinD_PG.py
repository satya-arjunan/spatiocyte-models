sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 2.74e-9
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1.0e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1.115e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1.115e-7
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Vacant')
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 3

# Create the surface compartment:
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')

theSimulator.createEntity('Variable', 'Variable:/Surface:PG').Value = 3400
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PG_MinDatp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs_MinDatp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PG_MinDadp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs_MinDadp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PG_MinDD').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:PGs_MinDD').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDatp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDadp').Value = 0
theSimulator.createEntity('Variable', 'Variable:/Surface:MinDD').Value = 0


populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/Surface:PG']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop2')
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
populator.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:koffMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Vacant', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '0']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '0']]
react.k = 500
react.Rates = [1, 1, 1]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:konMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '0']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '0']]
react.k = 4.04e+18
react.Rates = [0.01, 1, 1]

react = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:dissociateMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '1']]
react.k = 500

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dimerizeMinD')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '1']]
react.p = 0.1
react.SearchVacant = 1


react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactMinDatp_PG')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '1']]
react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dissocPG_MinDatp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Lipid', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
react.p = 0.3

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactMinDadp_PG')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '1']]
react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dissocPG_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Lipid', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
react.p = 0.3

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactMinDD_PG')
react.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
react.p = 1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:dissocPG_MinDD')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/:Lipid', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '1']]
react.p = 0.3


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


#AB: PGx + PGx_MinDatp => 3 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactABs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAsB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.p = 0.1

#AB: PGx + PGx_MinDadp => 3 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAB_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactABs_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactAsB_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
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


#BB: PGx_MinDatp + PGx_MinDatp => 2 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBB')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBBs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
react.p = 0.1

#BB: PGx_MinDadp + PGx_MinDadp => 2 reactions
react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBB_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
react.p = 0.1

react = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:reactBBs_MinDadp')
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
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


react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocMinDatpPGs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+5

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocMinDadpPGs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+5

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:dissocMinDD_PGs')
react.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD', '-1']]
react.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD', '1']]
react.Deoligomerize = 6
react.SearchVacant = 1
react.k = 1e+5


multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDatp_PGs')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '1']]

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDatp_PG')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '1']]

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDadp_PGs')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '1']]

multi = theSimulator.createEntity('MultiscaleReactionProcess', 'Process:/:multiMinDadp_PG')
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG', '-1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '1']]
multi.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '1']]

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


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenMinDatp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
diffuser.Interval = 5e-6
diffuser.Propensity = 1e+1
diffuser.MoleculeRadius = 2.81e-9

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenMinDadp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
diffuser.Interval = 5e-6
diffuser.Propensity = 1e+1
diffuser.MoleculeRadius = 2.81e-9

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:propenMinDD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
diffuser.Interval = 5e-6
diffuser.Propensity = 1e+1
diffuser.MoleculeRadius = 3.61e-9


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePG_MinDatp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePG_MinDadp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
diffuser.D = 10e-12

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePG_MinDD')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDD', '-1']]
diffuser.D = 10e-12


diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePGs_MinDatp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp', '-1']]
diffuser.D = 0

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePGs_MinDadp')
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp']]
diffuser.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp', '-1']]
diffuser.D = 0

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
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp', '1']]
fil.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp', '1']]
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
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDatp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDatp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDatp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDadp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDadp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDadp']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG_MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs_MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:MinDD']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PG']]
logger.VariableReferenceList = [['_', 'Variable:/Surface:PGs']]
logger.LogInterval = 1e-4
logger.MultiscaleStructure = 1

import time
run(1e-6)
print "Done stirring. Now running..."
start = time.time()
run(0.1)
end = time.time()
duration = end-start
print duration
