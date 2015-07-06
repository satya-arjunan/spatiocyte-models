Filaments = 13
RotateAngle = 0 #math.pi/4
MTRadius = 12.5e-9
VoxelRadius = 0.4e-8
KinesinRadius = 0.4e-8
dendriteRadius = 0.15e-6
dendriteLength = 0.7e-6
totalMTLength = 0.6e-6

theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = VoxelRadius
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 0.8e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

theSimulator.createEntity('System', 'System:/:neurite').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/neurite:GEOMETRY').Value = 3
theSimulator.createEntity('Variable', 'Variable:/neurite:LENGTHX').Value = dendriteLength
theSimulator.createEntity('Variable', 'Variable:/neurite:LENGTHY').Value = dendriteRadius*2
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINX').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ORIGINZ').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:ROTATEZ').Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:VACANT')
theSimulator.createEntity('System', 'System:/neurite:Membrane').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/neurite/Membrane:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/neurite/Membrane:VACANT')

theSimulator.createEntity('Variable', 'Variable:/neurite:Kinesin').Value = 80
theSimulator.createEntity('Variable', 'Variable:/neurite:MTKinesin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:MTKinesinATP' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:Tubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:actTubulin' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:TubulinM' ).Value = 0
theSimulator.createEntity('Variable', 'Variable:/neurite:TubulinP' ).Value = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:populate')
populator.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]

diffuse = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseKinesin')
diffuse.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]
diffuse.D = 4e-12

visualLogger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:visualLogger')
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Tubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:TubulinM']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:TubulinP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Kinesin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:actTubulin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesin']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesinATP']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite:Interface']]
visualLogger.VariableReferenceList = [['_', 'Variable:/neurite/Membrane:VACANT']]
visualLogger.LogInterval = 0.0001


Microtubule = theSimulator.createEntity('MicrotubuleProcess', 'Process:/neurite:Microtubule')
Microtubule.OriginX = 0
Microtubule.OriginY = 0
Microtubule.OriginZ = 0
Microtubule.RotateX = 0
Microtubule.RotateY = 0
Microtubule.RotateZ = 0
Microtubule.Radius = MTRadius
Microtubule.SubunitRadius = KinesinRadius
Microtubule.Length = totalMTLength
Microtubule.Filaments = 13
Microtubule.Periodic = 0
Microtubule.BindingDirection = 0
Microtubule.DissociationDirection = 0
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesin' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:MTKinesinATP' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:actTubulin' ]]
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:Tubulin' , '-1']]
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:TubulinM' , '-2']]
Microtubule.VariableReferenceList = [['_', 'Variable:/neurite:TubulinP' , '-3']]

run(0.01)

