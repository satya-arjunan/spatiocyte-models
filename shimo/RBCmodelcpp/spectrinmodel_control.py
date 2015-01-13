##############################################################                # band 3 cluster model (3/6) with spectrin             
#  with hemi --> hemiBand3oxi (direct)--> hemiBand3phos --> hemiBand3cluster (w/ deoli)
##############################################################

import os
import sys
import string
import math
import random

#############################                                                  
#                                           
# define input variables                                                  
# 
#############################
log_file = "logged_variables.dat"
duration_beforediamide = 10
#duration = 21600                                                             
duration = 7200                                                             

N_A        = 6.02214e+23      # avogadro nr               
SA_actual  = 1.4e-10          # actual RBC surface area      
SA_scaled  = 1.12e-12         # scaled RBC surface area                
Vol_actual = 9.2e-17          # actual RBC volume                   
Vol_scaled = 1.05e-19         # scaled RBC volume 

vSIZE_ext = Vol_scaled * 7.0/3.0 * 1.0e+3
vMgATP    = 91472806 * Vol_scaled/Vol_actual
vMgADP    = 6900782 * Vol_scaled/Vol_actual
vPi       = 61215118.9307 * Vol_scaled/Vol_actual
vGSH      = 195606916 * Vol_scaled/Vol_actual
vGSSG     = 278134 *  Vol_scaled/Vol_actual
vDia_ext  = 0.25e-3 * 1.0e+3 * Vol_scaled * N_A * 7.0/3.0
vNADP     = 3902.83468684 * Vol_scaled/Vol_actual
vNADPH    = 3931348.80531 * Vol_scaled/Vol_actual
vE_GSSGR  = 7528.0 * Vol_scaled/Vol_actual
vG6P      = 3646419.11708 * Vol_scaled/Vol_actual
vGL6P     = 315.897268678 * Vol_scaled/Vol_actual
vGLCi     = 5.0e-3 * 1.0e+3 *Vol_scaled * N_A
vf23DPG   = 137126738.447 * Vol_scaled/Vol_actual
vGDP      = 5774287.25996 * Vol_scaled/Vol_actual
vPSH      = 43500 * Vol_scaled/Vol_actual
vBand3    = 4382 #4800-418
vBand3oxi = 0
vBand3phos = 0
vBand3cluster = 0
vHb      =  212614098 * Vol_scaled/Vol_actual
vhemi = 0

#############################                                                  
#                                           
# model main                                                  
# 
#############################
sim = theSimulator.createStepper('SpatiocyteStepper', 'SS').VoxelRadius = 3.62e-9
sim2 = theSimulator.createStepper('FixedODE1Stepper', 'DE1')

theSimulator.rootSystem.StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/:SHAPE').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 8.9e-8
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 1.06e-6
theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 5
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 4
theSimulator.createEntity('Variable', 'Variable:/:VACANT').Value = 0

SIZE_ext = theSimulator.createEntity('Variable', 'Variable:/:SIZE_ext')
SIZE_ext.Value = vSIZE_ext
SIZE_extName = "HD"

Hb = theSimulator.createEntity('Variable', 'Variable:/:Hb')
Hb.Value = vHb
Hb.Name = "HD"

hemi = theSimulator.createEntity('Variable', 'Variable:/:hemi')
hemi.Value = vhemi
hemi.Name = "HD"

MgATP = theSimulator.createEntity('Variable', 'Variable:/:MgATP')
MgATP.Value = vMgATP
MgATP.Name = "HD"

MgADP = theSimulator.createEntity('Variable', 'Variable:/:MgADP')
MgADP.Value = vMgADP
MgADP.Name = "HD"

Pi = theSimulator.createEntity('Variable', 'Variable:/:Pi')
Pi.Value = vPi
Pi.Name = "HD"

GSH = theSimulator.createEntity('Variable', 'Variable:/:GSH')
GSH.Value = vGSH
GSH.Name = "HD"

GSSG = theSimulator.createEntity('Variable', 'Variable:/:GSSG')
GSSG.Value = vGSSG
GSSG.Name = "HD"

Dia_ext = theSimulator.createEntity('Variable', 'Variable:/:Dia_ext')
Dia_ext.Value = vDia_ext
Dia_ext.Name = "HD"

Dia = theSimulator.createEntity('Variable', 'Variable:/:Dia')
Dia.Value = 0
Dia.Name = "HD"

N = theSimulator.createEntity('Variable', 'Variable:/:N')
N.Value = 0
N.Name = "HD"

NADP = theSimulator.createEntity('Variable', 'Variable:/:NADP')
NADP.Value = vNADP
NADP.Name = "HD"

