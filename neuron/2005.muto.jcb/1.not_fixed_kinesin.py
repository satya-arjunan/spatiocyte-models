
T = 1+10*60.0

nKinesin = 10
VoxelRadius = 0.8e-8
Length = 15e-6
RodRadius = 4.1e-6
#Length = 1e-6
#RodRadius = 4.1e-6

ka0_v = 2.9557e-22
ka1_v = 5.9115e-22
ka2_v = 1.1823e-21

kd0 = 0.001667
kd1 = 0.000667
kd2 = 0.000267

sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 3
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = Length+VoxelRadius*40
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = RodRadius

sim.createEntity('Variable', 'Variable:/:VACANT')
v = sim.createEntity('Variable', 'Variable:/:KIF')
v.Value = nKinesin
#v.Name = "HD"
sim.createEntity('Variable', 'Variable:/:TUB_KIF0' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_KIF1' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB_KIF2' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB0' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB1' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB2' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUBM' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUBP' ).Value = 0

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:populateK')
p.VariableReferenceList = [['_', 'Variable:/:KIF']]
p.VariableReferenceList = [['_', 'Variable:/:TUB0']]
p.VariableReferenceList = [['_', 'Variable:/:TUB1']]
p.VariableReferenceList = [['_', 'Variable:/:TUB2']]
p.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1']]

# Attachments -----------------------------------------------------------------
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b1')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.RandomC = 0
#r.k = ka0_vf
r.k = ka0_v

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b2')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.RandomC = 0
r.k = ka0_v

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b3')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.RandomC = 0
r.k = ka1_v

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b4')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','1']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.RandomC = 0
r.k = ka2_v
#------------------------------------------------------------------------------

# Detachments -----------------------------------------------------------------
r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
r.k = kd0

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
r.k = kd1

r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/:KIF','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
r.k = kd2
#-------------------------------------------------------------------------------


# WalkReact --------------------------------------------------------------------
# | TUB1/TUB2 | KIF0 | TUB1 | TUB/TUB0/TUB1 | ->
# | TUB0/TUB1 | TUB1 | KIF0 | TUB1/TUB1/TUB2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:d5')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.ForcedSequence = 1
r.p = 1

# | TUB1/TUB2 | KIF0 | TUB2 | KIF0/KIF1 | ->
# | TUB0/TUB1 | TUB1 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:d6')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.ForcedSequence = 1
r.p = 1
#
# | KIF1/KIF2 | KIF1 | TUB1 | TUB/TUB0/TUB1 | ->
# | KIF0/KIF1 | TUB2 | KIF0 | TUB1/TUB1/TUB2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:d7')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.ForcedSequence = 1
r.p = 1
#
# | KIF1/KIF2 | KIF1 | TUB2 | KIF0/KIF1 | ->
# | KIF0/KIF1 | TUB2 | KIF1 | KIF1/KIF2 |
r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:d8')
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','1']]
#reactAdjoinsA
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','-10']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','10']]
#reactAdjoinsB
r.VariableReferenceList = [['_', 'Variable:/:TUB','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB2','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1','-20']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2','20']]
r.ForcedSequence = 1
r.p = 1
#-------------------------------------------------------------------------------


r = sim.createEntity('SpatiocyteNextReactionProcess', 'Process:/:d9')
r.VariableReferenceList = [['_', 'Variable:/:TUB0','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','1']]
r.k = 10

# Diffusion --------------------------------------------------------------------
d = sim.createEntity('DiffusionProcess', 'Process:/:dKIF')
d.VariableReferenceList = [['_', 'Variable:/:KIF']]
d.D = 0.6e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_KIF0')
d.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0']]
d.WalkReact = 1
d.D = 0.04e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_KIF1')
d.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1']]
d.WalkReact = 1
d.D = 0.04e-12
#-------------------------------------------------------------------------------

v = sim.createEntity('VisualizationLogProcess', 'Process:/:v')
v.VariableReferenceList = [['_', 'Variable:/:KIF']]
v.VariableReferenceList = [['_', 'Variable:/:TUB']]
#v.VariableReferenceList = [['_', 'Variable:/:TUBM']]
#v.VariableReferenceList = [['_', 'Variable:/:TUBP']]
v.VariableReferenceList = [['_', 'Variable:/:TUB0']]
v.VariableReferenceList = [['_', 'Variable:/:TUB1']]
v.VariableReferenceList = [['_', 'Variable:/:TUB2']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2']]
v.LogInterval = 1

v = sim.createEntity('MicrotubuleProcess', 'Process:/:Filament')
v.OriginX = 0
v.OriginY = 0
v.OriginZ = 0
v.RotateX = 0
v.RotateY = 0
v.RotateZ = 0
v.Radius = 12.5e-9
v.Filaments = 13
v.SubunitRadius = 0.4e-8
v.Length = Length
v.Periodic = 0
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB0' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB1' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB2' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB' , '-1']]
#v.VariableReferenceList = [['_', 'Variable:/:TUBM' , '-2']]
#v.VariableReferenceList = [['_', 'Variable:/:TUBP' , '-3']]

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:TUB_KIF0']]
l.VariableReferenceList = [['_', 'Variable:/:TUB_KIF1']]
l.VariableReferenceList = [['_', 'Variable:/:TUB_KIF2']]
l.LogInterval = 1e-1
l.LogEnd = T-1
l.Iterations = 1
l.FileName = "IterateLog.9pM.csv"

run(T)

