# алгоритми DFS і BFS для знаходження шляхів у графі

import networkx as nx

# Створення графа
G = nx.Graph()
# Додавання вершин і одразу ребер
G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 7), (3, 8), (4, 6), (4, 7), (7, 8), (3, 5)])


# Функція для DFS
def dfs(graph, start, end):
    stack = [start]
    visited = set()
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node == end:
                return path
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

    return None


# Функція для BFS
def bfs(graph, start, end):
    queue = [start]
    visited = set()
    path = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node == end:
                return path
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

    return None


# Пошук шляху з вершини 1 до вершини 7
path_dfs = dfs(G, 1, 8)
path_bfs = bfs(G, 1, 8)

# Порівняння шляхів
print(f"Шлях DFS: {path_dfs}")
print(f"Шлях BFS: {path_bfs}")


"""
Порівняння отриманих результатів:

    DFS: Шлях DFS проходить через вершини 1, 2, 4, 7, 8.
    BFS: Шлях BFS проходить через вершини 1, 2, 3, 4, 7, 8.

Пояснення:

    DFS: 
        використовує стек
        зазвичай бирає найглибший шлях на кожному кроці.
        може проходити через одні й ті вершини кілька разів.
    BFS: 
        використовуєте чергу
        зазвичай бирає найкоротший шлях до вершини на кожному кроці.
        не проходить через одні й ті вершини кілька разів.

    Наш граф не зважений, тому тут немає чіткості стосовно "найглибшого" і "найкоротшого" шляху.

    DFS:
        Починаючи з вершини 1, DFS досліджує всі можливі шляхи,
        спершу йдучи вглиб графа, перш ніж перейти до наступних вершин.
        Це призводить до того, що DFS знаходить шлях 1-2-4-7-8
        який є найглибшим шляхом з вершини 1 до вершини 8.
    BFS:
        BFS досліджує всі вершини на однаковій відстані від
        початкової вершини, перш ніж перейти до наступних вершин.
        Це призводить до того, що BFS знаходить шлях інакше.

"""