NADPH = theSimulator.createEntity('Variable', 'Variable:/:NADPH')
NADPH.Value = vNADPH
NADPH.Name = "HD"

E_GSSGR = theSimulator.createEntity('Variable', 'Variable:/:E_GSSGR')
E_GSSGR.Value = vE_GSSGR
E_GSSGR.Name = "HD"

AC_GSSGR = theSimulator.createEntity('Variable', 'Variable:/:AC_GSSGR')
AC_GSSGR.Value = 1000.0
AC_GSSGR.Name = "HD"

AC_G6PDH = theSimulator.createEntity('Variable', 'Variable:/:AC_G6PDH')
AC_G6PDH.Value = 1000.0
AC_G6PDH.Name = "HD"

E_G6PDH = theSimulator.createEntity('Variable', 'Variable:/:E_G6PDH')
E_G6PDH.Value = 1.0
E_G6PDH.Name = "HD"

AC_GSSG_transport = theSimulator.createEntity('Variable', 'Variable:/:AC_GSSG_transport')
AC_GSSG_transport.Value = 1000.0
AC_GSSG_transport.Name = "HD"

E_GSSG_transport = theSimulator.createEntity('Variable', 'Variable:/:E_GSSG_transport')
E_GSSG_transport.Value = 1.0
E_GSSG_transport.Name = "HD"

G6P = theSimulator.createEntity('Variable', 'Variable:/:G6P')
G6P.Value = vG6P
G6P.Name = "HD"

GL6P = theSimulator.createEntity('Variable', 'Variable:/:GL6P')
GL6P.Value = vGL6P
GL6P.Name = "HD"

GLCi = theSimulator.createEntity('Variable', 'Variable:/:GLCi')
GLCi.Value = vGLCi
GLCi.Name = "HD"

f23DPG = theSimulator.createEntity('Variable', 'Variable:/:f23DPG')
f23DPG.Value = vf23DPG
f23DPG.Name = "HD"

pHi = theSimulator.createEntity('Variable', 'Variable:/:pHi')
pHi.Value = 7.2
pHi.Name = "HD"

GDP = theSimulator.createEntity('Variable', 'Variable:/:GDP')
GDP.Value = vGDP
GDP.Name = "HD"

PSSG = theSimulator.createEntity('Variable', 'Variable:/:PSSG')
PSSG.Value = 0
PSSG.Name = "HD"

PSH = theSimulator.createEntity('Variable', 'Variable:/:PSH')
PSH.Value = 0
PSH.Name = "HD"

###   E_GSSG_transport   ###                                     
binder = theSimulator.createEntity('GSSGtransportProcess', 'Process:/:E_GSSG_transport')          
binder.StepperID = 'DE1'                                              
binder.VariableReferenceList = [['S0', 'Variable:.:GSSG',  '-1'], 
                                ['S1', 'Variable:.:MgATP', '-1'],        
                                ['C0', 'Variable:.:E_GSSG_transport'],
                                ['E0', 'Variable:.:AC_GSSG_transport'],   
                                ['E1', 'Variable:.:MgATP'      ],       
                                ['P0', 'Variable:.:MgADP',  '1'],       
                                ['P1', 'Variable:.:Pi',     '1']]      
#binder.Vmax1      = 20.0                                                      
#binder.Vmax2      = 190.0 
binder.Vmax1      = 1.0                                                     
binder.Vmax2      = 9.5 

###   HK   ###                                                             
binder = theSimulator.createEntity('HK_Kuchel_GSH_Process', 'Process:/:E_HK')
binder.StepperID = 'DE1'
binder.VariableReferenceList = [['S1', 'Variable:.:MgATP', '-1'],
                                ['E0', 'Variable:.:pHi'        ],
                                ['E1', 'Variable:.:f23DPG'     ],
                                ['E2', 'Variable:.:GDP'        ],
                                ['E3', 'Variable:.:GSH'        ],
                                ['E4', 'Variable:.:GSSG'       ],
                                ['S0', 'Variable:.:GLCi'       ],
                                ['P0', 'Variable:.:G6P',    '1'],
                                ['P1', 'Variable:.:MgADP',  '1']]
binder.HK         = 2.5e-08
binder.K_GSSG     = 0.0
binder.KdiB23PG   = 0.0027
binder.KdiGSH     = 0.003
binder.KdiGlc16P2 = 1e-05
binder.KdiGlc6P   = 1e-05
binder.KiGlc      = 4.7e-05
binder.KiGlc6P    = 4.7e-05
binder.KiMgADP    = 0.001
binder.KiMgATP    = 0.001
binder.KmMgADP    = 0.001
binder.KmMgATP    = 0.001
binder.kcatf      = 180.0
binder.kcatr      = 1.16

