
sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = VoxelRadius
s.SearchVacant = 1
s.RemoveSurfaceBias = 1
sim.rootSystem.StepperID = 'SS'

sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = rootLengths[0]
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = rootLengths[1]
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = rodRadius*4+6*VoxelRadius
sim.createEntity('Variable', 'Variable:/:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 1
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = somaRadius*2
sim.createEntity('Variable', 'Variable:/Soma:ORIGINX').Value = somaOrigin[0]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINY').Value = somaOrigin[1]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINZ').Value = somaOrigin[2]
sim.createEntity('Variable', 'Variable:/Soma:VACANT').Value = -1

sim.createEntity('System', 'System:/Soma:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Surface:VACANT')
