class Recursive:
    def __init__(self, graph):
        self.n = len(graph)
        self.visited = [False] * self.n
        self.path = []
        self.graph = graph

    @profile
    def recursive(self, curr):
        self.path.append(curr)
        if len(self.path) == self.n:
            if self.graph.is_connected(self.path[0], self.path[-1]):
                return True
            else:
                self.path.pop()
                return False
        self.visited[curr] = True

        for i in range(self.n):
            if self.graph.is_connected(curr, i) and not self.visited[i]:
                if self.recursive(i):
                    return True
        self.visited[curr] = False
        self.path.pop()

        return False

    def get_cycle(self):
        return (False, self.path)[self.recursive(0)]

    def set_graph(self, graph):
        self.__init__(graph)
