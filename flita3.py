import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Проверка графа на связность
def is_connected(graph):
    num_nodes = len(graph.nodes())
    num_edges = len(graph.edges())
    if num_edges >= num_nodes-1 and nx.is_connected(graph):
        return True
    else:
        return False

matrix = []
#Чтение матрицы из файла
with open('matrix.txt', 'r') as f:
    for line in f:
        matrix.append([int(x) for x in line.split()])

#Создание графа из матрицы смежности
graph = nx.from_numpy_array(np.array(matrix), create_using=nx.Graph)

#Вычисление позиций вершин для отображения графа
pos = nx.spring_layout(graph)

#Отрисовка графа с помощью Matplotlib
nx.draw(graph, pos)
# Установка размера фигуры
nx.draw(graph, pos, with_labels=True, node_size=500, font_size=10, font_weight='bold')

if is_connected(graph):
    print("Граф связный")
else:
    print("Граф не связный")

plt.show()