###   S-glutathionylation   ###                                               
binder = theSimulator.createEntity('ExpressionFluxProcess', 'Process:/:GLU')
binder.StepperID = 'DE1'
binder.Expression = 'k * E0.MolarConc * S0.MolarConc * self.getSuperSystem().SizeN_A'
binder.VariableReferenceList = [['S0', 'Variable:.:GSH',  '-1'],
                                ['S1', 'Variable:.:PSH',  '-1'],
                                ['E0', 'Variable:.:Dia'       ],
                                ['P0', 'Variable:.:PSSG',  '1']]
binder.k = 450

###   S-glutathionylation reverse   ###                                       
binder = theSimulator.createEntity('ExpressionFluxProcess', 'Process:/:GLU_rev')
binder.StepperID = 'DE1'
binder.Expression = 'k * S0.MolarConc * S1.MolarConc *self.getSuperSystem().SizeN_A'
binder.VariableReferenceList = [['S0', 'Variable:.:PSSG','-1'],
                                ['S1', 'Variable:.:GSH', '-1'],
                                ['P0', 'Variable:.:PSH',  '1'],
                                ['P1', 'Variable:.:GSSG', '1']]
binder.k = 0.15

###   GSH oxidation reaction   ###                                           
binder = theSimulator.createEntity('UniUniOXFluxProcess', 'Process:/:OX')
binder.StepperID = 'DE1'
binder.VariableReferenceList = [['S0', 'Variable:.:GSH','-2' ],
                                ['P0', 'Variable:.:GSSG', '1']]
binder.k = 2.38e-05

###   G6PDH   ###                                                         
binder = theSimulator.createEntity('G6PDHak_GSH_Process', 'Process:/:E_G6PDH')
binder.StepperID = 'DE1'
binder.VariableReferenceList = [['S0', 'Variable:.:NADP', '-1'],
                                ['S1', 'Variable:.:G6P'        ],
                                ['C0', 'Variable:.:E_G6PDH'    ],
                                ['E0', 'Variable:.:AC_G6PDH'   ],
                                ['E1', 'Variable:.:MgATP'      ],
                                ['E2', 'Variable:.:f23DPG'     ],
                                ['E3', 'Variable:.:GSH'        ],
                                ['E4', 'Variable:.:GSSG'       ],
                                ['P0', 'Variable:.:GL6P'       ],
                                ['P1', 'Variable:.:NADPH',  '1']]
binder.K_ATP   = 749.0
binder.K_DPG   = 2289.0
binder.K_G6P   = 66.7
binder.K_GSSG  = 0.0
binder.K_NADP  = 3.67
binder.K_NADPH = 3.12
binder.Vm      = 64.0

###   Diamide permeation   ###                                    
binder = theSimulator.createEntity('ExpressionFluxProcess', 'Process:/:DIA_PER')
binder.StepperID = 'DE1'
binder.Expression = 'k * S0.MolarConc * 3.0/7.0 * N_A * E0.Value * E1.Value'
binder.VariableReferenceList = [['S0', 'Variable:.:Dia_ext','-1'],
                                ['S1', 'Variable:.:Dia',     '1'],
                                ['E0', 'Variable:.:SIZE_ext'    ],
                                ['E1', 'Variable:.:N'           ]]
binder.k = 1.27e-3

###   GSSGR   ###                                                                                            
binder = theSimulator.createEntity('GSSGRProcess', 'Process:/:GSSGR')
binder.StepperID = 'DE1'
binder.VariableReferenceList = [['S0', 'Variable:.:NADPH', '-1'],
                                ['S1', 'Variable:.:GSSG',  '-1'],
                                ['C0', 'Variable:.:E_GSSGR'    ],
                                ['E0', 'Variable:.:AC_GSSGR'   ],
                                ['P1', 'Variable:.:NADP',   '1'],
                                ['P0', 'Variable:.:GSH',    '2']]
binder.k1  = 85000000.0
binder.k10 = 50000000.0
binder.k11 = 7000.0
binder.k12 = 100000000.0
binder.k2  = 510.0
binder.k3  = 100000000.0
binder.k4  = 560000.0
binder.k5  = 810.0
binder.k6  = 1000.0;
binder.k7  = 1000000.0;
binder.k8  = 50000000.0;
binder.k9  = 1000000.0;

###   Diamide reduction   ###                                         
binder = theSimulator.createEntity('MassActionFluxProcess', 'Process:/:E_DIA')
binder.StepperID = 'DE1'
binder.VariableReferenceList = [['_', 'Variable:.:Dia', '-1'],
                                ['_', 'Variable:.:GSH', '-2'],
                                ['_', 'Variable:.:GSSG', '1']]
