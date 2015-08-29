duration = 10000

sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 4.4e-9 
sim.SearchVacant = 0

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 1e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1e-6
theSimulator.createEntity('Variable', 'Variable:/:VACANT')

r = theSimulator.createEntity('Variable', 'Variable:/:S1')
r.Value = 0
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:S2')
r.Value = 0
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:S3')
r.Value = 0
r.Name = "HD"

r = theSimulator.createEntity('Variable', 'Variable:/:V')
r.Value = 500
r.Name = "HD"

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r12')
r.VariableReferenceList = [['_', 'Variable:/:S1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S2', '1']]
r.k = 6.289

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r1V')
r.VariableReferenceList = [['_', 'Variable:/:S1', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:V', '1']]
r.k = 0.036

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r21')
r.VariableReferenceList = [['_', 'Variable:/:S2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S1', '1']]
r.k = 2.896

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r2V')
r.VariableReferenceList = [['_', 'Variable:/:S2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:V', '1']]
r.k = 3.995

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r23')
r.VariableReferenceList = [['_', 'Variable:/:S2', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S3', '1']]
r.k = 0.406

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r32')
r.VariableReferenceList = [['_', 'Variable:/:S3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S2', '1']]
r.k = 0.029

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:r3V')
r.VariableReferenceList = [['_', 'Variable:/:S3', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:V', '1']]
r.k = 12.525

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV1')
r.VariableReferenceList = [['_', 'Variable:/:V', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S1', '1']]
r.k = 1.63959

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV2')
r.VariableReferenceList = [['_', 'Variable:/:V', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S2', '1']]
r.k = 0.48894

r = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:rV3')
r.VariableReferenceList = [['_', 'Variable:/:V', '-1']]
r.VariableReferenceList = [['_', 'Variable:/:S3', '1']]
r.k = 0.31983

l = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iter')
l.VariableReferenceList = [['_', 'Variable:/:S1']]
l.VariableReferenceList = [['_', 'Variable:/:S2']]
l.VariableReferenceList = [['_', 'Variable:/:S3']]
l.VariableReferenceList = [['_', 'Variable:/:V']]
l.LogInterval = 5e-1
l.LogEnd = duration
l.Iterations = 1

run(duration+0.1)
