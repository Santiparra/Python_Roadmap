class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

################## Below CONTEXT code #################

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

################## Below Pseudo code #################
"""
The constructor should create an empty dictionary called graph as a data member.

add_edge takes two vertices as inputs, and should add an edge to the adjacency list (the dictionary).

The dictionary maps vertices to a set of all other vertices they share an edge with. 

Use these steps:

    If vertex u is already a key in the dictionary, add v to u's set.
    Otherwise, create a new set for u that contains v.
    Repeat steps 1 & 2, but swap u and v.


"""