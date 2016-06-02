import numpy as np

VoxelRadius = 0.8e-8
nNeurite = 5
neuriteRadius = 0.2e-6
neuriteSpace = neuriteRadius*2
somaLength = nNeurite*neuriteRadius*2+neuriteSpace*(nNeurite+1)
somaWidth = somaLength/2
somaHeight = neuriteRadius*3
inSomaLength = VoxelRadius*6
neuriteLengths = np.empty((nNeurite))
neuriteLengths.fill(4e-6+inSomaLength)
rootSpace = VoxelRadius*6
rootLengths = np.empty((1,3))
rootLengths = (somaWidth+np.amax(neuriteLengths)-inSomaLength+rootSpace*2,
    somaLength+rootSpace*2, somaHeight+rootSpace*2)
neuriteOrigins = np.zeros((nNeurite, 3))
halfRootLengths = np.divide(rootLengths, 2.0)
somaOrigin = np.zeros((nNeurite, 3))
somaOrigin = (rootSpace+somaWidth/2, rootSpace+somaLength/2,
    rootSpace+somaHeight/2)
with np.errstate(divide='ignore', invalid='ignore'):
  somaOrigin = np.divide(np.subtract(somaOrigin, halfRootLengths),
      halfRootLengths)
  somaOrigin[somaOrigin == np.inf] = 0
  somaOrigin = np.nan_to_num(somaOrigin)

for i in range(nNeurite):
  neuriteOrigins[i] = np.array([rootSpace+somaWidth+(neuriteLengths[i]-
    inSomaLength)/2, 
    rootSpace+neuriteSpace+i*(neuriteRadius*2+neuriteSpace)+neuriteRadius,
    rootSpace+somaHeight/2])
  with np.errstate(divide='ignore', invalid='ignore'):
    neuriteOrigins[i] = np.divide(np.subtract(neuriteOrigins[i],
      halfRootLengths), halfRootLengths)
    neuriteOrigins[i][neuriteOrigins[i] == np.inf] = 0
    neuriteOrigins[i] = np.nan_to_num(neuriteOrigins[i])


sim = theSimulator
s = sim.createStepper('SpatiocyteStepper', 'SS')
s.VoxelRadius = VoxelRadius
s.SearchVacant = 1
s.RemoveSurfaceBias = 1
sim.rootSystem.StepperID = 'SS'

sim.createEntity('Variable', 'Variable:/:LENGTHX').Value = rootLengths[0]
sim.createEntity('Variable', 'Variable:/:LENGTHY').Value = rootLengths[1]
sim.createEntity('Variable', 'Variable:/:LENGTHZ').Value = rootLengths[2]
sim.createEntity('Variable', 'Variable:/:VACANT')

sim.createEntity('System', 'System:/:Soma').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma:GEOMETRY').Value = 0
sim.createEntity('Variable', 'Variable:/Soma:LENGTHX').Value = somaWidth
sim.createEntity('Variable', 'Variable:/Soma:LENGTHY').Value = somaLength
sim.createEntity('Variable', 'Variable:/Soma:LENGTHZ').Value = somaHeight
sim.createEntity('Variable', 'Variable:/Soma:ORIGINX').Value = somaOrigin[0]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINY').Value = somaOrigin[1]
sim.createEntity('Variable', 'Variable:/Soma:ORIGINZ').Value = somaOrigin[2]
sim.createEntity('Variable', 'Variable:/Soma:VACANT').Value = -1

sim.createEntity('System', 'System:/Soma:Surface').StepperID = 'SS'
sim.createEntity('Variable', 'Variable:/Soma/Surface:DIMENSION').Value = 2
sim.createEntity('Variable', 'Variable:/Soma/Surface:VACANT')

for i in range(nNeurite):
  sim.createEntity('System', 'System:/:Neurite%d' %i).StepperID = 'SS'
  sim.createEntity('Variable', 'Variable:/Neurite%d:GEOMETRY' %i).Value = 2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHX' %i)
  x.Value = neuriteLengths[i]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:LENGTHY' %i)
  y.Value = neuriteRadius*2
  x = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINX' %i)
  x.Value = neuriteOrigins[i][0]
  y = sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINY' %i)
  y.Value = neuriteOrigins[i][1]
  sim.createEntity('Variable', 'Variable:/Neurite%d:ORIGINZ' %i).Value = 0
  sim.createEntity('Variable', 'Variable:/Neurite%d:VACANT' %i)
  d = sim.createEntity('Variable', 'Variable:/Neurite%d:DIFFUSIVE' %i)
  d.Name = '/:Soma'
  # Create the neurite membrane:
  sim.createEntity('System', 'System:/Neurite%d:Surface' %i).StepperID = 'SS'
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Surface:DIMENSION' %i).Value = 2
  sim.createEntity('Variable', 'Variable:/Neurite%d/Surface:VACANT' %i)
  sim.createEntity('Variable',
      'Variable:/Neurite%d/Surface:DIFFUSIVE' %i).Name = '/Soma:Surface'


sim.createEntity('Variable', 'Variable:/Soma:MinDadp').Value = 1000

d = sim.createEntity('DiffusionProcess', 'Process:/Soma:diffuseMinDadp')
d.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp']]
d.D = 1e-12

l = sim.createEntity('VisualizationLogProcess', 'Process:/Soma:logger')
l.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp']]
l.VariableReferenceList = [['_', 'Variable:/Soma/Surface:VACANT']]
l.LogInterval = 0.1

p = sim.createEntity('MoleculePopulateProcess', 'Process:/Soma:pop')
p.VariableReferenceList = [['_', 'Variable:/Soma:MinDadp']]

run(100)
