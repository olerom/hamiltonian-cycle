class OreDirac:
    def __init__(self, graph):
        self.graph = graph

    def set_graph(self, graph):
        self.graph = graph

    def get_cycle(self):
        path = []
        n = len(self.graph)
        for i in range(n):
            path.append(i)

        for k in range(n * (n - 1)):
            if not self.graph.is_connected(path[0], path[1]):
                j = 2

                while (j < n) and (not self.graph.is_connected(path[0], path[j])) \
                        or (not self.graph.is_connected(path[1], path[j + 1])):
                    j += 1
                path = self.reverse_sublist(path, 1, j + 1)
            path.append(path.pop(0))
        return path

    def is_dirac(self):
        n = len(self.graph)
        if n < 3:
            return False

        for i in range(n):
            counter = 0

            for j in range(n):
                if self.graph.is_connected(i, j):
                    counter += 1

            if counter < n / 2:
                return False

        return True

    def is_ore(self):
        n = len(self.graph)
        if n < 3:
            return False

        edges = []
        for i in range(n):
            for j in range(n):
                edges.append([i, j])

        vertex_deg = {}

        for i in range(n):
            counter = 0
            for j in range(n):
                if self.graph.is_connected(i, j):
                    edges.remove([i, j])
                    counter += 1

            vertex_deg.update({i: counter})

        for edge in edges:
            if vertex_deg.get(edge[0]) + vertex_deg.get(edge[1]) < n:
                return False

        return True

    @staticmethod
    def reverse_sublist(lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        return lst
