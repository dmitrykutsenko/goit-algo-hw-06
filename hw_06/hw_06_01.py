# граф за допомогою бібліотеки networkX

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()


# Додавання вершин і одразу ребер
G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 7), (3, 8), (4, 6), (4, 7), (7, 8), (3, 5)])

# Візуалізація графа
nx.draw(G, node_size=600, with_labels=True)
plt.show()

# Кількість вершин і ребер
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

# Ступінь вершин
for node, degree in G.degree():
    print(f"Ступінь вершини {node}: {degree}")
