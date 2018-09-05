#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <random>
#include <cmath>
#include <chrono>

class Coordinate {
public:
  Coordinate(double x_, double y_, double z_):
    x(x_),
    y(y_),
    z(z_) {}
  double x;
  double y;
  double z;
};

double mod(double a, double m) {
  return a-m*floor(a/m);
}

int main()
{
  const double duration(10);
  const double L(1.44e-6);
  const unsigned nA(100);
  const double R(2.5e-9);
  const double D(1e-12);
  const double dt(2*R*R/3/D);
  const unsigned nSim(duration/dt);
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<> unidist(0, L);
  std::normal_distribution<> normdist(0, pow(2*D*dt,0.5));
  std::vector<Coordinate> mols;
  for (unsigned i(0); i < nA; ++i) {
    Coordinate mol(unidist(gen), unidist(gen), unidist(gen));
    mols.push_back(mol);
  }
  auto start = std::chrono::high_resolution_clock::now();
  for (unsigned n(0); n < nSim; ++n) {
    for (unsigned j(0); j < nA; ++j) {
      mols[j].x = mod(mols[j].x+normdist(gen), L);
      mols[j].y = mod(mols[j].y+normdist(gen), L);
      mols[j].z = mod(mols[j].z+normdist(gen), L);
    }
  }
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  std::cout << "elapsed:" << elapsed.count() << " s" << std::endl;
}
