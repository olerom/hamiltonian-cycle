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
        self.assertEquals(path, recursive.get_cycle())

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

    def test_huge_simple(self):
        n = 10000
        path = []
        graph_matrix = [[]]

        for i in range(n):
            path.append(i)
            for j in range(n):
                graph_matrix[i].append(1)
            graph_matrix.append([])
        graph_matrix.remove([])

        graph = Graph(graph_matrix)
        recursive = Recursive(graph)
        self.assertEquals(path, recursive.get_cycle())


if __name__ == '__main__':
    unittest.main()
