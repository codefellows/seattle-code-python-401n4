class Graph:

    def __init__(self):
        self.adjacency_list={}
        # 'seattle' ->(200) 'Los Angels'
        # 'seattle' ->(220) 'Denver'
        # 'seattle' ->(100) 'Spokane'
        # self.adjacency_list['seattle'] -> [('Los Angeles',200), ('Denver', 220), ('Spokane', 100)]



    def add_node(self):
        pass
            # Arguments: value
            # Returns: The added node
            # Add a node to the graph

    def add_edge(self, start_node, end_node, weight=0):
        pass
            # Check if the start and end nodes are in the adjancency list.
                # if no, raise an exception.
                # if yes
                    # instanciate an edge (end_node, weight)
                # self.adjacency_list[start_node].append(edge)
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
            # len(self.adjacency_list)-



class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
