# алгоритм Дейкстри

import networkx as nx
import heapq

# Додавання вершин і ребер до графа
G = nx.Graph()
G.add_edges_from([(1, 2, {'weight': 7}), (2, 3, {'weight': 1}), (2, 4, {'weight': 8}),
                  (3, 7, {'weight': 4}), (3, 8, {'weight': 5}), (4, 6, {'weight': 3}),
                  (4, 7, {'weight': 2}), (7, 8, {'weight': 1}), (3, 5, {'weight': 6})])


# Функція для алгоритму Дейкстри
def dijkstra(graph, start):
    """
    Знаходить найкоротші шляхи від вершини `start` до всіх інших вершин графа `graph`.

    Args:
        graph: Граф, представлений словником суміжності.
        start: Початкова вершина.

    Returns:
        Словник, де ключем є вершина, а значенням - список, 
        що містить найкоротший шлях від `start` до цієї вершини.
    """

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Функція для алгоритму Дейкстри
def dijkstra_all(graph):
  """
  Знаходить найкоротші шляхи від **всіх** вершин до **всіх** інших вершин графа `graph`.

  Args:
    graph: Граф, представлений словником суміжності.

  Returns:
    Словник, де ключем є пара вершин (start, end), а значенням - 
    найкоротша відстань між ними.
  """

  distances = {}
  for start in graph:
      distances[start] = dijkstra(graph, start)

  return distances


# Знаходження всіх найкоротших шляхів
distances = dijkstra_all(G)

# Вивід результатів
print(f"Згідно алгоритму Дейкстри")
print(f"Найкоротші шляхи з урахуванням ваги є такими:")
for start, distance in distances.items():
    print()
    for destination, distance in distance.items():
        print(f"  від {start} до {destination}: {distance}")
