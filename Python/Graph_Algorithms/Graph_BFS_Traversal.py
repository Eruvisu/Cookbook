"""Breadth-first traversal of a graph"""

from queue import Queue
from Graph_Representation import *


def breadth_first(graph, start=0, bPrintTraversal=False):
    """Description: Traverse a graph using the breadth-first algorithm.

    Args:
        graph: A graph that is to be traversed.
        start: The node fom where the traversal will start.
        bPrintTraversal: If True, it wil print each node while the graph is traversed.

    Returns: A list with the nodes arranged in order of traversal.
    """

    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)  # Matrix to remember the visited nodes.
    list_of_traversed_nodes = []  # A list to save the nodes in order of traversal

    while not queue.empty():
        vertex = queue.get()
        if visited[vertex] == 1:
            continue

        if bPrintTraversal:
            print("Visit: ", vertex)
        visited[vertex] = 1  # Add the node to the list of visited vertices
        list_of_traversed_nodes.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)

    return list_of_traversed_nodes


def make_graph_for_BFS():
    """Helper function to create a graph for quick testing"""
    g = AdjacencyMatrixGraph(9, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)
    return g


if __name__ == "__main__":
    g = make_graph_for_BFS()
    breadth_first(g, 0, True)
