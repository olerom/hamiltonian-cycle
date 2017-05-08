class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def __len__(self):
        return len(self.matrix)

    def is_connected(self, vertex_from, vertex_to):
        return self.matrix[vertex_from][vertex_to] == 1