binder.k = 300.0

############################                         
#                                                                    
# model surface                                                            
#                                                            
############################                                                             
theSimulator.createEntity('System', 'System:/:Surface').StepperID = 'SS'
theSimulator.createEntity('Variable', 'Variable:/Surface:DIMENSION').Value = 2
theSimulator.createEntity('Variable', 'Variable:/Surface:VACANT').Value = 0

Band3 = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3')
Band3.Value = vBand3

Band3oxi = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3oxi')
Band3oxi.Value = vBand3oxi

Band3phos = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3phos')
Band3phos.Value = vBand3phos

Band3cluster = theSimulator.createEntity('Variable', 'Variable:/Surface:Band3cluster')
Band3cluster.Value = vBand3cluster

theSimulator.createEntity('Variable', 'Variable:/Surface:Edge').Value = 0

theSimulator.createEntity('Variable', 'Variable:/Surface:Vertex').Value = 0

### NEW ####
Spectrin = theSimulator.createEntity('Variable', 'Variable:/Surface:Spectrin')
Spectrin.Value = 4454

BoundBand3 = theSimulator.createEntity('Variable', 'Variable:/Surface:BoundBand3')
BoundBand3.Value = 418

BoundBand3oxi = theSimulator.createEntity('Variable', 'Variable:/Surface:BoundBand3oxi')
BoundBand3oxi.Value = 0

BoundBand3phos = theSimulator.createEntity('Variable', 'Variable:/Surface:BoundBand3phos')
BoundBand3phos.Value = 0

Spectrin_Band3 = theSimulator.createEntity('Variable', 'Variable:/Surface:Spectrin_Band3')
Spectrin_Band3.Value = 0

Spectrin_Band3oxi = theSimulator.createEntity('Variable', 'Variable:/Surface:Spectrin_Band3oxi')
Spectrin_Band3oxi.Value = 0

Spectrin_Band3phos = theSimulator.createEntity('Variable', 'Variable:/Surface:Spectrin_Band3phos')
Spectrin_Band3phos.Value = 0

V_Band3  = theSimulator.createEntity('Variable', 'Variable:/Surface:V_Band3')
V_Band3.Value = 0

E_Band3  = theSimulator.createEntity('Variable', 'Variable:/Surface:E_Band3')
E_Band3.Value = 0

V_Band3oxi  = theSimulator.createEntity('Variable', 'Variable:/Surface:V_Band3oxi')
V_Band3oxi.Value = 0

E_Band3oxi  = theSimulator.createEntity('Variable', 'Variable:/Surface:E_Band3oxi')
E_Band3oxi.Value = 0

V_Band3phos  = theSimulator.createEntity('Variable', 'Variable:/Surface:V_Band3phos')
V_Band3phos.Value = 0

E_Band3phos  = theSimulator.createEntity('Variable', 'Variable:/Surface:E_Band3phos')
E_Band3phos.Value = 0

V_Band3cluster  = theSimulator.createEntity('Variable', 'Variable:/Surface:V_Band3cluster')
V_Band3cluster.Value = 0

E_Band3cluster  = theSimulator.createEntity('Variable', 'Variable:/Surface:E_Band3cluster')
E_Band3cluster.Value = 0

pop = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
pop.VariableReferenceList = [['_', 'Variable:/Surface:Band3'   ],
                             ['_', 'Variable:/Surface:V_Band3'],                             
                             ['_', 'Variable:/Surface:E_Band3'],
                             ['_', 'Variable:/Surface:V_Band3oxi'],                             
                             ['_', 'Variable:/Surface:E_Band3oxi'],
                             ['_', 'Variable:/Surface:V_Band3phos'],                             
                             ['_', 'Variable:/Surface:E_Band3phos'],
                             ['_', 'Variable:/Surface:V_Band3cluster'],                             
                             ['_', 'Variable:/Surface:E_Band3cluster'],
                             ['_', 'Variable:/Surface:Band3oxi'],
                             ['_', 'Variable:/Surface:BoundBand3'],
                             ['_', 'Variable:/Surface:BoundBand3oxi'],
                             ['_', 'Variable:/Surface:BoundBand3phos'],
                             ['_', 'Variable:/Surface:Spectrin'],
                             ['_', 'Variable:/Surface:Spectrin_Band3'],
                             ['_', 'Variable:/Surface:Spectrin_Band3oxi'],
                             ['_', 'Variable:/Surface:Spectrin_Band3phos'],
                             ['_', 'Variable:/Surface:Band3phos']]

log = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:log')
log.VariableReferenceList = [['_', 'Variable:/Surface:Band3'],
                             ['_', 'Variable:/Surface:Spectrin'],
                             ['_', 'Variable:/Surface:V_Band3'],
                             ['_', 'Variable:/Surface:E_Band3'],
                             ['_', 'Variable:/Surface:V_Band3oxi'],                             
                             ['_', 'Variable:/Surface:E_Band3oxi'],
                             ['_', 'Variable:/Surface:V_Band3phos'],                             
                             ['_', 'Variable:/Surface:E_Band3phos'],
                             ['_', 'Variable:/Surface:V_Band3cluster'],                             
                             ['_', 'Variable:/Surface:E_Band3cluster'],
                             ['_', 'Variable:/Surface:BoundBand3'],
                             ['_', 'Variable:/Surface:BoundBand3oxi'],
                             ['_', 'Variable:/Surface:BoundBand3phos'],
                             ['_', 'Variable:/Surface:Spectrin_Band3'],
                             ['_', 'Variable:/Surface:Spectrin_Band3oxi'],
                             ['_', 'Variable:/Surface:Spectrin_Band3phos'],
                             ['_', 'Variable:/Surface:Band3oxi'],
                             ['_', 'Variable:/Surface:Band3phos'],
                             ['_', 'Variable:/Surface:Band3cluster']]
log.LogInterval = 10

log = theSimulator.createEntity('CoordinateLogProcess', 'Process:/:clog')
log.VariableReferenceList = [['_', 'Variable:/Surface:Band3'],
                             ['_', 'Variable:/Surface:Spectrin'],
                             ['_', 'Variable:/Surface:V_Band3'],
                             ['_', 'Variable:/Surface:E_Band3'],
                             ['_', 'Variable:/Surface:V_Band3oxi'],                             
                             ['_', 'Variable:/Surface:E_Band3oxi'],
                             ['_', 'Variable:/Surface:V_Band3phos'],                             
                             ['_', 'Variable:/Surface:E_Band3phos'],
                             ['_', 'Variable:/Surface:V_Band3cluster'],                             
                             ['_', 'Variable:/Surface:E_Band3cluster'],
                             ['_', 'Variable:/Surface:BoundBand3'],
                             ['_', 'Variable:/Surface:BoundBand3oxi'],
                             ['_', 'Variable:/Surface:BoundBand3phos'],
                             ['_', 'Variable:/Surface:Spectrin_Band3'],
                             ['_', 'Variable:/Surface:Spectrin_Band3oxi'],
                             ['_', 'Variable:/Surface:Spectrin_Band3phos'],
                             ['_', 'Variable:/Surface:Band3oxi'],
                             ['_', 'Variable:/Surface:Band3phos'],
                             ['_', 'Variable:/Surface:Band3cluster']]
log.LogInterval = 10

separator = theSimulator.createEntity('ErythrocyteProcess', 'Process:/Surface:separ')
separator.VariableReferenceList = [['_', 'Variable:/Surface:Edge', '-1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:Vertex', '-2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3oxi', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3cluster', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3oxi', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3phos', '1']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3oxi','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3cluster','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3oxi','2']]
separator.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3phos','2']]
#separator.EdgeLength = 120e-9 #40e-9                                            
separator.EdgeLength = 100e-9 #40e-9                                            
# #diffuse on spectrin                                                           
# diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diff_Spectrinband3')
# diffuser.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3']]
# diffuser.D = 1e-13

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/Surface:diffBand3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/Surface:diffBand3oxi')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi']]
dif.D = 1.0e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/Surface:diffBand3phos')
dif.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos']]
dif.D = 1.0e-12

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffV_Band3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffE_Band3')
dif.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffV_Band3oxi')
dif.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3oxi']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffE_Band3oxi')
dif.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3oxi']]
dif.D = 1e-14

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffV_Band3phos')
dif.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos']]
dif.D = 1e-12

dif = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffE_Band3phos')
dif.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos']]
dif.D = 1e-12

#################
### reactions ###
#################

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

######################
# cluster nucleation #
######################

# Band3phos <-> Band3cluster
sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleate')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 0.1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleateEandnorm')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 0.1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleateEandE')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1']]
sinker.p = 0.1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleateVandnorm')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 0.1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleateVandV')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1']]
sinker.p = 0.1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:nucleateEandV')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1']]
sinker.p = 0.1


