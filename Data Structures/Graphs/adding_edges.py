class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

################## Below CONTEXT code #################

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

################## Below Pseudo code #################
"""
Create a new data member called graph, it should be an empty list. Fill the list with n lists, where n is the number of vertices in the graph. Each of these lists should contain n False values.
add_edge(self, u, v)

add_edge takes two vertices as inputs, and should add an edge to the graph by setting the corresponding cells to True.

There are two cells in the matrix for each pair of vertices. For example, (2, 3) corresponds to these cells:

"""