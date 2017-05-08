import unittest
from recursive import *
from graph_adjacency_matrix import *


class TestRecursiveAlgorithm(unittest.TestCase):
    def test_hamiltonian_graph(self):
        path = [0, 1, 2, 3, 4, 5, 6]
        graph = Graph([
            [0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0]
        ])
        recursive = Recursive(graph)
        self.assertTrue(path, recursive.get_cycle())

    def test_not_ham_graph(self):
        graph = Graph([
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0]
        ])
        recursive = Recursive(graph)
        self.assertFalse(recursive.get_cycle())


if __name__ == '__main__':
    unittest.main()
