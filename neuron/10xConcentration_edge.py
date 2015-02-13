import math

Filaments = 13
RotateAngle = math.pi
MTradius = 12.5e-9
KinesinRadius = 0.4e-8
neuriteRadius = 0.2e-6
neuriteLength = 5e-6

comp_x = 30e-6
comp_y = 3.4e-6
comp_z = 500e-9
VoxelRadius = 0.8e-8

singleMTVolumeVoxels = 717256.0
singleNeuriteVolumeVoxels = 48325789.0
totalKinesins = 100
print "totalKinesins:", totalKinesins

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
react.p = 1
#react.k = 1.69706e-20

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:explicitAttach_k1')
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','1']]
#react.k = 2.5863133e-24
react.p = 0.005
#react.k = 6.78823e-24

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:detach_k4')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.SearchVacant = 1
react.k = 15

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:inactive_k7')
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','1']]
react.k = 0.055

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
diffuse.VariableReferenceList = [['_', 'Variable:/:actTubulin', '1']]
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

visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
visualLogger.VariableReferenceList = [['_', 'Variable:/:Tubulin']]
#visualLogger.VariableReferenceList = [['_', 'Variable:/:TubulinM']]
#visualLogger.VariableReferenceList = [['_', 'Variable:/:TubulinP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:Kinesin', '10600']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '10600']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '10600']]
visualLogger.VariableReferenceList = [['_', 'Variable:/Surface:VACANT']]
visualLogger.LogInterval = 10

MTn = 60
MTlength_x = 10e-6
MTlength_y = MTradius*2
MTlength_z = MTradius*2
MTn_z = 3
MTinterval_min_x = 0.2e-6
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
      X = ((MTlength_x+MTinterval_x+comp_x-len_x)/2+(MTinterval_x+MTlength_x)*i)/comp_x*2-1
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

run(1000000000)


