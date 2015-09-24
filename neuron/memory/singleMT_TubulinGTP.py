Filaments = 13
RotateAngle = 0 #math.pi/4
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
dendriteRadius = 0.15e-6
dendriteLength = 0.7e-6
totalMTLength = 8e-6

sim = theSimulator

sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 2
sim.createEntity('Variable', 'Variable:/:ROTATEZ').Value = RotateAngle
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = dendriteLength
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = dendriteRadius*2
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:KIF').Value = 25
sim.createEntity('Variable', 'Variable:/:TUB_GTP' ).Value = 1
sim.createEntity('Variable', 'Variable:/:TUB_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_GTP_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_GTP_KIF_ATP' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_M' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_P' ).Value = 0

sim.createEntity('System', 'System:/:Membrane').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Membrane:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Membrane:VACANT')

#Populate-----------------------------------------------------------------------
p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_KIF')
p.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_GTP')
p.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
p.LengthBinFractions = [1, 0.3, 0.8]
p.Priority = 100 #set high priority for accurate fraction

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pKIF')
p.VariableReferenceList = [['_', 'Variable:/:KIF']]
#-------------------------------------------------------------------------------

#Cytosolic KIF recruitment to microtubule---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b1')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b2')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.p = 1
#-------------------------------------------------------------------------------

#MT KIF detachment to cytosol---------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:detach')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.SearchVacant = 1
r.k = 15

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:detachGTP')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.SearchVacant = 1
r.k = 15
#-------------------------------------------------------------------------------

#KIF ATP hydrolysis-------------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:h1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.SearchVacant = 1
r.k = 100

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:h2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.SearchVacant = 1
r.k = 100
#-------------------------------------------------------------------------------

#KIF ADP phosphorylation--------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:phos1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:phos2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']]
r.SearchVacant = 1
r.k = 145
#-------------------------------------------------------------------------------

#KIF ratchet biased walk_-------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rat1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','0']] #If BindingSite[1]==TUB
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']] #option 1
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','0']] #Elif BindingSite[1]==TUB_GTP
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']] #option 2
r.BindingSite = 1
r.k = 55

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rat2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]    #A
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]         #C
r.VariableReferenceList = [['_', 'Variable:/:TUB','0']]             #E
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','1']]     #D
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','0']]         #H
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','1']] #F
r.BindingSite = 1
r.k = 55
#-------------------------------------------------------------------------------

#KIF random walk between GTP and GDP tubulins-----------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.ForcedSequence = 1
r.p = 1

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:w3')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','1']]
r.ForcedSequence = 1
r.p = 1
#-------------------------------------------------------------------------------

#KIF normal diffusion-----------------------------------------------------------
d = sim.createEntity('DiffusionProcess', 'Process:/:dKIF')
d.VariableReferenceList = [['_', 'Variable:/:KIF']]
d.D = 0.5e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_KIF')
d.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_GTP_KIF')
d.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------


visualLogger = sim.createEntity('VisualizationLogProcess', 'Process:/:v')
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_M']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_P']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:KIF']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
visualLogger.LogInterval = 1e-2

Microtubule = sim.createEntity('MicrotubuleProcess', 'Process:/:Microtubule')
Microtubule.OriginX = 0
Microtubule.OriginY = 0
Microtubule.OriginZ = 0
Microtubule.RotateX = 0
Microtubule.RotateY = 0
Microtubule.RotateZ = RotateAngle
Microtubule.Radius = MTRadius
Microtubule.SubunitRadius = KinesinRadius
Microtubule.Subunits = 70
Microtubule.Filaments = 13
Microtubule.Periodic = 0
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_GTP' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB', '-1']]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_M', '-2']]
Microtubule.VariableReferenceList = [['_', 'Variable:/:TUB_P', '-3']]

run(10)

