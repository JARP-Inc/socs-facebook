class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)

    def remove_edge(self, v1, v2):
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)

    def is_edge(self, v1, v2):
        return v2 in self.adj_list[v1]

    def get_neighbors(self, v):
        return self.adj_list[v]

    def get_vertices(self):
        return self.vertices

    def get_adj_list(self, vertice):
        return self.adj_list[vertice]
