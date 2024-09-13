class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

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
The depth_first_search_r method is a recursive helper method for depth_first_search.

depth_first_search takes a start vertex as input. It will traverse the graph in a 
depth-first manner and record the vertices it visits in a list. That list will be returned.

It should:

    Create an empty visited list.
    Call depth_first_search_r with the empty list and the start vertex
    Return the visited array after depth_first_search_r has mutated it


depth_first_search_r takes a list of vertices that have been visited so far and a current vertex as input.

It should:

    Visit the current vertex by adding it to the visited list
    Get a sorted list of the neighbors of the current vertex using the sorted() function
    For each of those neighbors:
        If the neighboring vertex hasn't been visited yet, visit it by recursively calling depth_first_search_r with the neighboring vertex


"""