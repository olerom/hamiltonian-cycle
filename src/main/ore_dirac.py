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

    @staticmethod
    def reverse_sublist(lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        return lst
