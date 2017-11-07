"""Depth-first traversal of a graph"""

from Graph_Representation import *


def depth_first(graph, visited, list_of_traversed_nodes, current=0, bPrintTraversal=False):
    """Description: Traverse a graph using the depth-first algorithm.
    At the end ''list_of_traversed_nodes'' will contain the nodes in order of traversal.

    Args:
        graph: A graph that is to be traversed.
        visited: An array with the visited vertices at any point in time.
        current: The current node in the graph that we want to process.
                At first call, this represents the starting node.
        bPrintTraversal: If True, it wil print each node while the graph is traversed.

    Returns: A list with the nodes arranged in order of traversal.
    """

    if visited[current] == 1:
        return

    visited[current] = 1  # Mark the current node as visited
    list_of_traversed_nodes.append(current)

    if bPrintTraversal:
        print("Visit: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex, bPrintTraversal)


def run_depth_first(g, start=0, bPrintTraversal=False):
    """Description: A wrapper function that creates the ''visited'' array and
    ''list_of_traversed_nodes'' list before calling the function ''depth_first''.

    Args:
        g: A graph that is to be traversed.
        bPrintTraversal: If True, it wil print each node while the graph is traversed.

    Returns: A list with the nodes arranged in order of traversal.
    """
    visited = np.zeros(g.numVertices)
    list_of_traversed_nodes = []
    depth_first(g, visited, list_of_traversed_nodes, start, bPrintTraversal)
    return list_of_traversed_nodes


def make_graph_for_DFS():
    """Helper function for quick testing."""
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
    g = make_graph_for_DFS()
    run_depth_first(g, bPrintTraversal=True)
