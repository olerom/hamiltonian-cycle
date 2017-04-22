def is_safe(vertex, graph, path, position):
    if graph[path[position - 1]][vertex] == 0:
        return False

    for i in range(position):
        if path[i] == vertex:
            return False

    return True


def back_tracing(graph, path, position):
    if position == len(graph):
        if graph[path[0]][path[-1]]:
            return True
        else:
            return False

    for vertex in range(len(graph)):

        if is_safe(vertex, graph, path, position):

            # path[position] = vertex
            path.append(vertex)

            if back_tracing(graph, path, position + 1):
                return path
                # return True
            else:
                graph.remove(vertex)

    return False
