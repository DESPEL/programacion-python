
# graph: list of edges


def get_path(graph, size, actual, visited=None):
    if visited is None:
        visited = []
    else:
        visited = visited.copy()
    if len(visited) == len(graph):
        return visited

    neighbors = filter(lambda x: actual in x, graph)
    for neighbor in neighbors:
        if neighbor not in visited:
            next_ = neighbor[0] if neighbor[1] == actual else neighbor[1]
            path_ = get_path(graph, size, next_, visited+[neighbor])
            if path_:
                return path_
    return None


def find_eulerian_path(graph):
    sz = len(graph)
    numbers = list(set(sum(graph, [])))

    for node in numbers:
        path_ = get_path(graph, sz, node)
        if path_ is not None:
            return path_


path_ = find_eulerian_path([
    [0, 1], [0, 2], [0, 3],
    [1, 2], [1, 4],
    [2, 3], [2, 4],
    [3, 4],
])

print(path_)

path_ = find_eulerian_path([
    [0, 1], [0, 2], [0, 3], [0, 4], [0, 5],
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 5],
    [3, 4], [3, 5],
    [4, 5]
])

print(path_)