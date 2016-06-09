
sim = theSimulator
sim.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = 0.4e-8
sim.rootSystem.StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 3
sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = 0.4e-6
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = 0.15e-6

sim.createEntity('Variable', 'Variable:/:VACANT')
sim.createEntity('Variable', 'Variable:/:KIF').Value = 100
sim.createEntity('Variable', 'Variable:/:TUB_KIF' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUB' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUBM' ).Value = 0
sim.createEntity('Variable', 'Variable:/:TUBP' ).Value = 0

p = sim.createEntity('MoleculePopulateProcess', 'Process:/:populateK')
p.VariableReferenceList = [['_', 'Variable:/:KIF']]

r = sim.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:b1')
r.VariableReferenceList = [['_', 'Variable:/:KIF','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB','-1']]
r.VariableReferenceList = [['_', 'Variable:/:TUB_KIF','1']]
r.p = 1


d = sim.createEntity('DiffusionProcess', 'Process:/:dKIF')
d.VariableReferenceList = [['_', 'Variable:/:KIF']]
d.D = 0.5e-12

d = sim.createEntity('DiffusionProcess', 'Process:/:dTUB_KIF')
d.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]
d.WalkReact = 1
d.D = 0.04e-12

v = sim.createEntity('VisualizationLogProcess', 'Process:/:v')
v.VariableReferenceList = [['_', 'Variable:/:KIF']]
v.VariableReferenceList = [['_', 'Variable:/:TUB']]
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF']]
v.VariableReferenceList = [['_', 'Variable:/:TUBM']]
v.VariableReferenceList = [['_', 'Variable:/:TUBP']]
v.LogInterval = 1e-3

v = sim.createEntity('FilamentProcess', 'Process:/:Filament')
v.OriginX = 0
v.OriginY = 0
v.OriginZ = 0
v.RotateX = 0
v.RotateY = 0
v.RotateZ = 0
v.SubunitRadius = 0.4e-8
v.Length = 0.38e-6
v.Periodic = 0
v.VariableReferenceList = [['_', 'Variable:/:TUB_KIF' ]]
v.VariableReferenceList = [['_', 'Variable:/:TUB' , '-1']]
v.VariableReferenceList = [['_', 'Variable:/:TUBM' , '-2']]
v.VariableReferenceList = [['_', 'Variable:/:TUBP' , '-3']]

run(1)

