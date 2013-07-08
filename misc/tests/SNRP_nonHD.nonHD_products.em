Stepper SpatiocyteStepper(SS) { VoxelRadius 1.5e-9; }

System System(/)
{
  StepperID       SS; 
  Variable Variable(GEOMETRY)
    {
      Value 0;
    } 
  Variable Variable(LENGTHX)
    {
      Value 0.2e-6;
    } 
  Variable Variable(LENGTHY)
    {
      Value 0.2e-6;      # m
    } 
  Variable Variable(LENGTHZ)
    {
      Value 0.2e-6;      # m
    } 
  Variable Variable(XYPLANE)
    {
      Value 5;      
    }
  Variable Variable(XZPLANE)
    {
      Value 5;      
    }
  Variable Variable(YZPLANE)
    {
      Value 4;      
    }
  Variable Variable(VACANT)
    {
      Value 0; 
    } 
 }

System System(/Surface)
{
  StepperID SS;

  Variable Variable(DIMENSION)
    {
      Value 2;         # { 3: Volume
                       #   2: Surface }
    }
  Variable Variable(VACANT)
    {
      Value 0;
    }
  Variable Variable(Spectrin)
    {
      Value 0;         # molecule number
    }
  Variable Variable(freeBand3)
    {
#      Value 1;         # molecule number
      Value 0;         # molecule number
    }
  Variable Variable(Band3)
    {
      Value 0;         # molecule number
    }
  Variable Variable(Spectrin_Band3)
    {
      Value 0;         # molecule number
    }

## new

  Variable Variable(A)
    {
      Value 0;         # molecule number 
    }
  Variable Variable(C)
    {
      Value 0;         # molecule number 
    }

  Variable Variable(B)
    {
      Value 1;         # molecule number 
    }

  Variable Variable(preBand3)
    {
      Value 268;         # molecule number
      Name "HD";
    }

  Variable Variable(preSpectrin)
    {
      Value 4606;         # molecule number
      Name "HD";
    }

  Variable Variable(A_freeBand3)
    {
      Value 0;         
    }

  Process MoleculePopulateProcess(clss)
    {
      VariableReferenceList   [_ Variable:/Surface:Spectrin]
                              [_ Variable:/Surface:A]
                              [_ Variable:/Surface:freeBand3];
    }  
  Process DiffusionProcess(diff)
    {
      VariableReferenceList   [_ Variable:/Surface:Spectrin];
      D 0;
    }  
  Process DiffusionProcess(diff_freeband3)
    {
      VariableReferenceList   [_ Variable:/Surface:freeBand3];
      D 1e-13;
    }  
  Process VisualizationLogProcess(visual)
    {
      VariableReferenceList   [_ Variable:/Surface:Spectrin]
                              [_ Variable:/Surface:A]
                              [_ Variable:/Surface:B]
                              [_ Variable:/Surface:C]
                              [_ Variable:/Surface:freeBand3]
                              [_ Variable:/Surface:Spectrin_Band3];
      LogInterval 1.0e-2;
    }  

  Process ErythrocyteProcess(spec)
    {
      VariableReferenceList   [_ Variable:/Surface:A -1]
                              [_ Variable:/Surface:B];
      EdgeLength 50e-8;
    }  

  Process SpatiocyteNextReactionProcess(makespectrin)
    {
      VariableReferenceList   [_ Variable:/Surface:A           -1]
                              [_ Variable:/Surface:preSpectrin -1]
                              [_ Variable:/Surface:Spectrin     1];
      k 1e-19;        
    }

  Process SpatiocyteNextReactionProcess(removespectrin)
    {
      VariableReferenceList   [_ Variable:/Surface:B        -1]
                              [_ Variable:/Surface:Spectrin -1]
                              [_ Variable:/Surface:B         1]
                              [_ Variable:/Surface:A         1]
                              [_ Variable:/Surface:preSpectrin 1];
      k 100;        
    }
  Process SpatiocyteNextReactionProcess(removespectrinchain)
    {
      VariableReferenceList   [_ Variable:/Surface:A        -1]
                              [_ Variable:/Surface:Spectrin -1]
                              [_ Variable:/Surface:A         1]
                              [_ Variable:/Surface:A         1]
                              [_ Variable:/Surface:preSpectrin 1];
      k 100;        
    }
  Process SpatiocyteNextReactionProcess(addpectrinchain)
    {
      VariableReferenceList   [_ Variable:/Surface:A        -1]
                              [_ Variable:/Surface:Spectrin -1]
                              [_ Variable:/Surface:preSpectrin -1]
                              [_ Variable:/Surface:Spectrin  1]
                              [_ Variable:/Surface:Spectrin  1];
      k 9e-16;        
    }
}

