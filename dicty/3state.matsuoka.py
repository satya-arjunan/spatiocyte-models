duration = 10

sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 4.4e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

r = theSimulator.createEntity('Variable', 'Variable:/:PTENp2')
r.Value = 942
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:PTENa')
r.Value = 944
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:PTEN')
r.Value = 80
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:PTENvol')
r.Value = 1966
r.Name = "HD"

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 6.289
r.LogEvent = 1
r.LogStart = 5

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 0.036

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = 2.896

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 3.995

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = 0.406

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 0.029

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '1']]
r.k = 12.525

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENp2', '1']]
r.k = 1.63959

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTENa', '1']]
r.k = 0.48894

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:PTENvol', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:PTEN', '1']]
r.k = 0.31983

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:PTENp2']]
l.VariableReferenceList = [['_', 'Variable:/:PTENa']]
l.VariableReferenceList = [['_', 'Variable:/:PTEN']]
l.VariableReferenceList = [['_', 'Variable:/:PTENvol']]
l.LogInterval = 5e-1
l.LogEnd = duration
l.Iterations = 1

run(duration+0.1)