#####################
# cluster extension #
#####################

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:extend')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:extend2')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Vextend2')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Eextend3')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos','-1'],
                                ['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Eextend4')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Eextend5')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Vextend3')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','-1'],
                                ['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Vextend4')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','-1'],
                                ['_', 'Variable:/Surface:E_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:E_Band3cluster' ,'1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:Vextend5')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1'],
                                ['_', 'Variable:/Surface:V_Band3cluster' ,'1']]
sinker.p = 1


binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:decluster')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3cluster','-1'],
                                ['_', 'Variable:/Surface:Band3phos',    '1']]
binder.Deoligomerize = 6
binder.Rates = [1024, 256, 64, 16, 4, 1]
#binder.Rates = [32, 16, 8, 4, 2, 1]


binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:declusterV')
binder.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:V_Band3phos',    '1']]
binder.Deoligomerize = 6
binder.Rates = [1024, 256, 64, 16, 4, 1]
#binder.Rates = [32, 16, 8, 4, 2, 1]

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:declusterE')
binder.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3cluster','-1'],
                                ['_', 'Variable:/Surface:E_Band3phos',    '1']]
binder.Deoligomerize = 6
#binder.Rates = [32, 16, 8, 4, 2, 1]
binder.Rates = [1024, 256, 64, 16, 4, 1]


###############################                                     
##    Bound band 3 changes   ##                                 
############################### 
# oxidation (remove BoundBand3)
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:oxidizeboundband3')
binder.VariableReferenceList = [['_', 'Variable:/:Dia',            '-1'],
                                ['_', 'Variable:/Surface:BoundBand3', '-1'],
                                ['_', 'Variable:/Surface:BoundBand3oxi', '1']]
binder.k = 1e-23

# deoxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:deoxidizebound')
binder.VariableReferenceList = [['_', 'Variable:/:GSH',            '-2'],
                                ['_', 'Variable:/Surface:BoundBand3oxi','-1'],
                                ['_', 'Variable:/:GSSG',            '1'],
                                ['_', 'Variable:/Surface:BoundBand3',    '1']]
binder.k = 1e-50

## remove spectrin                                                                                                           
dis = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:removeSpectrin')
dis.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin', '-1']]
dis.VariableReferenceList = [['_', 'Variable:/Surface:Vertex', '-1']]
dis.VariableReferenceList = [['_', 'Variable:/Surface:Edge', '1']]
dis.k = 0.01
#dis.k = kkk

dis = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:removeSpectrinEdge')
dis.VariableReferenceList = [['_', 'Variable:/Surface:Edge', '-1']]
dis.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin', '-1']]
dis.VariableReferenceList = [['_', 'Variable:/Surface:Edge', '1']]
dis.k = 0.0001
#dis.k = iii

# phosphorylation/dephosphorylation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:phosphorylateboundband3phos')
binder.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3oxi','-1'],
                                ['_', 'Variable:/Surface:BoundBand3phos','1']]
binder.k = 5e-4

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dephosboundBand3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3phos','-1'],
                                ['_', 'Variable:/Surface:BoundBand3oxi',  '1']]
binder.k = 5e-3

## key reaction
sinker = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:BoundBand3phoswalkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:BoundBand3phos','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '1'],
                                ['_', 'Variable:/Surface:Band3phos' ,  '1']]
sinker.k = 10


#####################################                                     
##   changes in spectrin bound   ##                                 
##################################### 
# oxidation (remove BoundBand3)
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:oxidizeSpectrin_band3')
binder.VariableReferenceList = [['_', 'Variable:/:Dia',            '-1'],
                                ['_', 'Variable:/Surface:Spectrin_Band3', '-1'],
                                ['_', 'Variable:/Surface:Spectrin_Band3oxi', '1']]
binder.k = 1e-23

# deoxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:deoxidizeSpectrin_band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/:GSH',            '-2'],
                                ['_', 'Variable:/Surface:Spectrin_Band3oxi','-1'],
                                ['_', 'Variable:/:GSSG',            '1'],
                                ['_', 'Variable:/Surface:Spectrin_Band3',    '1']]
binder.k = 1e-50

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:phosSpectrin_Band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3oxi','-1'],
                                ['_', 'Variable:/Surface:Spectrin_Band3phos','1']]
binder.k = 5e-4

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dephosSpectrin_Band3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3phos','-1'],
                                ['_', 'Variable:/Surface:Spectrin_Band3oxi',  '1']]
binder.k = 5e-3


#####################################                                     
##  changes in E_, V_ species   ##                                 
##################################### 
# oxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:oxidizeE_band3')
binder.VariableReferenceList = [['_', 'Variable:/:Dia',            '-1'],
                                ['_', 'Variable:/Surface:E_Band3', '-1'],
                                ['_', 'Variable:/Surface:E_Band3oxi', '1']]
