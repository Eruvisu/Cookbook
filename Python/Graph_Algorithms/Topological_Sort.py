"""DAG - Directed Acyclic Graph
DAGs specify precedence relationships between nodes.
Topological Sort applies to DAGs. A graph can have more than
one Topological Sort.A Topological Sort is any ordering of all
the DAG's vertices that satisfies all precedence relationships.
Topological sort should have all the dependencies of a node come
before the node itself.If a graph has a cycle there is no topological
sort for it.The in-degree of a node is the number of directed edges that
'directly flow' into that node.The in-degree determines how many nodes
that particular node depends on.This concept of 'in-degree' is used in
the topological sort algorithm. If no node has an in-degree=0, then the
graph has a cycle(i.e. it is not a DAG => there is no topological sort
order possible on the graph).
"""

from queue import Queue
from Graph_Representation import *


def topological_sort(graph):
    """Description: It finds one valid topological sort order of the
                    vertices of a graph.

    Args:
        graph: A graph data structure

    Returns: A list with the graph vertices is topological sort order.
    """
    queue = Queue()  # It will hold all vertices with in-degree=0.These are
    # the vertices that we can visit next.
    indegreeMap = {}  # Holds the in-degree of every vertex in the graph.

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        # Queue all nodes which have no dependencies i.e. no edges coming in.
        if indegreeMap[i] == 0:
            queue.put(i)

    sortedList = []  # It will hold the graph vertices in topological sort order.

    while not queue.empty():
        vertex = queue.get()
        sortedList.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v] - 1

            if indegreeMap[v] == 0:
                queue.put(v)

    if len(sortedList) != graph.numVertices:
        raise ValueError("This graph has a cycle!")

    return sortedList


def make_graph():
    """Helper function to make a graph for quick testing."""
    g = AdjacencyMatrixGraph(9, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(3, 4)
    g.add_edge(6, 8)
    return g


if __name__ == "__main__":
    g = make_graph()
    print(topological_sort(g))
