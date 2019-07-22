from vertex import Vertex

class Graph:
    """ Graph Class
    A class demonstrating the essential facts and functionalities of graphs.
    """
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_list = {}
        self.num_vertices = 0
        self.DEFAULT_WEIGHT = 1

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        self.num_vertices += 1
        self.vert_list[key] = Vertex(key)
        return self.vert_list[key]

    def get_vertex(self, key):
        """Return the vertex if it exists."""
        return self.vert_list[key]

    def add_edge(self, key1, key2, weight=None):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        if weight is None:
            weight = self.DEFAULT_WEIGHT
        if key1 not in self.vert_list:
            self.add_vertex(key1)
        if key2 not in self.vert_list:
            self.add_vertex(key2)
        self.vert_list[key1].add_neighbor(self.vert_list[key2], weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return list(self.vert_list.keys())

    def get_num_vertices(self):
        """Return the number of vertices in the graph."""
        return self.num_vertices

    def get_edges(self):
        """Return the list of edges, as tuples."""
        edges = []
        for v in self.vert_list.values():
            for w in v.neighbors:
                edges.append((v.id, w.id))
        return edges

    def get_edges_weighted(self):
        """Return the list of edges with weights, as tuples."""
        edges = []
        for v in self.vert_list.values():
            for w in v.neighbors:
                edges.append((v.id, w.id, v.neighbors[w]))
        return edges
    
    def get_num_edges(self):
        """Return the number of edges in the graph."""
        neighbor_counts = map(lambda v: len(v.neighbors), self.vert_list.values())
        return sum(neighbor_counts)

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_list.values())
