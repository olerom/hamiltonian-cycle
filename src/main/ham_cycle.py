from recursive import *
from ore_dirac import *
from data import *

recursive = Recursive(hamiltonian_matrix)

ore_dirac = OreDirac(ore_dirac_graph)

print(ore_dirac.is_dirac())
print(ore_dirac.is_ore())

print("Recursive algorithm:", recursive.get_cycle())

print("Algorithm for graph that satisfy ore or dirac theorems:", ore_dirac.get_cycle())
