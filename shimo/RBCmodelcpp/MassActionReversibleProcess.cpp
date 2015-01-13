#include "libecs.hpp"
#include "Util.hpp"
#include "PropertyInterface.hpp"

#include "System.hpp"

#include "ContinuousProcess.hpp"

USE_LIBECS;

LIBECS_DM_CLASS( MassActionReversibleProcess, ContinuousProcess )
{

 public:

  LIBECS_DM_OBJECT( MassActionReversibleProcess, Process )
    {
      INHERIT_PROPERTIES( Process );

      PROPERTYSLOT_SET_GET( Real, Kma );
      PROPERTYSLOT_SET_GET( Real, Kmd );
    }

  SIMPLE_SET_GET_METHOD( Real, Kma );
  SIMPLE_SET_GET_METHOD( Real, Kmd );

  virtual void initialize()
  {
    Process::initialize();

    S0 = getVariableReference( "S0" );
    P0 = getVariableReference( "P0" );

  }  
  
  virtual void fire()
  {

    Real velocity = Kma * S0.getMolarConc() -
      Kmd * P0.getMolarConc();

    velocity = velocity * getSuperSystem()->getSize() * N_A;

    setFlux( velocity );

  }

 protected:

  VariableReference S0;
  VariableReference P0;

  Real Kma;
  Real Kmd;

};

LIBECS_DM_INIT( MassActionReversibleProcess, Process );
