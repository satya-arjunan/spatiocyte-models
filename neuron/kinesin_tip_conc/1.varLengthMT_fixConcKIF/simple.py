import scipy.constants

T = 10
Filaments = 13
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
neuriteRadius = 0.2e-6
neuriteLength = 1e-6
MT_NeuriteTip_space = 0.2e-6
pPlusEnd_Detach = 1
MTLength = neuriteLength-MT_NeuriteTip_space*2
KinesinConc = 2e-7 #in Molar
ActualVolume =  1.14e-19 #in m^3
nKinesin = KinesinConc*scipy.constants.N_A*1e+3*ActualVolume
print "nKinesin:", nKinesin

sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 3 #Rod shaped
sim.createEntity('Variable', 'Variable:/:ROTATEZ').Value = 0
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = neuriteLength
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = neuriteRadius*2
sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:KIF').Value = nKinesin
sim.createEntity('Variable', 'Variable:/:TUB_GTP' ).Value = 0
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

#Loggers-----------------------------------------------------------------------
v = sim.createEntity('VisualizationLogProcess', 'Process:/:v')
v.VariableReferenceList = [['_', 'Variable:/:TUB']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_M']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_P']]
v.VariableReferenceList = [['_', 'Variable:/:KIF']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
v.LogInterval = 1e-2
#-------------------------------------------------------------------------------

#Populate-----------------------------------------------------------------------
p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_KIF')
p.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]

#p = sim.createEntity('MoleculePopulateProcess', 'Process:/:pTUB_GTP')
#p.VariableReferenceList = [['_', 'Variable:/:TUB_GTP']]
#p.LengthBinFractions = [1, 0.3, 0.8]
#p.Priority = 100 #set high priority for accurate fraction

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

#MT KIF detachment to cytosol at plus end---------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_GTP','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p3')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:p4')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_P','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
r.p = pPlusEnd_Detach
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

m = sim.createEntity('MicrotubuleProcess', 'Process:/:Microtubule')
m.OriginX = 0
m.OriginY = 0
m.OriginZ = 0
m.RotateX = 0
m.RotateY = 0
m.RotateZ = 0
m.Radius = MTRadius
m.SubunitRadius = KinesinRadius
m.Length = MTLength
m.Filaments = Filaments
m.Periodic = 0
m.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
m.VariableReferenceList = [['_', 'Variable:/:TUB_KIF_ATP' ]]
m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP' ]]
m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF' ]]
m.VariableReferenceList = [['_', 'Variable:/:TUB_GTP_KIF_ATP' ]]
m.VariableReferenceList = [['_', 'Variable:/:TUB', '-1']]
m.VariableReferenceList = [['_', 'Variable:/:TUB_M', '-2']]
m.VariableReferenceList = [['_', 'Variable:/:TUB_P', '-3']]

run(T+0.01)