binder.k = 1e-23

# deoxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:deoxidizeE_band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/:GSH',            '-2'],
                                ['_', 'Variable:/Surface:E_Band3oxi','-1'],
                                ['_', 'Variable:/:GSSG',            '1'],
                                ['_', 'Variable:/Surface:E_Band3',    '1']]
binder.k = 1e-50

# oxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:oxidizeV_band3')
binder.VariableReferenceList = [['_', 'Variable:/:Dia',            '-1'],
                                ['_', 'Variable:/Surface:V_Band3', '-1'],
                                ['_', 'Variable:/Surface:V_Band3oxi', '1']]
binder.k = 1e-23

# deoxidation
binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:deoxidizeV_band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/:GSH',            '-2'],
                                ['_', 'Variable:/Surface:V_Band3oxi','-1'],
                                ['_', 'Variable:/:GSSG',            '1'],
                                ['_', 'Variable:/Surface:V_Band3',    '1']]
binder.k = 1e-50

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:phosE_Band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3oxi','-1'],
                                ['_', 'Variable:/Surface:E_Band3phos','1']]
binder.k = 5e-4

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dephosE_Band3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos','-1'],
                                ['_', 'Variable:/Surface:E_Band3oxi',  '1']]
binder.k = 5e-3

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:phosV_Band3oxi')
binder.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3oxi','-1'],
                                ['_', 'Variable:/Surface:V_Band3phos','1']]
binder.k = 5e-4

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/Surface:dephosV_Band3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','-1'],
                                ['_', 'Variable:/Surface:V_Band3oxi',  '1']]
binder.k = 5e-3



#####################################                                     
##   free diff over vertex/edge   ##                                 
##################################### 
sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3bind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Vertex',      '-1'],
                                ['_', 'Variable:/Surface:Band3',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3walkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3' ,  '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3bind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Edge',      '-1'],
                                ['_', 'Variable:/Surface:Band3',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3walkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3' ,  '1']]
sinker.p = 1

###

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3oxibind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Vertex',      '-1'],
                                ['_', 'Variable:/Surface:Band3oxi',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3oxi' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3oxiwalkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3oxi','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3oxi' ,  '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3oxibind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Edge',      '-1'],
                                ['_', 'Variable:/Surface:Band3oxi',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3oxi' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3oxiwalkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3oxi','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3oxi' ,  '1']]
sinker.p = 1

###

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3phosbind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Vertex',      '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:V_Band3phos' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:V_Band3phoswalkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:V_Band3phos','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3phos' ,  '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3phosbind')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:Edge',      '-1'],
                                ['_', 'Variable:/Surface:Band3phos',   '-1'],
                                ['_', 'Variable:/Surface:E_Band3phos' , '1']]
sinker.p = 1

sinker = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/Surface:E_Band3phoswalkoff')
sinker.VariableReferenceList = [['_', 'Variable:/Surface:E_Band3phos','-1'],
                                ['_', 'Variable:/Surface:VACANT' , '-1'],
                                ['_', 'Variable:/Surface:Band3phos' ,  '1']]
sinker.p = 1


###############################                                     
##    hop-over spectrin    ##                                 
############################### 

#freely diffusing Band3 hops over
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:hopreaction1')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3',    '-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',     '-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3','1']]
binder.p = 0.008
#binder.p = 0.5

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:hopreaction2')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',       '1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3',      '1']]
binder.k = 100000

#Band3oxi hops over
binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:hopreaction3')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi',    '-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',     '-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3oxi','1']]
binder.p = 0.008
#binder.p = 0.5

binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:hopreaction4')
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3oxi','-1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',       '1']]
binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3oxi',      '1']]
binder.k = 100000

# #Band3phos hops over
# binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:hopreaction5')
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos',    '-1']]
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',     '-1']]
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3phos','1']]
# binder.p = 0.008
# #binder.p = 0.5

# binder = theSimulator.createEntity('SpatiocyteNextReactionProcess', 'Process:/:hopreaction6')
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin_Band3phos','-1']]
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Spectrin',       '1']]
# binder.VariableReferenceList = [['_', 'Variable:/Surface:Band3phos',      '1']]
# binder.k = 100000


############################                                      
#                                                                   
# run model                                             
#                                         
############################    
with open(log_file, 'w') as output :
    output.write('#time\tGSH(value)\tDia(value)\tBand3\ttotaloxi\ttotalphos\ttotalcluster\tBand3hemiphos')
    output.write('\n')

