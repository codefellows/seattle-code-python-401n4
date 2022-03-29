class Graph:

    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
        v = Vertex(value)
            # Arguments: value
            # Returns: The added node
            # Add a node to the graph or add to adj list

    def add_edge(self):
        pass
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph

    def get_node(self):
        pass
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self):
        pass
            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection

    def size(self):
        pass
            # Arguments: none
            # Returns the total number of nodes in the graph


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
