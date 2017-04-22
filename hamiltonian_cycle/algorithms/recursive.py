from data import *

n = len(graph_matrix_test)
visited = [False] * n
hamiltonian_path = []


def recursive(curr):
    hamiltonian_path.append(curr)
    if len(hamiltonian_path) == n:
        if graph_matrix_test[hamiltonian_path[0]][hamiltonian_path[-1]] == 1:
            return True
        else:
            hamiltonian_path.pop()
            return False
    visited[curr] = True

    for i in range(n):
        if graph_matrix_test[curr][i] == 1 and not visited[i]:
            if recursive(i):
                return True
    visited[curr] = False
    hamiltonian_path.pop()

    return False
