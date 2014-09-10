import _gfrd
import model
import gfrdbase
import numpy
import myrandom
myrandom.seed(0)

L = 1e-6
D = 1e-12
radius = 2.5e-9
N = 60

# matrix_size = 3
matrix_size = max(3, int(min(numpy.power(N, 1.0 / 3.0), L / (2 * radius))))

m = model.ParticleModel(L)
A = model.Species('A', D, radius)
m.add_species_type(A)
m.set_all_repulsive()

w = gfrdbase.create_world(m, matrix_size)
gfrdbase.throw_in_particles(w, A, N)
nrw = gfrdbase.create_network_rules_wrapper(m)
sim = _gfrd._EGFRDSimulator(w, nrw, myrandom.rng)
# import egfrd
# sim = egfrd.EGFRDSimulator(w, myrandom.rng, nrw)

for _ in xrange(120):
  sim.step()
  print sim.t

for pid, p in w:
  print p.position
