class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)

################## Below CONTEXT code #################

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

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


################## Below Pseudo code #################
"""
note that we're using unique strings instead of integers for our vertices here.

breadth_first_search takes a starting vertex as input. It will traverse the entire graph in a 
breadth-first manner and record the vertices it visits in a list. That list will be returned.

It should:

    Create an empty visited list.
    Create an empty to_visit list.
    Queue up the start vertex by adding it to the to_visit list.
    While to_visit is not empty:
        Remove the first vertex off the to_visit list with pop and visit it by appending it to visited.
        Get a sorted() list of the neighbors of the vertex we just visited.
        For each sorted neighbor:
            If the neighbor hasn't been visited and it isn't already queued up to be visited:
                Queue up the neighbor by adding it to the to_visit loop.
    Once to_visit is empty, we've traversed the whole graph so just return visited.


"""