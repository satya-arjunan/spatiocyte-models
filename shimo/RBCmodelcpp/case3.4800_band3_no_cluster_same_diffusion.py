##############################################################                
# band 3 cluster model (10/02)             
#  with hemi --> hemiBand3oxi (direct)--> hemiBand3phos --> hemiBand3cluster (w/ deoli)
##############################################################

import os
import sys
import string
import math
import random

vBand3    = 4800
vBand3oxi = 0
vBand3phos = 0
vBand3cluster = 0

sim = theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = 3.62e-9
theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 8.9e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:VACANT').Value = 0

theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT').Value = 0

GFP = theSimulator.createEntity('Variable', 'Variable:/Surface:GFP')
GFP.Value = 0
Band3 = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3')
Band3.Value = vBand3
Band3oxi = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3oxi')
Band3oxi.Value = vBand3oxi
Band3phos = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3phos')
Band3phos.Value = vBand3phos

#Tag 10 molecules of Band3 with GFP, to get Band3-GFP. A-GFP can transition to As-GFP:
tagger = theSimulator.createEntity('TagProcess', 'Process:/:tagger')
tagger.VariableReferenceList = [['_', 'Variable:/Surface:GFP', '-1' ]]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:Band3', '4800' ]]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:Band3cluster']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3oxi']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3phos']]
tagger.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3cluster']]

Band3cluster = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3cluster')
Band3cluster.Value = vBand3cluster

hemiBand3 = theSimulator.createEntity('Variable', 'Variable:/Surface:hemiBand3')
hemiBand3.Value = 0

hemiBand3oxi = theSimulator.createEntity('Variable', 'Variable:/Surface:hemiBand3oxi')
hemiBand3oxi.Value = 0

hemiBand3phos = theSimulator.createEntity('Variable', 'Variable:/Surface:hemiBand3phos')
hemiBand3phos.Value = 0

hemiBand3cluster = theSimulator.createEntity('Variable', 'Variable:/Surface:hemiBand3cluster')
hemiBand3cluster.Value = 0

hemi = theSimulator.createEntity('Variable', 'Variable:/:hemi')
hemi.Value = 1000
hemi.Name = "HD"

GSH = theSimulator.createEntity('Variable', 'Variable:/:GSH')
GSH.Value = 1000
GSH.Name = "HD"

GSSG = theSimulator.createEntity('Variable', 'Variable:/:GSSG')
GSSG.Value = 0
GSSG.Name = "HD"

Dia = theSimulator.createEntity('Variable', 'Variable:/:Dia')
Dia.Value = 1000
Dia.Name = "HD"

pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
pop.VariableReferenceList = [['_', 'Variable:/Surface:Band3'   ],
                             ['_', 'Variable:/Surface:Band3oxi'],
                             ['_', 'Variable:/Surface:hemiBand3'],
                             ['_', 'Variable:/Surface:hemiBand3oxi'],
                             ['_', 'Variable:/Surface:Band3phos']]

log = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:log')
log.VariableReferenceList = [['_', 'Variable:/Surface:Band3'],
                             ['_', 'Variable:/Surface:Band3oxi'],
                             ['_', 'Variable:/Surface:Band3phos'],
                             ['_', 'Variable:/Surface:hemiBand3'],
                             ['_', 'Variable:/Surface:hemiBand3oxi'],
                             ['_', 'Variable:/Surface:hemiBand3phos'],
                             ['_', 'Variable:/Surface:hemiBand3cluster'],
                             ['_', 'Variable:/Surface:Band3cluster'],
                             ['_', 'Variable:/Surface:GFP']]
log.LogInterval = 0.05

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffBand3oxi')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffhemiBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffhemiBand3oxi')
dif.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3oxi']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffBand3phos')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('PeriodicBoundaryDiffusionProcess', 'Process:/Surface:diffhemiBand3phos')
dif.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3phos']]
dif.D = 1.0e-14


#Band3oxi ok
# Band3 <-> Band3oxi
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:oxidize')
binder.VariableReferenceList = [['_', 'Variable:/:Dia',            '-1'],
                                ['_', 'Variable:/Surface:Band3',   '-1'],
                                ['_', 'Variable:/Surface:Band3oxi', '1']]
binder.k = 1e-23

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:deoxidize')
binder.VariableReferenceList = [['_', 'Variable:/:GSH',            '-2'],
                                ['_', 'Variable:/Surface:Band3oxi','-1'],
                                ['_', 'Variable:/:GSSG',            '1'],
                                ['_', 'Variable:/Surface:Band3',    '1']]
binder.k = 1e-50

# Band3oxi <-> Band3phos
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:phosphorylate')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi','-1'],
                                ['_', 'Variable:/Surface:Band3phos','1']]
binder.k = 5e-4

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dephos')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:Band3oxi',  '1']]
binder.k = 5e-3

# Band3phos <-> Band3cluster
sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleate')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 0

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:extend')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 1

# hemiBand3oxi ok
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:hemioxidize')
binder.VariableReferenceList = [['_', 'Variable:/:hemi',               '-1'],
                                ['_', 'Variable:/Surface:Band3oxi',    '-1'],
                                ['_', 'Variable:/Surface:hemiBand3oxi', '1']]
#binder.k = 1e-3
binder.k = 1e-23
 
# hemiBand3phos ok one only
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:hemiphosphorylate')
binder.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3oxi','-1'],
                                ['_', 'Variable:/Surface:hemiBand3phos','1']]
binder.k = 5e-2
#binder.k = 0

#edit this
sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:heminucleate')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3phos',   '-1'],
                                ['_', 'Variable:/Surface:hemiBand3phos',   '-1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1']]
sinker.p = 0

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:heminucleate2')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:hemiBand3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1']]
sinker.p = 0

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:hemiextend')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3phos','-1'],
                                ['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:hemiextend2')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:hemiextend3')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:hemiBand3phos','-1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster','-1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1'],
                                ['_', 'Variable:/Surface:hemiBand3cluster' ,'1']]
sinker.p = 1

iterator = theSimulator.createEntity('IteratingLogProcess', 'Process:/:iterate')
iterator.VariableReferenceList = [['_', 'Variable:/Surface:GFP']]
iterator.Iterations = 1
iterator.LogEnd = 100
iterator.LogStart = 1
iterator.LogInterval = 0.05
iterator.Diffusion = 1
iterator.FileName = "case3.4800_band3_no_cluster_same_diffusion.csv"

run(101)
