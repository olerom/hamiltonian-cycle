from data import *
from recursive import *
from ore_dirac import *
from backtracking import *

print("Recursive algorithm:", (False, hamiltonian_path)[recursive(0)])

print("Algorithm for graph that satisfy ore or dirac theorems:", ore_dirac(ore_dirac_graph))

print("Backtracking algorithm:", back_tracing(graph_matrix_test, [0], 1))


