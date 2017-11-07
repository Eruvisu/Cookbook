"""Classes for graph representation.
Comparison:
Adjacency Matrix - Makes sense for small, densely connected graphs. Efficient on space when there
                    are many edges to represent in a graph.

Adjacency List/Set - Useful for large, sparsely connected graphs; saves on storage space.
"""

import abc
import numpy as np


class Graph(abc.ABC):
    """Description: Abstract base class to represent a graph
        with all the interface methods."""

    def __init__(self, numVertices, directed=False):
        """Args:
            numVertices: Total number of vertices of the graph.
                Every vertex has a unique vertex ID ranging from 0 to numVertices-1.
            directed: True if it's a directed graph, False if it's undirected
        """
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        """Description: Add edges to the graph.
        Args:
            v1,v2: The two nodes connected by this edge
            weight: The weight of the edge
        """
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        """Description: Get all adjacent vertices for any specified vertex ''v''.
        Args:
            v: The vertex for which to retrieve al adjacent vertexes.

        Returns: A list with all the adjacent vertices of vertex ''v''.
        """
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        """Description: Get the number of edges that are incident on a node
                        and flow into that node in a directed graph.
        Args:
            v: A vertex for which to find the indegree.

        Returns: The indegree of the node ''v''.
        """
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        """Description: Get the weight of the edge connecting 2 vertices.

        Args:
            v1,v2: The vertices for which to find the weight of the edge
                    connecting them.
        Returns: The weight of the edge connecting vertices ''v1'' and ''v2''.
        """
        pass

    @abc.abstractmethod
    def display(self):
        """Description: Prints the graph. Serves as a debugging aid.
        """
        pass


class AdjacencyMatrixGraph(Graph):
    """Class to represent a graph as an adjacency matrix. A cell in the
        matrix has a value when there exists an edge between the vertex
        represented by the row and column numbers.
        Weighted graphs can hold values > 1 in the matrix cells.
        A value of 0 in the cell indicates that there is no edge."""

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))  # assign all cells of the matrix to 0

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds!".format(v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex {}".format(v))

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex {}".format(v))

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


class Node:
    """A single node in a graph represented by an adjacency set. Every node
    has a vertex Id. Each node is associated with a set of adjacent vertices.
    """

    def __init__(self, vertexId):
        self.vertexId = vertexId
        "Vertex id. It is unique for each node"
        self.adjacency_set = set()
        "A set with all adjacent nodes"

    def add_edge(self, v):
        """Description: Add an edge from this node to node ''v''."""
        if self.vertexId == v:
            raise ValueError("The vertex {} cannot be adjacent to itself!".format(v))

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        """Get a list with all adjacent vertices. The list is sorted in ascending order."""
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    """Represents a graph as an adjacency set. A graph is a list of Nodes and
    each Node has a set of adjacent vertices. This graph in this current form
    cannot be used to represent weighted edges, only unweighted edges can be represented
    """

    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex {}".format(v))

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex {}".format(v))

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


def make_graph(representation_type, numNodes, directed):
    """Helper function to create a graph for quick testing"""
    graph = representation_type(numNodes, directed=directed)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(2, 3)

    return graph


def test_graph(g):
    """Helper function to test a graph"""
    for i in range(4):
        print("Adjacent to: ", i, g.get_adjacent_vertices(i))

    for i in range(4):
        print("Indegree: ", i, g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

    g.display()


if __name__ == "__main__":
    g = make_graph(AdjacencySetGraph, 4, directed=True)
    test_graph(g)
