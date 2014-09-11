#include <libecs/libecs.hpp>
#include <libecs/Model.hpp>
#include <libecs/Entity.hpp>
#include <libecs/Variable.hpp>
#include <libecs/Process.hpp>
#include <libecs/SpatiocyteCommon.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>


libecs::Variable& createVariable(libecs::Model& model,
                                 const libecs::String& fullid,
                                 const double& value)
{
  libecs::Entity& entity(*model.createEntity("Variable",
                                             libecs::FullID(fullid)));
  entity.loadProperty("Value", libecs::Polymorph(value));
  return dynamic_cast<libecs::Variable&>(entity);
}

libecs::Process& createProcess(libecs::Model& model,
                               const libecs::String& class_name,
                               const libecs::String& fullid)
{
  return dynamic_cast<libecs::Process&>(
                  *model.createEntity(class_name, libecs::FullID(fullid)));
}

libecs::System& createSystem(libecs::Model& model,
                             const libecs::String& fullid,
                             const libecs::String& stepperID)
{

  libecs::Entity& entity(*model.createEntity("System",
                                             libecs::FullID(fullid)));
  entity.loadProperty("StepperID", libecs::Polymorph(stepperID));
  return dynamic_cast<libecs::System&>(entity);
}

void run(libecs::Model& model, double aTime)
{
  double startTime(model.getCurrentTime());
  double t(startTime);
  while(t-startTime < aTime)
    { 
      model.step();
      t = model.getCurrentTime();
    }
}


int main()
{
  double T(1e-1);
  double L(1e-6);
  double N(1e+4);
  double R(2.5e-9);
  double D(1e-12);
  double stirTime(T*0.5);

  libecs::initialize();
  libecs::Model& 
    model(*(new libecs::Model(*libecs::createDefaultModuleMaker())));
  model.setup();
  libecs::Stepper& stepper(*model.createStepper("SpatiocyteStepper", "SS"));
  stepper.setProperty("VoxelRadius", libecs::Polymorph(R)); 
  stepper.setProperty("ThreadSize", libecs::Polymorph(libecs::Integer(2))); 
  model.getRootSystem()->setProperty("StepperID", libecs::Polymorph("SS"));
  createVariable(model, "Variable:/:GEOMETRY", CUBOID);
  createVariable(model, "Variable:/:LENGTHX", L);
  createVariable(model, "Variable:/:LENGTHY", L);
  createVariable(model, "Variable:/:LENGTHZ", L);
  createVariable(model, "Variable:/:XYPLANE", PERIODIC);
  createVariable(model, "Variable:/:XZPLANE", PERIODIC);
  createVariable(model, "Variable:/:YZPLANE", PERIODIC);
  createVariable(model, "Variable:/:VACANT", 0);

  createVariable(model, "Variable:/:A", N);
  createVariable(model, "Variable:/:B", 0); 
  
  /*
  libecs::Process& vis(createProcess(model, "VisualizationLogProcess",
                                     "Process:/:logger"));
  vis.registerVariableReference("_", libecs::String("Variable:/Surface:A"), 0);
  vis.registerVariableReference("_", libecs::String("Variable:/Surface:As"), 0);
  vis.loadProperty("LogInterval", libecs::Polymorph(0.01));
  */

  libecs::Process& pop(createProcess(model, "MoleculePopulateProcess",
                                     "Process:/:pop"));
  pop.registerVariableReference("_", libecs::String("Variable:/:A"), 0);

  libecs::Process& dif(createProcess(model, "DiffusionProcess",
                                     "Process:/:diffuseA"));
  dif.registerVariableReference("_", libecs::String("Variable:/:A"), 0);
  dif.loadProperty("D", libecs::Polymorph(D));

  model.initialize();
  run(model, stirTime);
  boost::posix_time::ptime start(
                 boost::posix_time::microsec_clock::universal_time());
  run(model, T);
  boost::posix_time::ptime end(
                 boost::posix_time::microsec_clock::universal_time());
  std::cout << "duration:" << end-start << std::endl;
  delete &model;
  libecs::finalize(); 
}
