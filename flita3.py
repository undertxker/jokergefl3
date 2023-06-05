import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def read_adjacency_matrix(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        adjacency_matrix = [list(map(int, line.split())) for line in lines]
    return nx.from_numpy_array(np.array(adjacency_matrix))

def is_connected(graph):
    num_nodes = len(graph.nodes())
    num_edges = len(graph.edges())
    if num_edges >= num_nodes-1 and nx.is_connected(graph):
        return True
    else:
        return False

def plot_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    plt.show(block=True)
    plt.pause(0.001)

file_name = "matrix.txt"
graph = read_adjacency_matrix(file_name)

if is_connected(graph):
    print("Граф связный")
else:
    print("Граф не связный")

plot_graph(graph)
