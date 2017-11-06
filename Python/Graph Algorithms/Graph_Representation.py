"""Classes for graph representation"""

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

        Returns: All adjacent vertices of vertex ''v''.
        """
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        """Description: Get the number of edges that are incident on a vertex
                        and flow into that vertex.
        Args:
            v: A vertex for which to find the indegree.

        Returns: The indegree of the vertex ''v''.
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
        """Description: Prints the graph. Serves as debugging aid.
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
        self.matrix = np.zeros((numVertices, numVertices))
