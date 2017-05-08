import unittest
from ore_dirac import *
from graph_adjacency_matrix import *


class TestOreDiracAlgorithm(unittest.TestCase):
    def test_ore_dirac(self):
        path = [4, 1, 2, 3, 0]
        graph = Graph([
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
        ])
        ore_dirac = OreDirac(graph)
        self.assertTrue(path, ore_dirac.get_cycle())


if __name__ == '__main__':
    unittest.main()
