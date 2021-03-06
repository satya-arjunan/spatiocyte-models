Stepper SpatiocyteStepper(SS)
{
  VoxelRadius 6e-8;
}

System System( / )
{
  StepperID       SS; 
  Variable Variable(GEOMETRY)
    {
      Value     0;   
    } 
  Variable Variable( LENGTHX )
    {
      Value     25e-6;        # in meters
    } 
  Variable Variable( LENGTHY )
    {
      Value     25e-6;        # in meters
    } 
  Variable Variable( LENGTHZ )
    {
      Value     13e-6;        # in meters
    } 
  Variable Variable( YZPLANE )
    {
      Value     5;  
    } 
  Variable Variable( XZPLANE )
    {
      Value     5; 
    } 
  Variable Variable( XYPLANE )
    {
      Value     3;
    } 
  Variable Variable( VACANT )
    {
      Value             0; 
    } 
  Process VisualizationLogProcess(loggerMean)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP2m 10050]
                            [_ Variable:/Cell/Surface:PTENm 10050]
                            [_ Variable:/Cell/Surface:PIP3m 10050]
                            [_ Variable:/Cell/Surface:PIP3a 10050]
                            [_ Variable:/Cell/Surface:PI3Km 10050]
                            [_ Variable:/Membrane:VACANT];
      LogInterval 20;
    }
#  Process MicroscopyTrackingProcess(track)
#    {
#      VariableReferenceList [_ Variable:/Cell/Surface:PIP2m 1]
#                            [_ Variable:/Cell/Surface:PTENm 1]
#                            [_ Variable:/Cell/Surface:PIP3m 1]
#                            [_ Variable:/Cell/Surface:PIP3a 1]
#                            [_ Variable:/Cell/Surface:PI3Km 1]
#                            [_ Variable:/Membrane:VACANT 1]
#                            [_ Variable:/Cell/Surface:PIP2m -1]
#                            [_ Variable:/Cell/Surface:PTENm -1]
#                            [_ Variable:/Cell/Surface:PIP3m -1]
#                            [_ Variable:/Cell/Surface:PIP3a -1]
#                            [_ Variable:/Cell/Surface:PI3Km -1]
#                            [_ Variable:/Membrane:VACANT -1];
#      ExposureTime 20;
#      LogInterval 1;
#    }
  Process CoordinateLogProcess(coord)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP2m]
                            [_ Variable:/Cell/Surface:PTENm]
                            [_ Variable:/Cell/Surface:PIP3m]
                            [_ Variable:/Cell/Surface:PIP3a]
                            [_ Variable:/Cell/Surface:PI3Km];
      LogInterval 20;
    }
  Process MoleculePopulateProcess( populate )
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP2m]
                            [_ Variable:/Cell/Surface:PIP3m]
                            [_ Variable:/Cell/Surface:PIP3a]
                            [_ Variable:/Cell/Surface:PTENm]
                            [_ Variable:/Cell/Surface:PI3Km];
    }
}

System System( /Membrane )
{
  StepperID SS;

  Variable Variable(DIMENSION)
    {
      Value 2; 
    } 
  Variable Variable(VACANT)
    {
      Value 0;
    } 
}

System System( /Cell )
{
  StepperID SS;
  Variable Variable(GEOMETRY)
    {
      Value     1;     
    } 
  Variable Variable( LENGTHX )
    {
      Value     20e-6;        # in meters
    } 
  Variable Variable( LENGTHY )
    {
      Value     20e-6;        # in meters
    } 
  Variable Variable( LENGTHZ )
    {
      Value     11e-6;        # in meters
    } 
  Variable Variable( ORIGINZ )
    {
      Value     -0.9;       
    } 
  Variable Variable( VACANT )
    {
      Value             0; 
    } 
}

System System( /Cell/Surface )
{
  StepperID SS;

  Variable Variable(DIMENSION)
    {
      Value 2;     
    } 
  Variable Variable(VACANT)
    {
      Value 1; # 1: enclosed surface
    } 
  Variable Variable(PIP2m)
    {
      Value             1233; 
    } 
  Variable Variable(PIP3m)
    {
      Value             0; 
    } 
  Variable Variable(PIP3a)
    {
      Value             0; 
    } 
  Variable Variable(PTENm)
    {
      Value             309; 
    } 
  Variable Variable(PI3Km)
    {
      Value             3096; 
    } 
  Variable Variable(PIP2)
    {
      Value             8054; 
      Name "HD";
    } 
  Variable Variable(PI3K)
    {
      Value             9264; 
      Name "HD";
    } 
  Variable Variable(PTEN)
    {
      Value             6194; 
      Name "HD";
    } 
  Process DiffusionProcess(diffusePIP2)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP2m];
      D 1e-14;
    }
  Process DiffusionProcess(diffusePIP3)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP3m];
      D 1e-14;
    }
  Process DiffusionProcess(diffusePIP3a)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PIP3a];
      D 1e-14;
    }
  Process DiffusionProcess(diffusePTEN)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PTENm];
      D 1e-14;
    }
  Process DiffusionProcess(diffusePI3K)
    {
      VariableReferenceList [_ Variable:/Cell/Surface:PI3Km];
      D 1e-14;
    }

#Membrane recruitments:
  Process SpatiocyteNextReactionProcess(recruitPIP2)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP2 -1]
                              [_ Variable:/Cell/Surface:PIP2m 1];
      k 4e-2;
    }
  Process SpatiocyteNextReactionProcess(recruitPTEN)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PTEN -1]
                              [_ Variable:/Cell/Surface:PIP2m -1]
                              [_ Variable:/Cell/Surface:PTENm 1]
                              [_ Variable:/Cell/Surface:PIP2m 1];
      k 2e-14;
    }
  Process SpatiocyteNextReactionProcess(recruitPI3Ka)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3a -1]
                              [_ Variable:/Cell/Surface:PI3K -1]
                              [_ Variable:/Cell/Surface:PIP3m 1]
                              [_ Variable:/Cell/Surface:PI3Km 1];
      k 1e-13;
    }
#Membrane recruitments end


#Activations:
  Process DiffusionInfluencedReactionProcess(dimerPIP3)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3m -1]
                              [_ Variable:/Cell/Surface:PIP3m -1]
                              [_ Variable:/Cell/Surface:PIP3a 1]
                              [_ Variable:/Cell/Surface:PIP3a 1];
      p 0.8;
    }
  Process DiffusionInfluencedReactionProcess(PIP2toPIP3)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP2m -1]
                              [_ Variable:/Cell/Surface:PI3Km -1]
                              [_ Variable:/Cell/Surface:PIP3m 1]
                              [_ Variable:/Cell/Surface:PI3Km 1];
      p 0.15;
    }



#identical dephosphorylation
  Process DiffusionInfluencedReactionProcess(PIP3toPIP2)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3m -1]
                              [_ Variable:/Cell/Surface:PTENm -1]
                              [_ Variable:/Cell/Surface:PIP2m 1]
                              [_ Variable:/Cell/Surface:PTENm 1];
      p 1;
    }
  Process DiffusionInfluencedReactionProcess(PIP3atoPIP2)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3a -1]
                              [_ Variable:/Cell/Surface:PTENm -1]
                              [_ Variable:/Cell/Surface:PIP2m 1]
                              [_ Variable:/Cell/Surface:PTENm 1];
      p 1;
    }
#identical dephosphorylation end


#Membrane dissociations:
  Process SpatiocyteNextReactionProcess(dissociatePTEN)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PTENm -1]
                              [_ Variable:/Cell/Surface:PTEN 1];
      k 0.09;
    }
  Process SpatiocyteNextReactionProcess(dissociatePI3K)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PI3Km -1]
                              [_ Variable:/Cell/Surface:PI3K 1];
      k 0.02;
    }
  Process SpatiocyteNextReactionProcess(dissociatePIP3)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3m -1]
                              [_ Variable:/Cell/Surface:PIP2 1];
      k 0.02;
    }
  Process SpatiocyteNextReactionProcess(dissociatePIP3a)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP3a -1]
                              [_ Variable:/Cell/Surface:PIP2 1];
      k 0.02;
    }
  Process SpatiocyteNextReactionProcess(dissociatePIP2)
    {
      VariableReferenceList   [_ Variable:/Cell/Surface:PIP2m -1]
                              [_ Variable:/Cell/Surface:PIP2 1];
      k 0.0001;
    }
#Membrane dissociations end

}


