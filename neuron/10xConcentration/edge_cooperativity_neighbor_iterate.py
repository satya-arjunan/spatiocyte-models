import math

try:
  T
except NameError:
  T = 4000
  K1 = 7.5e-6
  K6 = 1
  K7 = 1e-4
  K8 = 5e+3
  filename = "HistogramLog.csv"

Filaments = 13
RotateAngle = math.pi
MTradius = 12.5e-9
KinesinRadius = 0.4e-8

#from bestTranslocatingSmallNeuron.py
smallNeuronVolumeVoxels = 1792266
smallNeuronTubulins = 225576
smallNeuronActualVolume = 5.716e-18
smallNeuronKinesins = 25.0

#from singleNeuriteMultipleMT.py
singleNeuriteVolumeVoxels = 48325789
singleNeuriteTubulins = 686101
singleNeuriteActualVolume = 1.786e-17


thisVolumeVoxels = 854112 # 2562336/3
thisActualVolume = 2.77e-18 # 8.313e-18/3 
thisTubulins = 106410 # 2.77e-18/1.786e-17*686101= 

comp_x = 30e-6
comp_y = 0.5e-6
comp_z = 0.5e-6
VoxelRadius = 0.8e-8
totalKinesins = 500 # 10 uM

theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius

# Create the root container compartment using the default Cuboid geometry:
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = comp_x
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = comp_y
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = comp_z
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT')


theSimulator.createEntity('Variable', 'Variable:/:Kinesin').Value = totalKinesins
theSimulator.createEntity('Variable', 'Variable:/:MTKinesin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MTKinesinATP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:Tubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:actTubulin' ).Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:TubulinM' ).Value = 0
#theSimulator.createEntity('Variable', 'Variable:/:TubulinP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:GFP' ).Value = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populate')
populator.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
populator.VariableReferenceList = [['_', 'Variable:/:actTubulin']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populateK')
populator.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
#populator.OriginX = -1.0
#populator.UniformRadiusX = 0.1

#react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:detachPlus')
#react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
#react.VariableReferenceList = [['_', 'Variable:/:TubulinP','-1']]
#react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
#react.VariableReferenceList = [['_', 'Variable:/:TubulinP','1']]
#react.p = 1

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseKinesin')
diffuse.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
diffuse.D = 0.5e-12

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:explicitAttachAct_k6')
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
#react.k = 2.5863133e-22
react.p = K6
#react.k = 1.69706e-20

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:explicitAttach_k1')
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
#react.k = 2.5863133e-24
react.p = K1
#react.k = 6.78823e-24

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:detach_k4')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.SearchVacant = 1
react.k = K8

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:detach_k8')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.SearchVacant = 1
react.k = K8

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:inactive_k7')
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','1']]
react.k = K7

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:hydrolysis_k3')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
react.SearchVacant = 1
react.k = 100

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:phosphorylate_k2')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','1']]
react.SearchVacant = 1
react.k = 145

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:ratchet_k5')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.BindingSite = 1
react.k = 55

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffusePlus')
diffuse.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
diffuse.VariableReferenceList = [['_', 'Variable:/:actTubulin', '2']]
diffuse.D = 0.04e-12

#tagger = theSimulator.createEntity('TagProcess', 'Process:/:tagger')
#tagger.VariableReferenceList = [['_', 'Variable:/:GFP', '-1' ]]
#tagger.VariableReferenceList = [['_', 'Variable:/:Kinesin', '5' ]]
#tagger.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
#tagger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP']]

#life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
#life.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '-1']]
#life.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '-1']]
#life.VariableReferenceList = [['_', 'Variable:/:Kinesin', '1']]

his = theSimulator.createEntity('HistogramLogProcess', 'Process:/:his')
his.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
his.Length = comp_x
his.Radius = comp_y
his.Bins = 3
his.LogInterval = 10
his.FileName = filename

radiusScale = 10600
visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
visualLogger.VariableReferenceList = [['_', 'Variable:/:Tubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:Kinesin', '%d' %(radiusScale)]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '%d' %((radiusScale-10000)*VoxelRadius/KinesinRadius+10000)]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '%d' %((radiusScale-10000)*VoxelRadius/KinesinRadius+10000)]]
visualLogger.LogInterval = 5

MTn = 9
MTlength_x = 8e-6
MTlength_y = MTradius*2
MTlength_z = MTradius*2
MTn_z = 3
MTinterval_min_x = 0.1e-6
len_x = comp_x/2
MTn_x = int(len_x/(MTlength_x+MTinterval_min_x))
MTn_y = MTn/MTn_z/MTn_x
print "MTn_x:",MTn_x,"MTn_y:",MTn_y,"MTn_z:",MTn_z
MTinterval_x = (len_x-MTn_x*MTlength_x)/MTn_x
MTinterval_y = (comp_y-MTn_y*MTlength_y)/MTn_y
MTinterval_z = (comp_z-MTn_z*MTlength_z)/MTn_z

print "MTinterval_x:",MTinterval_x,"MTinterval_y:",MTinterval_y,"MTinterval_z:",MTinterval_z

for i in range(MTn_x):
  for j in range(MTn_y):
    for k in range(MTn_z):
      Microtubule = theSimulator.createEntity('MicrotubuleProcess', 'Process:/:Microtubule%d%d%d' %(i,j,k))
      X = (comp_x-MTlength_x/2)/comp_x*2-1
      Y = ((MTlength_y+MTinterval_y)/2+(MTinterval_y+MTlength_y)*j)/comp_y*2-1
      Z = ((MTlength_z+MTinterval_z)/2+(MTinterval_z+MTlength_z)*k)/comp_z*2-1
      Microtubule.OriginX = X
      Microtubule.OriginY = Y
      Microtubule.OriginZ = Z
      Microtubule.RotateX = 0
      Microtubule.RotateY = 0
      Microtubule.RotateZ = 0
      Microtubule.Radius = MTradius
      Microtubule.SubunitRadius = KinesinRadius
      Microtubule.Length = MTlength_x
      Microtubule.Filaments = Filaments
      Microtubule.Periodic = 1
      Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesin' ]]
      Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP' ]]
      Microtubule.VariableReferenceList = [['_', 'Variable:/:actTubulin' ]]
      Microtubule.VariableReferenceList = [['_', 'Variable:/:Tubulin' , '-1']]
      #Microtubule.VariableReferenceList = [['_', 'Variable:/:TubulinM' , '-2']]
      #Microtubule.VariableReferenceList = [['_', 'Variable:/:TubulinP' , '-3']]

run(T)


