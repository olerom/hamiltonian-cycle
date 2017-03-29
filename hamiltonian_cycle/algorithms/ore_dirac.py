# Only if ore or dirac
def ore_dirac(graph):
    path = []
    n = len(graph)
    for i in range(n):
        path.append(i)

    for k in range(n * (n - 1)):
        if graph[path[0]][path[1]] != 1:
            j = 2
            while j < n and ((graph[path[0]][path[j]] != 1) or (graph[path[1]][path[j + 1]] != 1)):
                j += 1
            path = reverse_sublist(path, 1, j + 1)
        path.append(path.pop(0))
    return path


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst
