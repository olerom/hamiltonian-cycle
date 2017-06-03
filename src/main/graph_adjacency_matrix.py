class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    @classmethod
    def get_full_graph(cls, n):
        graph = [[]]

        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i].append(0)
                else:
                    graph[i].append(1)
            graph.append([])
        graph.remove([])

        return cls(graph)

    def __len__(self):
        return len(self.matrix)

    def is_connected(self, vertex_from, vertex_to):
        return self.matrix[vertex_from][vertex_to] == 1
