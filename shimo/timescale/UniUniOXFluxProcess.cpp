#include "libecs.hpp"
#include "Util.hpp"
#include "PropertyInterface.hpp"

#include "System.hpp"
#include "Stepper.hpp"

#include "ContinuousProcess.hpp"

USE_LIBECS;

LIBECS_DM_CLASS( UniUniOXFluxProcess, ContinuousProcess )
{

 public:

  LIBECS_DM_OBJECT( UniUniOXFluxProcess, Process )
    {
      INHERIT_PROPERTIES( Process );

      PROPERTYSLOT_SET_GET( Real, k );
    }


  SIMPLE_SET_GET_METHOD( Real, k );


  virtual void initialize()
  {
    Process::initialize();

    S0 = getVariableReference( "S0" );
    prevTime = 0;
    prevValue = 0;
    totalInterval = 0;
    intervalCnt = 0;
  }  
  
  virtual void fire()
  {
        double currTime(getStepper()->getCurrentTime());
        if(currTime > 1000)
          { 
            double currValue(getVariableReference("S0").getValue());
            double diffValue(currValue-prevValue);
            if(diffValue*diffValue >= 
               getVariableReference("S0").getCoefficient()*
               getVariableReference("S0").getCoefficient()
               && currValue != prevValue)
              {
                double interval(currTime-prevTime);
                totalInterval += interval;
                ++intervalCnt;
                std::cout << currTime << " " << getID() << " averageInterval:"
                  << totalInterval/intervalCnt << std::endl;
                prevTime = currTime;
                prevValue = currValue;
              }
          }
        else
          {
            prevTime = currTime;
          }

    Real velocity = k * S0.getMolarConc();

    velocity = velocity * getSuperSystem()->getSize() * N_A;

    setFlux( velocity );

  }

 protected:
  double prevTime;
  double prevValue;
  double totalInterval;
  unsigned intervalCnt;

  Real k;

  VariableReference S0;

};

LIBECS_DM_INIT( UniUniOXFluxProcess, Process );
