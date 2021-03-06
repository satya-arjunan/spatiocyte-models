Filaments = 13
RotateAngle = 0 #math.pi/4
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
neuriteLength = 5e-6
neuriteRadius = 0.2e-6
MTLength = neuriteLength*0.95


theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 2
theSimulator.createEntity('Variable', 'Variable:/:ROTATEZ').Value = RotateAngle
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = neuriteLength
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = neuriteRadius*2
theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:Kinesin').Value = 100
theSimulator.createEntity('Variable', 'Variable:/:Crowder').Value = 500000
#theSimulator.createEntity('Variable', 'Variable:/:Crowder').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MTKinesin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:MTKinesinATP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:Tubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:actTubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:TubulinM' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:TubulinP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/:GFP' ).Value = 0

theSimulator.createEntity('System', 'System:/:Membrane').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Membrane:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Membrane:VACANT')

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populate')
populator.VariableReferenceList = [['_', 'Variable:/:MTKinesin']]
populator.VariableReferenceList = [['_', 'Variable:/:actTubulin']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populateCrowder')
populator.VariableReferenceList = [['_', 'Variable:/:Crowder']]

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populateK')
populator.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
#populator.OriginX = -1.0
#populator.UniformRadiusX = 0.1

react = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:detachPlus')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:TubulinP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.VariableReferenceList = [['_', 'Variable:/:TubulinP','1']]
react.p = 1

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseKinesin')
diffuse.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
diffuse.D = 0.5e-12

#diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseCrowder')
#diffuse.VariableReferenceList = [['_', 'Variable:/:Crowder']]
#diffuse.D = 0.5e-12




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
react.p = 0.001
#react.Collision = 3
#react.k = 6.78823e-24

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:detach_k4')
react.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP','-1']]
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','1']]
react.VariableReferenceList = [['_', 'Variable:/:Kinesin','1']]
react.SearchVacant = 0
react.k = 15

react = theSimulator.createEntity('SpatiocyteTauLeapProcess', 'Process:/:inactive_k7')
react.VariableReferenceList = [['_', 'Variable:/:actTubulin','-1']]
react.VariableReferenceList = [['_', 'Variable:/:Tubulin','1']]
react.k = 10




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

life = theSimulator.createEntity('LifetimeLogProcess', 'Process:/:lifetime')
life.VariableReferenceList = [['_', 'Variable:/:MTKinesin', '-1']]
life.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP', '-1']]
life.Iterations = 1
life.LogEnd = 10000
life.FileName = "LifetimeLogKinesinInVitroCrowded.csv"
life.Verbose = 1

visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
#visualLogger.VariableReferenceList = [['_', 'Variable:/:Crowder']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:Tubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:Kinesin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesin' ]]
visualLogger.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP' ]]
visualLogger.LogInterval = 10

Microtubule = theSimulator.createEntity('MicrotubuleProcess', 'Process:/:Microtubule')
Microtubule.OriginX = 0
Microtubule.OriginY = 0
Microtubule.OriginZ = 0
Microtubule.RotateX = 0
Microtubule.RotateY = 0
Microtubule.RotateZ = RotateAngle
Microtubule.Radius = MTRadius
Microtubule.SubunitRadius = KinesinRadius
Microtubule.Length = MTLength
Microtubule.Filaments = Filaments
Microtubule.Periodic = 1
Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesin' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:MTKinesinATP' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:actTubulin' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/:Tubulin' , '-1']]

run(100000)

