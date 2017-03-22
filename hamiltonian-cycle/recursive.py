# dict way
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

# hamiltonian graph:
graph_matrix = [
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0]
]

n = len(graph_matrix)
visited = [False] * n
hamiltonian_path = []


def hamilton(curr):
    hamiltonian_path.append(curr)
    if len(hamiltonian_path) == n:
        if graph_matrix[hamiltonian_path[0]][hamiltonian_path[-1]] == 1:
            return True
        else:
            hamiltonian_path.pop()
            return False
    visited[curr] = True

    for i in range(n):
        if graph_matrix[curr][i] == 1 and not visited[i]:
            if hamilton(i):
                return True
    visited[curr] = False
    hamiltonian_path.pop()

    return False


print(hamilton(0), hamiltonian_path)
