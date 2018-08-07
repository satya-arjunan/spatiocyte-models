sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 100e-9
#
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 100e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Vacant').Value = 0
#
theSimulator.createEntity('Variable', 'Variable:/:MinDm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinEm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDEm').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MinDEEm').Value = 0
s = theSimulator.createEntity('Variable', 'Variable:/:MinD')
s.Value = 50000
s.Name = "HD"
#
s = theSimulator.createEntity('Variable', 'Variable:/:MinE')
s.Value = 30000
s.Name = "HD"
#
# Surface Compartment
fil = theSimulator.createEntity('CompartmentProcess', 'Process:/:Membrane')
fil.VariableReferenceList = [['_', 'Variable:/:Vacant', '-1']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinEm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
fil.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
fil.PlaneXY = 1
#
# Log coordinates for visualization
l = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
l.VariableReferenceList = [['_', 'Variable:/:MinDm']]
l.VariableReferenceList = [['_', 'Variable:/:MinEm']]
l.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
l.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
l.LogInterval = 1
#
## Populate non-HD molecules in compartment
##pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
##pop.VariableReferenceList = [['_', 'Variable:/:MinDm']]
##pop.VariableReferenceList = [['_', 'Variable:/:MinEm']]
#
#
# Diffusion 
# MinDm
dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDm')
dif.VariableReferenceList = [['_', 'Variable:/:MinDm']]
dif.D = 1e-13
#
# MinEm
dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinEm')
dif.VariableReferenceList = [['_', 'Variable:/:MinEm']]
dif.D = 1e-13
#
# MinDEm
dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEm')
dif.VariableReferenceList = [['_', 'Variable:/:MinDEm']]
dif.D = 1e-13
#
# MinDEEm
dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_MinDEEm')
dif.VariableReferenceList = [['_', 'Variable:/:MinDEEm']]
dif.D = 1e-13
#
#
# Reactions
# MinD -> MinDm
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1')
b.VariableReferenceList = [['_', 'Variable:/:MinD','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDm','1']]
b.k = 5e-8
#
# MinE -> MinEm
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2')
b.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
b.k = 5e-10

# MinEm + MinDm -> MinDEm
b = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r3')
b.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
b.k = 6.8e-13

# MinE + MinDm -> MinDEm
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r4')
b.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEm','1']]
b.k = 6.8e-22
#
#
## MinEm + MinDEm -> MinDEEm
b = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:r5')
b.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
b.k = 6.8e-13

## MinE + MinDEm -> MinDEEm
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r6')
b.VariableReferenceList = [['_', 'Variable:/:MinE','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinDEEm','1']]
b.k = 6.8e-22
#
# MinDEEm -> MinEm + MinEm + MinD
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r7')
b.VariableReferenceList = [['_', 'Variable:/:MinDEEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
b.VariableReferenceList = [['_', 'Variable:/:MinEm','1']]
b.VariableReferenceList = [['_', 'Variable:/:MinD','1']]
b.k = 10000
#
# MinEm -> MinE
b = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r8')
b.VariableReferenceList = [['_', 'Variable:/:MinEm','-1']]
b.VariableReferenceList = [['_', 'Variable:/:MinE','1']]
b.k = 0.01
#
run(10000)