# initial                                                              
with open(log_file, 'a') as output :

    output.write(str((getCurrentTime())/60) + '\t' +
                 str(((GSH.Value)/(Vol_scaled*N_A))*1)        + '\t' +   # conc=value/(vol*N_A), litre->m^3                                         
                 str(((Dia.Value)/(Vol_scaled*N_A))*1)        + '\t' +
                 str(((Dia_ext.Value)/(Vol_scaled*N_A))*1)        + '\t' +
                 str(((hemi.Value)/(Vol_scaled*N_A))*1)       + '\t' +
#                 str(((Band3.Value)/4800)*100)      + '\t' +
                 str((((Band3.Value) + (E_Band3.Value) + (BoundBand3.Value) + (V_Band3.Value) + (Spectrin_Band3.Value))/4800)*100)      + '\t' +
#                 str(((Band3oxi.Value)/4800)*100)   + '\t' +
                 str((((Band3oxi.Value) + (E_Band3oxi.Value) + (BoundBand3oxi.Value) + (V_Band3oxi.Value) + (Spectrin_Band3oxi.Value))/4800)*100)      + '\t' +
#                 str(((Band3phos.Value)/4800)*100)   + '\t' +
                 str((((Band3phos.Value) + (E_Band3phos.Value) + (V_Band3phos.Value) + (Spectrin_Band3phos.Value) + (BoundBand3phos.Value))/4800)*100)      + '\t' +
#                 str(((Band3cluster.Value)/4800)*100)   + '\t' +
                 str((((Band3cluster.Value) + (E_Band3cluster.Value) + (V_Band3cluster.Value))/4800)*100)      + '\t\n' )


                 # str(((hemiBand3cluster.Value)/4800)*100)  + '\t' +
                 # str((((Band3oxi.Value) + (Band3phos.Value) + (Band3cluster.Value) + (hemiBand3phos.Value) + (hemiBand3cluster.Value))/4800)*100) + '\t' +
                 # str((((Band3phos.Value) + (Band3cluster.Value) + (hemiBand3phos.Value) + (hemiBand3cluster.Value))/4800)*100) + '\t' +
                 # str((((Band3cluster.Value) + (hemiBand3cluster.Value))/4800)*100) + '\t\n' )

# running the simulation (before diamide input)                                
while getCurrentTime() < duration_beforediamide :
    run(1)

theSimulator.setEntityProperty( "Variable:/:N:Value", 1)

while getCurrentTime() < duration + duration_beforediamide :
    run(1)
    with open(log_file, 'a') as output :
        output.write(str((getCurrentTime() - duration_beforediamide)/60) + '\t' +
                     str(((GSH.Value)/(Vol_scaled*N_A))*1)        + '\t' +   # conc=value/(vol*N_A), litre->m^3                                      
                     str(((Dia.Value)/(Vol_scaled*N_A))*1)        + '\t' +
                     str(((Dia_ext.Value)/(Vol_scaled*N_A))*1)        + '\t' +
                     str(((hemi.Value)/(Vol_scaled*N_A))*1)       + '\t' +
                     str((((Band3.Value) + (E_Band3.Value) + (BoundBand3.Value) + (V_Band3.Value) + (Spectrin_Band3.Value))/4800)*100)      + '\t' +
                     str((((Band3oxi.Value) + (E_Band3oxi.Value) + (BoundBand3oxi.Value) + (V_Band3oxi.Value) + (Spectrin_Band3oxi.Value))/4800)*100)      + '\t' +
                     str((((Band3phos.Value) + (E_Band3phos.Value) + (V_Band3phos.Value) + (Spectrin_Band3phos.Value)+ (BoundBand3phos.Value))/4800)*100)      + '\t' +
                     str((((Band3cluster.Value) + (E_Band3cluster.Value) + (V_Band3cluster.Value))/4800)*100)      + '\t\n' )


#                      str(GSH.Value)        + '\t' +
#                      str(Dia.Value)        + '\t' +
#                      str(Band3.Value)      + '\t' +
#                      str((Band3oxi.Value) + (hemiBand3oxi.Value) + (Band3phos.Value) + (Band3cluster.Value) + (hemiBand3phos.Value) + (hemiBand3cluster.Value))   + '\t' +
#                      str((Band3phos.Value) + (Band3cluster.Value) + (hemiBand3cluster.Value) + (hemiBand3phos.Value))  + '\t' +
# #                     str((Band3cluster.Value) + (hemiBand3cluster.Value))    + '\t' + 
#                      str((Band3cluster.Value) + (hemiBand3cluster.Value) + (BoundBand3cluster.Value) + (BoundhemiBand3cluster.Value))    + '\t' + 
#                      str(hemiBand3phos.Value)   + '\t\n' ) 
print "simulation is finished!"
