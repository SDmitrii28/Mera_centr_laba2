import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
G = nx.Graph()
nodes = range(7)
G.add_nodes_from(nodes)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), 
    (4, 5), (5, 6), (1, 5), (2, 4)
]
G.add_edges_from(edges)
eig_centrality = nx.eigenvector_centrality_numpy(G)
sorted_centrality = sorted(eig_centrality.items())
print("Центральность собственного вектора графа:")
for node, centrality in sorted_centrality:
    print(f"Узел {node}: {centrality:.4f}")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.show()
centrality_values = [centrality for node, centrality in sorted_centrality]

print("\nЗначения центральности:")
print(centrality_values)

print("\nПроверяем на наличие 'ямы' и 'горбика':")
is_valley_peak = (
    centrality_values[0] > centrality_values[1] and
    centrality_values[1] < centrality_values[2] and
    centrality_values[2] < centrality_values[3] and
    centrality_values[3] > centrality_values[4] and
    centrality_values[4] < centrality_values[5] and
    centrality_values[5] > centrality_values[6]
)

print(f"Последовательность имеет 'яму' и 'горбик': {is_valley_peak}")
